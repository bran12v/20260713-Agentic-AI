"""All the necessary code to persist a turn on disk. (store all info on a given run)

A trace is what an engineer will look at for a few hours/days. A run record is something
    that an engineer might come back to 2 year later."""

import json
from collections.abc import Sequence
from pathlib import Path
from opentelemetry.sdk.trace import ReadableSpan
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult

PATH = Path("run_records.json")

class RunRecordExporter(SpanExporter):
    """Fold each trace into one append-only JSON row."""

    def __init__(self, path: Path = PATH):
        self.path = path
        self.spans: list[ReadableSpan] = []

    def export(self, spans: Sequence[ReadableSpan]) -> SpanExportResult:
        self.spans.extend(spans)
        return SpanExportResult.SUCCESS

    def force_flush(self, timeout_millis = 30000) -> bool:
            return True

    def shutdown(self) -> None:
        by_trace: dict[str, list[ReadableSpan]] = {}
        for span in self.spans:
            by_trace.setdefault(f"{span.context.trace_id:032x}", []).append(span)

        with self.path.open("a", encoding="utf-8") as handle:
            for trace_id, spans in by_trace.items():
                handle.write(json.dumps(_row(trace_id, spans)) + "\n")

def _ms(span: ReadableSpan) -> int:
    return round((span.end_time - span.start_time) / 1_000_000)

def _row(trace_id: str, spans: list[ReadableSpan]) -> dict:
    pairs = [(s, s.attributes or {}) for s in sorted(spans, key=lambda s: s.start_time)]
    root = next((s for s, _ in pairs if s.parent is None), pairs[0][0])

    def of(operation: str):
        # Match on the CONVENTION, never on the span's display name.
        return [(s, a) for s, a in pairs if a.get("gen_ai.operation.name") == operation]

    return {
        "correlation_id": (root.attributes or {}).get("turn.correlation_id", ""),
        "trace_id": trace_id,
        "duration_ms": _ms(root),
        # Per-call model and tokens - what the brief asks to be measured rather
        # than estimated. E6 prices exactly this list; nothing here costs money.
        "model_calls": [
            {"model": a.get("gen_ai.response.model"),
             "input_tokens": a.get("gen_ai.usage.input_tokens", 0),
             "output_tokens": a.get("gen_ai.usage.output_tokens", 0),
             "reasoning_tokens": a.get("gen_ai.usage.reasoning.output_tokens", 0),
             "duration_ms": _ms(s)} for s, a in of("chat")],
        "tool_calls": [
            {"name": a.get("gen_ai.tool.name"), "duration_ms": _ms(s)}
            for s, a in of("execute_tool")],
        "retrievals": [
            {"doc_ids": list(a.get("retrieval.doc_ids", [])),
             "chunk_ids": list(a.get("retrieval.chunk_ids", [])),
             "scores": list(a.get("retrieval.scores", [])),
             "top_score": a.get("retrieval.top_score")} for s, a in of("retrieve")],
        "guardrails": [
            {"stage": a.get("guardrail.stage"), "allowed": a.get("guardrail.allowed"),
             "reason": a.get("guardrail.reason"), "top": a.get("guardrail.top"),
             "tau": a.get("guardrail.tau"), "dropped": a.get("guardrail.dropped")}
            for _, a in pairs if "guardrail.stage" in a],
    }