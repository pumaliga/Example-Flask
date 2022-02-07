from flask import Blueprint, request

views = Blueprint("views", __name__)



@views.route("/", methods=["POST"])
def index():
    print(request.json)
    return {"Ok": True}

