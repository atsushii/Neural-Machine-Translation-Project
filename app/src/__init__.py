from src import views
from flask import Flask, Blueprint
import tensorflow as tf
from .views.views import view_blueprint

app = Flask(__name__, static_url_path="/static")
app.register_blueprint(view_blueprint)
