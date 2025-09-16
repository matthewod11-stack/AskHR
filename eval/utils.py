
import requests
import time
import re
import csv
import os
import json
from typing import List
from schema import CaseRow

def read_cases_csv(path: str) -> List[CaseRow]:
    cases = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            must_have = [kw.strip() for kw in row["must_have"].split("|")]
            min_citations = int(row["min_citations"]) if row.get("min_citations") else 2
            k = int(row["k"]) if row.get("k") else 8
            cases.append(CaseRow(
                id=row["id"],
                question=row["question"],
                must_have=must_have,
                min_citations=min_citations,
                k=k
            ))
    return cases

def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())

def score_keywords(answer: str, keywords: List[str]) -> float:
    answer_norm = normalize(answer)
    found = sum(1 for kw in keywords if kw.lower() in answer_norm)
    return 100.0 * found / max(1, len(keywords))

def post_ask(api_url: str, query: str, k: int, timeout: int) -> dict:
    payload = {"query": query, "k": k}
    resp = requests.post(api_url, json=payload, timeout=timeout)
    resp.raise_for_status()
    return resp.json()

def timestamp_dir(base="eval/results") -> str:
    ts = time.strftime("%Y%m%d-%H%M")
    path = os.path.join(base, ts)
    os.makedirs(path, exist_ok=True)
    return path

def write_csv(path, rows: List[dict]):
    if not rows:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def write_json(path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def exponential_backoff(attempt: int, base: float = 0.5) -> float:
    return base * (2 ** attempt)
