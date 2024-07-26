from flask import Flask

from views.dashboard_views import dashboard_bp
from core.config import Config as cfg

def create_app() -> Flask:
    app = Flask(__name__,template_folder=cfg.TEMPLATE_DIR)
    print(cfg.TEMPLATE_DIR)
    app.config.from_object("core.config")
    # register blueprint
    app.register_blueprint(dashboard_bp)

    return app