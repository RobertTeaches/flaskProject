from flask import Flask, render_template, flash, redirect
from configs.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)

from app import routes
from app.data_models.encoder import JSONEncoder

app.json_encoder = JSONEncoder