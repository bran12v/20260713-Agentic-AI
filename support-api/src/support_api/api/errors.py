from __future__ import annotations

import structlog
from flask import Flask
from pydantic import ValidationError     # Pydantic v2 raises this on validate

log = structlog.get_logger(__name__)


class DomainError(Exception):
    """Base class — subclasses override status_code + error_code."""
    status_code = 500
    error_code = "internal_error"

    def __init__(self, message: str, **context) -> None:
        super().__init__(message)
        self.message = message
        self.context = context

    def envelope(self) -> dict:
        # Canonical error shape: {"error": slug, "message": ..., ...context}
        return {"error": self.error_code, "message": self.message, **self.context}


class TicketNotFound(DomainError):
    status_code = 404
    error_code = "ticket_not_found"

    def __init__(self, ticket_id: str) -> None:
        super().__init__(f"no ticket with id {ticket_id}", ticket_id=ticket_id)


class ConflictError(DomainError):
    status_code = 409
    error_code = "conflict"

def register_error_handlers(app: Flask) -> None:
    """Wire handler functions to the app. Called from create_app()."""

    @app.errorhandler(ValidationError)
    def _validation(e: ValidationError):
        # e.errors() → list of {loc, type, msg, input, url}. Slim to 3 keys.
        details = [
            {
                "field": ".".join(str(x) for x in err["loc"]),
                "type": err["type"],
                "message": err["msg"],
            }
            for err in e.errors()
        ]
        log.info("validation_failed", error_count=len(details))
        return {
            "error": "validation_failed",
            "message": "request body failed validation",
            "details": details,
        }, 422  # Unprocessable Entity

    @app.errorhandler(DomainError)
    def _domain(e: DomainError):
        log.info("domain_error", error_code=e.error_code, **e.context)
        return e.envelope(), e.status_code

    @app.errorhandler(404)
    def _404(_e):
        return {"error": "route_not_found",
                "message": "no route matches this URL and method"}, 404

    @app.errorhandler(405)
    def _405(e):
        # werkzeug HTTPException carries .valid_methods
        return {"error": "method_not_allowed",
                "message": "this URL does not accept that HTTP method",
                "allowed": sorted(e.valid_methods or [])}, 405

    @app.errorhandler(500)
    def _500(_e):
        log.error("internal_error", exc_info=True)  # traceback → logs, not response
        return {"error": "internal_server_error",
                "message": "an unexpected error occurred"}, 500