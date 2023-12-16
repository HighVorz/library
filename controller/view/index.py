
from flask import Blueprint
from flask import render_template

route_index = Blueprint('index', __name__)

@route_index.route("/")
def index():
    return render_template("index.html")


