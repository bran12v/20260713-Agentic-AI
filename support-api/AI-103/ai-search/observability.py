"""Where our spans go.

The Agent Framework emits the spans; this module will define what will happen to them."""

from collections.abc import Sequence

from opentelemetry.sdk.trace import ReadableSpan
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult
from opentelemetry.trace import StatusCode, get_tracer

from contextlib import contextmanager
from typing import Any

PRINTED = ("gen_ai.", "retrieval.", "guardrail.")

class TreeExporter(SpanExporter):
    """Buffers spans, the print them as a tree when the process completes.
    
    An exporter has three methods:
        * export - called with a batch of finished spans
        * shutdown - the hook that fires at the end to summarize
        * force_flush
    """

    def __init__(self) -> None:
        self.spans: list[ReadableSpan] = []

    def export(self, spans: Sequence[ReadableSpan]) -> SpanExportResult:
        self.spans.extend(spans)
        return SpanExportResult.SUCCESS

    def force_flush(self, timeout_millis = 30000) -> bool:
        return True

    def shutdown(self) -> None:
        """Reconstructing the Trace based on all the spans and their parent pointers."""
        by_parent: dict[int | None, list[ReadableSpan]] = {}
        for span in self.spans:
            by_parent.setdefault(span.parent.span_id if span.parent else None, []).append(span) # setting the key and value

        def emit(parent_id: int | None, depth: int) -> None:
            """This helper funtion will actually print out the trace tree."""
            for span in sorted(by_parent.get(parent_id, []), key=lambda s: s.start_time):
                sec = (span.end_time - span.start_time) / 1_000_000_000
                mark = "!" if span.status.status_code is StatusCode.ERROR else " "
                print(f"{mark}{'  ' * depth}{span.name}  ({sec:.0f} sec)")
                for key in sorted(span.attributes or {}):
                    if key.startswith(PRINTED):
                        print(f" {'  ' * depth}    {key} = {str(span.attributes[key])[:72]}")
                emit(span.context.span_id, depth + 1)

        print("\n--- trace ---")
        emit(None, 0)

def start_tracing(*, exporters: list[SpanExporter] | None = None) -> TreeExporter:
    """Turn on the framework's OpenTelemetry layer and choose the destination for the spans."""
    from agent_framework.observability import configure_otel_providers

    tree = TreeExporter()
    configure_otel_providers(
        exporters=[tree, *(exporters or [])],
        # Prompts, completions and tool arguments are set to OFF
        enable_sensitive_data=False
    )
    return tree

def tracer():
    """One tracer for everything this project instruments by hand."""
    return get_tracer("delivery-standards.harness")

@contextmanager
def retrieval_span(query: str, *, top_k: int, capture_query: bool = False):
    """Wrap a search. Record the EVIDENCE about the request - ids, scores, not the text."""
    with tracer().start_as_current_span("retrieve delivery-standards") as span:
        span.set_attribute("gen_ai.operation.name", "retrieve")
        span.set_attribute("retrieval.top_k", top_k)
        if capture_query:
            span.set_attribute("retrieval.query", query[:1000])

        def record(rows: list[dict[str, Any]]) -> None:
            span.set_attribute("retrieval.hit_count", len(rows))
            span.set_attribute("retrieval.chunk_ids", [row["chunk_id"] for row in rows])
            span.set_attribute("retrieval.doc_ids", [row["doc_id"] for row in rows])
            scores = [round(row["reranker"], 2) for row in rows if row.get("reranker") is not None]
            span.set_attribute("retrieval.scores", scores)
            span.set_attribute("retrieval.top_score", max(scores, default=0.0))

        span.record = record
        yield span

@contextmanager
def guardrail_span(stage: str):
    """One span per guardrail decision. """
    with tracer().start_as_current_span(f"guardrail {stage}", record_exception=False, set_status_on_exception=False) as span:
        span.set_attribute("guardrail.stage", stage)

        def record(*, allowed: bool, reason: str, **details: Any):
            span.set_attribute("guardrail.allowed", allowed)
            span.set_attribute("guardrail.reason", reason)
            for key, value in details.items():
                span.set_attribute(f"guardrail.{key}", value)

        span.record = record
        yield span