from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("core.config")
    return app