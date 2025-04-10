from flask import Flask
from app.routes import bp
from app.models import Transaction, Base
from app.database import engine


app = Flask(__name__)
app.register_blueprint(bp)
Base.metadata.create_all(bind=engine)


@app.route("/")
def home():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)
