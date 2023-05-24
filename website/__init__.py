from flask import Flask

def create_app():
    app = Flask(__name__) # __name__ represents name of the file that runs
    app.config['SECRET_KEY'] = 'abcdefghijk'

    return app


