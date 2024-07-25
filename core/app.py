from flask import Flask

from views.dashboard_views import dashboard_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("core.config")
    # register blueprint
    app.register_blueprint(dashboard_bp)

    return app