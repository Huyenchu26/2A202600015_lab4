from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv
import re

load_dotenv()

# 1. Đọc System Prompt

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# 2. Khai báo State

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    user_info: dict  # Lưu trữ: origin, destination, budget, dates

# 2.5. Memory Extraction Function

def extract_user_info(messages: list, current_info: dict) -> dict:
    """Trích xuất thông tin người dùng từ conversation history"""
    info = current_info.copy()
    
    cities_map = {
        "hà nội": "Hà Nội",
        "đà nẵng": "Đà Nẵng", 
        "phú quốc": "Phú Quốc",
        "hồ chí minh": "Hồ Chí Minh",
        "hcm": "Hồ Chí Minh"
    }
    
    # Tìm thông tin từ human messages
    for msg in messages[-20:]:  # Xem 20 message gần nhất
        if hasattr(msg, 'type') and msg.type == 'human':
            text = msg.content.lower()
        elif isinstance(msg, tuple) and msg[0] == 'human':
            text = msg[1].lower()
        else:
            continue
        
        # Extract origin (từ ... tới/đến)
        from_match = re.search(r'từ\s+([a-zăâôơư\s]+?)(?:\s+(?:tới|đến)\s+|,|\s*$)', text)
        if from_match:
            from_text = from_match.group(1).strip()
            for city, proper in cities_map.items():
                if city in from_text:
                    info["origin"] = proper
                    break
        
        # Extract destination (tới/đến ... từ/,/.)
        for word in ["tới", "đến"]:
            dest_match = re.search(rf'{word}\s+([a-zăâôơư\s]+?)(?:\s+từ|\s*$|,)', text)
            if dest_match:
                dest_text = dest_match.group(1).strip()
                for city, proper in cities_map.items():
                    if city in dest_text:
                        info["destination"] = proper
                        break
        
        # Extract budget (số triệu)
        budget_match = re.search(r'(\d+)\s*triệu', text)
        if budget_match:
            info["budget"] = f"{budget_match.group(1)} triệu"
        
        # Extract dates (XX/XX hoặc XX-XX)
        dates = re.findall(r'(\d{1,2})[/-](\d{1,2})', text)
        if dates:
            date_str = "/".join(dates[0])
            if len(dates) > 1:
                date_str += " - " + "/".join(dates[-1])
            info["dates"] = date_str
    
    return info

# 3. Khởi tạo LLM và Tools

tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node

def agent_node(state: AgentState):
    messages = state["messages"]
    user_info = state.get("user_info", {})
    
    # Extract updated info từ conversation
    user_info = extract_user_info(messages, user_info)
    
    # Xây dựng system prompt với memory context
    memory_context = ""
    if user_info:
        info_lines = []
        if user_info.get("origin"):
            info_lines.append(f"- Thành phố khởi hành: {user_info['origin']}")
        if user_info.get("destination"):
            info_lines.append(f"- Thành phố đến: {user_info['destination']}")
        if user_info.get("dates"):
            info_lines.append(f"- Ngày đi/về: {user_info['dates']}")
        if user_info.get("budget"):
            info_lines.append(f"- Ngân sách: {user_info['budget']}")
        
        if info_lines:
            memory_context = "\n<memory>\nThông tin người dùng đã cung cấp:\n" + "\n".join(info_lines) + "\nKhi trả lời, hãy tham chiếu các thông tin này và không hỏi lại. Chỉ hỏi những thông tin còn thiếu.\n</memory>\n"
    
    # System prompt với memory
    system_content = memory_context + SYSTEM_PROMPT
    
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=system_content)] + messages
    
    response = llm_with_tools.invoke(messages)
    
    # === LOGGING ===
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"Gọi tool: {tc['name']}({tc['args']})")
    else:
        print(f"Trả lời trực tiếp")
    
    return {"messages": [response], "user_info": user_info}

# 5. Xây dựng Graph

builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")
builder.add_edge("agent", END)

graph = builder.compile()

# 6. Chat loop

if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy — Trợ lý Du lịch Thông minh")
    print(" Gõ 'quit' để thoát")
    print("=" * 60)
    
    user_info = {}
    conversation_history = []  # Lưu toàn bộ messages
    
    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
        
        # Add user message vào history
        conversation_history.append(("human", user_input))
        
        print("\nTravelBuddy đang suy nghĩ...")
        # Pass toàn bộ history, không chỉ message mới
        result = graph.invoke({"messages": conversation_history, "user_info": user_info})
        
        # Extract assistant response
        final = result["messages"][-1]
        
        # Add assistant response vào history
        if hasattr(final, 'content'):
            conversation_history.append(("assistant", final.content))
        
        user_info = result.get("user_info", {})
        print(f"\nTravelBuddy: {final.content}")