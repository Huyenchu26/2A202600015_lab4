#!/usr/bin/env python3
"""
Test script để chạy 5 test cases cho TravelBuddy Agent
"""
from agent import graph

# Test cases từ PHẦN 4 của guide.md
test_cases = [
    {
        "name": "Test 1 — Direct Answer (Không cần tool)",
        "input": "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
        "expected": "Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào."
    },
    {
        "name": "Test 2 — Single Tool Call",
        "input": "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng, lịch trình linh hoạt",
        "expected": "Gọi search_flights('Hà Nội', 'Đà Nẵng'), liệt kê 4 chuyến bay."
    },
    {
        "name": "Test 3 — Multi-Step Tool Chaining",
        "input": "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm vào tuần tới, budget 5 triệu. Tư vấn giúp!",
        "expected": "Chuỗi nhiều bước: search_flights + search_hotels + calculate_budget"
    },
    {
        "name": "Test 4 — Missing Info / Clarification",
        "input": "Tôi muốn đặt khách sạn",
        "expected": "Agent hỏi lại: thành phố nào? bao nhiêu đêm? ngân sách bao nhiêu?"
    },
    {
        "name": "Test 5 — Guardrail / Refusal",
        "input": "Giải giúp tôi bài tập lập trình Python về linked list",
        "expected": "Từ chối lịch sự, nói rằng chỉ hỗ trợ về du lịch."
    }
]

print("=" * 80)
print("🧪 TEST CASES CHO TRAVELBUDDY AGENT - PHẦN 4")
print("=" * 80)

for i, test in enumerate(test_cases, 1):
    print(f"\n{'='*80}")
    print(f"📋 {test['name']}")
    print(f"{'='*80}")
    print(f"\n👤 Người dùng: {test['input']}")
    print(f"\n⏳ TravelBuddy đang suy nghĩ...\n")
    
    try:
        result = graph.invoke({"messages": [("human", test['input'])]})
        final = result["messages"][-1]
        print(f"🤖 TravelBuddy: {final.content}")
        print(f"\n✅ Kỳ vọng: {test['expected']}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

print(f"\n{'='*80}")
print("✨ KẾT THÚC TEST SUITE")
print(f"{'='*80}\n")
