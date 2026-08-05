from flask import Flask, g
import os
from support_api.api.blueprints.tickets import bp as ticket_bp
from support_api.api.blueprints.health import bp as health_bp
from support_api.logging import configure_logging
from support_api.api.errors import register_error_handlers
from support_api.api.middleware import register_request_logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app(database_url: str | None = None) -> Flask:
    """Main entrypoint for the creation of the flask app."""
    # on app startup first we want to configure our logs so that resource logs are
    # owned by structlog.
    configure_logging()

    # __name__ tells flask where it is in our file structure
    app = Flask(__name__)

    app.config["DATABASE_URL"] = str(
        database_url or os.environ.get("DATABASE_URL")
    )

    # mount the blueprints to the flask app to allow them to be accessable.
    app.register_blueprint(ticket_bp, url_prefix="/tickets") # localhost:5000/tickets
    app.register_blueprint(health_bp)
    # url_prefix defines what the routes for this registration start with

    Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["20 per minute"],
        storage_uri="memory://"
    )

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
