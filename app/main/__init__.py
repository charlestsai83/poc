from flask import Blueprint

main = Blueprint('main', '__main__')

from . import index
