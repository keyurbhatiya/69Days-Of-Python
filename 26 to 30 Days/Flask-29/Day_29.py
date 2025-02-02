################################## Day 29: 69 Days of Python #####################################
# Flask
# Flask is a micro web framework written in Python.

#  Flask is a lightweight backend framework with minimal dependencies.
#  Flask is easy to learn because its simple and intuitive API makes it easy to learn and use for beginners.
#  Flask is a flexible Framework because it allows you to customize and extend the framework to suit your needs easily.
#  Flask can be used with any database like:- SQL and NoSQL and with any Frontend Technology such as React or Angular.
#  Flask is great for small to medium projects that do not require the complexity of a large framework.
#  Flask Documentation

# Started With Flask
# from flask import Flask     
# app = Flask(__name__)   # Flask constructor 
  
# # A decorator used to tell the application 
# # which URL is associated function 
# @app.route('/')       
# def hello(): 
#     return 'HELLO'


# # decorator to route URL 
# @app.route("/hello") 
# # binding to the function of router
# def hello_world():
#    return 'Hello, World!'


  
# if __name__=='__main__': 
#   app.debug = True
#   app.run() 

# Variables in Flask
# from flask import Flask 
# app = Flask(__name__) 

# # routing the decorator function hello_name 
# @app.route('/hello/<name>') 
# def hello_name(name): 
#     return 'Hello %s!' % name 

# if __name__ == '__main__':
#     app.debug = True
#     app.run()

# open this url http://127.0.0.1:5000/hello/keyur

# Build a URL in Flask
'''
from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
'''
# Output

# Inputfile: http://localhost:5000/user/admin
# Output: Hello Admin 

# Input: http://localhost:5000/user/ABC
# Output: Hello ABC as Guest


# Serve Static Files in Flask
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
'''