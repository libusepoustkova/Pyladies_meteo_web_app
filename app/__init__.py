from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="assets")
app.config.from_object(Config)
db = SQLAlchemy(app)
print(Config.SQLALCHEMY_DATABASE_URI)
from app import routes, models