#! /bin/python3

from flask import Flask

app = Flask('__main__')

@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run()