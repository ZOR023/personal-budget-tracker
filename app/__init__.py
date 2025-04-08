from flask import Flask
from .database import engine,Base
from .routes import bp


def create_app():
  app = Flask(__name__)
  Base.metadata.create_all(bind = engine)
  app.register_blueprint(bp)
  return app


