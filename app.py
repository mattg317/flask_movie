from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.conf['SQLALCHEMY_DATABASE_URI']
db =SQLAlchemy(app)

@app.route('/')
def index():
	return "<h1>hello flask</h1>"

if __name__ == "__main__":
	app.run()
