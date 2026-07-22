from flask import Flask, g
from pathlib import Path
import os
from support_api.api.blueprints.tickets import bp as ticket_bp
from support_api.logging import configure_logging
from support_api.api.errors import register_error_handlers
from support_api.api.middleware import register_request_logging

_DEFAULT_DB_PATH = (
    Path(__file__).resolve().parent.parent.parent.parent / "tickets.db"
)

def create_app(db_path: Path | str | None = None) -> Flask:
    """Main entrypoint for the creation of the flask app."""
    # on app startup first we want to configure our logs so that resource logs are
    # owned by structlog.
    configure_logging()

    # __name__ tells flask where it is in our file structure
    app = Flask(__name__)

    app.config["DB_PATH"] = str(
        db_path or os.environ.get("DB_PATH") or _DEFAULT_DB_PATH
    )

    # mount the blueprints to the flask app to allow them to be accessable.
    app.register_blueprint(ticket_bp, url_prefix="/tickets") # localhost:5000/tickets
    # url_prefix defines what the routes for this registration start with

    register_error_handlers(app)
    register_request_logging(app)

    @app.teardown_appcontext
    def _close_db(_exc): # function that will close db connction when app is closed.
        db = g.pop("db", None)
        if db is not None:
            db.close()


    # tiny top level route for smoke-testing
    @app.route("/", methods=["GET"]) # root
    def index() -> dict[str, str]:
        return {"service": "support-api", "version": "1.0.0"}
    
    return app
