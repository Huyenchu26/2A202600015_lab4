# -*- coding: utf-8 -*-
"""
Ngày 14 — Endpoint sản phẩm hóa cho RAG (khung sẵn).

Chạy:
    cd docs
    uvicorn day14_app:app --reload --port 8000

POST /answer   body: {"query": "..."}   -> {answer, sources, latency_ms, tokens, cost_usd, need_review}
POST /answer/stream                      -> streaming câu trả lời (SSE / text/plain)

Điền các phần # TODO. KHÔNG hardcode API key — đọc từ biến môi trường OPENAI_API_KEY.
"""
import os
import json
import time
import hashlib

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="Day14 RAG Service")

MODEL = "gpt-4.1-mini"
EMBED_MODEL = "text-embedding-3-small"
LOG_PATH = "day14_requests.jsonl"

# Bảng giá (USD / 1M token) — cập nhật theo openai.com/pricing
PRICE_IN = 0.15 / 1_000_000
PRICE_OUT = 0.60 / 1_000_000

# ----------------------------------------------------------------------
# Corpus + retrieval (tái dùng logic Ngày 9 — rút gọn ở đây)
# ----------------------------------------------------------------------
# TODO: nạp corpus "Sổ tay chính sách IT" (8 đoạn, mỗi đoạn 1 source_id) như Ngày 9.
CORPUS = []  # [{"source_id": "IT-001", "text": "..."}, ...]

_embed_cache = {}   # cache embedding theo hash(text)
_answer_cache = {}  # cache câu trả lời theo hash(query)


def _key(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def get_embedding(text: str):
    k = _key(text)
    if k in _embed_cache:
        return _embed_cache[k]
    # TODO: gọi client.embeddings.create(model=EMBED_MODEL, input=text)
    # TODO: lưu vào _embed_cache rồi return
    raise NotImplementedError


def retrieve(query: str, k: int = 3):
    # TODO: cosine similarity giữa query và CORPUS (numpy), trả top-k {source_id, text, score}
    raise NotImplementedError


def build_prompt(query: str, results):
    context = "".join(f"[{r['source_id']}]\n{r['text']}\n\n" for r in results)
    return (
        "Chỉ trả lời dựa trên ngữ cảnh. Nếu không có thông tin, trả lời "
        "'Không tìm thấy trong tài liệu.'. Luôn trích nguồn [source_id].\n\n"
        f"Ngữ cảnh:\n{context}\nCâu hỏi:\n{query}\n"
    )


def estimate_cost(usage) -> float:
    # TODO: usage.prompt_tokens * PRICE_IN + usage.completion_tokens * PRICE_OUT
    raise NotImplementedError


def log_request(record: dict):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ----------------------------------------------------------------------
# API
# ----------------------------------------------------------------------
class Query(BaseModel):
    query: str
    k: int = 3


@app.post("/answer")
def answer(q: Query):
    t0 = time.perf_counter()

    if not q.query.strip():
        return {"answer": "Câu hỏi rỗng.", "sources": [], "latency_ms": 0,
                "tokens": 0, "cost_usd": 0.0, "need_review": True}

    ck = _key(f"{q.query}|{q.k}")
    if ck in _answer_cache:
        cached = dict(_answer_cache[ck])
        cached["latency_ms"] = round((time.perf_counter() - t0) * 1000, 2)
        cached["cached"] = True
        log_request(cached)
        return cached

    # TODO: results = retrieve(q.query, q.k)
    # TODO: resp = client.chat.completions.create(model=MODEL, temperature=0,
    #           messages=[{"role": "user", "content": build_prompt(q.query, results)}])
    # TODO: text = resp.choices[0].message.content; tokens = resp.usage.total_tokens
    # TODO: cost = estimate_cost(resp.usage); sources = [r["source_id"] for r in results]

    latency_ms = round((time.perf_counter() - t0) * 1000, 2)
    result = {
        "answer": None,        # TODO: text
        "sources": [],         # TODO: sources
        "latency_ms": latency_ms,
        "tokens": 0,           # TODO: tokens
        "cost_usd": 0.0,       # TODO: cost
        "need_review": False,
        "cached": False,
    }
    _answer_cache[ck] = result
    log_request(result)
    return result


@app.post("/answer/stream")
def answer_stream(q: Query):
    def gen():
        # TODO: results = retrieve(q.query, q.k)
        # TODO: stream = client.chat.completions.create(..., stream=True)
        # TODO: for chunk in stream: yield chunk.choices[0].delta.content or ""
        yield "TODO: streaming"
    return StreamingResponse(gen(), media_type="text/plain")


@app.get("/health")
def health():
    return {"status": "ok", "corpus_size": len(CORPUS)}
