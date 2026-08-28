"""The gate's JOB 2 drops chunks below tau. Multi-hop cases need TWO documents."""

from __future__ import annotations

import json
import sys

from guardrails import TAU
from kb_tool import retrieve

sys.stdout.reconfigure(encoding="utf-8")

GOLDEN = json.loads(open("corpus/golden-set.json", encoding="utf-8").read())
MULTI = [c for c in GOLDEN["cases"] if c["expect"] == "answer" and c.get("hops") == 2]

for case in MULTI:
    want = set(case["expected_doc_ids"])
    got = retrieve(case["question"], k=5)
    print(f"\n{case['id']}  needs {sorted(want)}")

    for i, r in enumerate(got, 1):
        mark = " <- WANTED" if r["doc_id"] in want else ""
        bar = "keep" if (r["reranker"] or 0) >= TAU else "DROP"
        print(f"   {i}. {r['reranker']:.2f} [{bar}] {r['doc_id']:9}{mark}")

    kept = {r["doc_id"] for r in got if (r["reranker"] or 0) >= TAU}
    lost = want - kept

    print(f"   after the filter: {sorted(want & kept)}"
          f"   *** {'BOTH SURVIVE' if not lost else f'FILTER LOST {sorted(lost)}'} ***")