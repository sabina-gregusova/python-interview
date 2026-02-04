from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "Hello from Phonexia!"


@main.route("/about")
def about():
    return "About page"
