################################## Day 30: 69 Days of Python #####################################

# Flask HTTP methods

# Flask provides a set of built-in HTTP methods for handling requests.
# These methods are used to handle different types of HTTP requests, such as GET, POST, PUT, DELETE, etc.
# Here are some of the most commonly used HTTP methods in Flask:

# GET: The GET method is used to retrieve data from a server.
# POST: The POST method is used to send data to a server.
# PUT: The PUT method is used to update data on a server.
# DELETE: The DELETE method is used to delete data from a server.
# PATCH: The PATCH method is used to update part of a resource on a server.

# Example POST request

# from flask import *  
# app = Flask(__name__)  
  
# @app.route('/login',methods = ['POST'])  
# def login():  
#       uname=request.form['uname']  
#       passwrd=request.form['pass']  
#       if uname=="keyur" and passwrd=="kabir":  
#           return "Welcome %s" %uname  
   
# if __name__ == '__main__':  
#    app.run(debug = True)  


# GET Method example

# from flask import *  
# app = Flask(__name__)  
  
  
# @app.route('/login',methods = ['GET'])  
# def login():  
#       uname=request.args.get('uname')  
#       passwrd=request.args.get('pass')  
#       if uname=="keyur" and passwrd=="kabir":  
#           return "Welcome %s" %uname  
   
# if __name__ == '__main__':  
#    app.run(debug = True)  


# Flask Templates
# Flask provides a templating engine that allows you to render HTML templates with dynamic data.
# Example
from flask import *  
app = Flask(__name__)  
# @app.route('/')  
# def message():  
#       return "<html><body><h1>Hi, welcome to the website</h1></body></html>"  
# if __name__ == '__main__':  
#    app.run(debug = True) 



# Rendering external HTML files
# @app.route('/')  
# def message():  
#       return render_template('message.html')  
# if __name__ == '__main__':  
#    app.run(debug = True) 


# Delimiters

# @app.route('/user/<uname>')  
# def message(uname):  
#       return render_template('message.html',name=uname)  
# if __name__ == '__main__':  
#    app.run(debug = True) 


# Embedding Python statements in HTML
# @app.route('/table/<int:num>')  
# def table(num):  
#       return render_template('print-table.html',n=num)  
# if __name__ == '__main__':  
#    app.run(debug = True)  


''' NEXT TOPIC : Flask Request Objects --> Day_31.py '''