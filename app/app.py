from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware

from .routes import api
from . import logger

def create_app():
    logger.debug("Creating app...")
    app = Flask(__name__)

    @app.route("/")
    def index_page():
        return render_template("index.html")

    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        "app" : ("static/sass", "static/css", "/static/css")
    })

    app.register_blueprint(api.example_bp)

    logger.debug("Starting app...")
    return app