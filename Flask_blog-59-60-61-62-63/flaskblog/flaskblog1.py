from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba24b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)