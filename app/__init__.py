from flask import Flask
from app.routes import task_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(task_routes)
    return app
