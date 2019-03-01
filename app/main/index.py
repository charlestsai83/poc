from . import main

@main.route('/')
def index_page():
    return 'hello world!'
