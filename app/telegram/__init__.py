from flask import Blueprint

telega = Blueprint('telega', __name__)

from . import views

