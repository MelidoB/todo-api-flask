#import flask, database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    #setup flask app
    app = Flask(__name__)
    #setup database properties
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)