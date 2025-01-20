from flask import Flask,render_template,request

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')

# Design
@app.route('/design')
def design():
    return render_template('design.html')

# Form
@app.route('/form')
def form():
    return render_template('form.html')

# Upload
@app.route('/upload' ,methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        school = request.form.get('school')
        college = request.form.get('college')
        phone = request.form.get('phone')
        email = request.form.get('email')
        about = request.form.get('about')
        skill1 = request.form.get('skill1')
        skill2 = request.form.get('skill2')
        skill3 = request.form.get('skill3')
        skill4 = request.form.get('skill4')


        print(fname,lname,school,college,phone,email,about,skill1,skill2,skill3,skill4)
    return 'Success'

app.run(debug=True)