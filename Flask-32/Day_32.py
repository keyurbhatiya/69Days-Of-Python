################################## Day 31: 69 Days of Python #####################################
# Flask File Uploading
'''
from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  
  
if __name__ == '__main__':  
    app.run(debug = True)  
'''


# Flask Redirect and Errors
# login.py
'''
from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("home.html")  
 
@app.route('/login')  
def login():  
    return render_template("login.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'keyur':  
        return redirect(url_for("success"))  
    return redirect(url_for("login"))  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True)  
'''
# Flask Flashing

# flashing.py
'''
from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/index')  
def home():  
    return render_template("index.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    error = None;  
    if request.method == "POST":  
        if request.form['pass'] != 'keyur':  
            error = "invalid password"  
        else:  
            flash("you are successfuly logged in")  
            return redirect(url_for('home'))  
    return render_template('login.html',error=error)  
  
      
if __name__ == '__main__':  
    app.run(debug = True) 
'''

# Flask-Mail Extension
# pip install Flask-Mail

'''
from flask import *  
# from flaskmail import *
from flask_mail import *  
  
app = Flask(__name__)  
  
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app)  
  
#configure the Message class object and send the mail from a URL  
@app.route('/')  
def index():  
    msg = Message('subject', sender = 'admin@gmail.com', recipients=['username@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    return "Mail Sent, Please check the mail id"  
  
if __name__ == '__main__':  
    app.run(debug = True)   
'''

# Email verification in flask using OTP
'''
from flask import *  
from flask_mail import *  
from random import *  
  
app = Flask(__name__)  
mail = Mail(app)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465     
app.config["MAIL_USERNAME"] = 'username@gmail.com'  
app.config['MAIL_PASSWORD'] = '*************'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
mail = Mail(app)  
otp = randint(000000,999999)  
 
@app.route('/')  
def index():  
    return render_template("index2.html")  
 
@app.route('/verify',methods = ["POST"])  
def verify():  
    email = request.form["email"]  
      
    msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
 
@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3>Email verified successfully</h3>"  
    return "<h3>failure</h3>"  
  
if __name__ == '__main__':  
    app.run(debug = True)  
'''

''' NEXT TOPIC : Flask SQLite --> Day_33.py '''