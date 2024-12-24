################################## Day 31: 69 Days of Python #####################################

# Flask Request Objects
# Attributes of the request object: Form data,arguments,cookies,files,Method,URL


# Form data retrieval on the template
'''
from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('customer.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result)  
   
if __name__ == '__main__':  
   app.run(debug = True)  
'''

# Flask Cookies
'''
from flask import *  
  
app = Flask(__name__)  
 
@app.route('/cookie')  
def cookie():  
    res = make_response("<h1>cookie is set</h1>")  
    res.set_cookie('foo','bar')  
    return res  
  
if __name__ == '__main__':  
    app.run(debug = True)  
'''

# Flask Session
'''
from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/')  
def home():  
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")  
    session['response']='session#1'  
    return res;  
 
@app.route('/get')  
def getVariable():  
    if 'response' in session:  
        s = session['response'];  
        return render_template('getsession.html',name = s)  
  
if __name__ == '__main__':  
    app.run(debug = True)  
'''

''' NEXT TOPIC : FILE UPLOADS --> Day_32.py '''