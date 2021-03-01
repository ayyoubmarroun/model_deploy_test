from flask import Flask
from microservice.services import predict_blueprint


def create_application() -> Flask:
    application = Flask(__name__)
    application.register_blueprint(predict_blueprint.predict_blueprint)
    return application