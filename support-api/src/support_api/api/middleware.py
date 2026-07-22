from __future__ import annotations

import time
import uuid

import structlog
from flask import Flask, Response, g, request

log = structlog.get_logger(__name__)


def register_request_logging(app: Flask) -> None:
    @app.before_request
    def _start() -> None:
        rid = request.headers.get("X-Request-ID") or uuid.uuid4().hex[:16]
        structlog.contextvars.clear_contextvars()
        structlog.contextvars.bind_contextvars(
            request_id=rid, method=request.method, path=request.path,
        )
        g.request_id = rid
        g.start_time = time.perf_counter()

    @app.after_request
    def _end(response: Response) -> Response:
        duration_ms = round((time.perf_counter() - g.start_time) * 1000, 1)
        log.info(
            "request_completed",
            status=response.status_code,
            duration_ms=duration_ms,
        )
        response.headers["X-Request-ID"] = g.request_id
        return response