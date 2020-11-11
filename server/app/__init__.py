from app.resources.footer_links import FooterLinks
from config import app_config
from flask import Flask
from flask_restful import Api

# from flask_cors import CORS


def create_app(flask_env):
    """Create an app for the server to run.
    flask_env should be one of the following:
        production
        development
        test
    """

    # create app and Flask-RESTful Api instance
    app = Flask(__name__)

    # Add CORS for React front end (bonnie.dev)
    # CORS(app, {r"/api/*": {"origins": "bonnie.dev"}})

    # set up config based on flask_env
    config = app_config.get(
        flask_env,
        app_config["production"],
    )  # default to production
    app.config.from_object(config)

    # for Flask-RESTful
    api = Api(app, catch_all_404s=True)

    # add resources / routes
    api.add_resource(FooterLinks, "/api/footer_links")

    return app
