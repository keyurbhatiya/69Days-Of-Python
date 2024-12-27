from flask import Flask, render_template, request, redirect, flash,session
from flask import Flask, make_response, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from flask import url_for
import pandas as pd
import json
import io
from fpdf import FPDF
from flask import send_file
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages


# Function to establish a DB connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="project_management"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        app.logger.error(f"Database connection failed: {e}")
        return None

# Route to render the login page
@app.route('/')
def home():
    return render_template('login.html')


# Route to handle login form submission
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    # Check if the email exists and the password matches
    if email == "keyur@admin.com" and password == "keyur@password":
        session['user'] = email  # Store user in session
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid email or password. Please try again.', 'danger')
        return redirect(url_for('home'))
    


# Route for a protected dashboard page
@app.route('/dashboard')
def dashboard():
    connection = None
    try:
        connection = get_db_connection()
        if not connection:
            app.logger.error("Database connection failed!")
            return render_template('error.html', error_message="Unable to connect to the database. Please try again later.")

        cursor = connection.cursor(dictionary=True)

        # Fetch data from the projects table
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()

        # Fetch members for each project
        cursor.execute("SELECT * FROM members")
        members = cursor.fetchall()

        # Group members by group_number
        grouped_members = {}
        for member in members:
            group = member.get('group_number')
            if group not in grouped_members:
                grouped_members[group] = []
            grouped_members[group].append(member)

        return render_template('data_table.html', projects=projects, grouped_members=grouped_members)
    except Error as e:
        app.logger.error(f"Error fetching project data: {e}")
        return render_template('error.html', error_message="An error occurred while fetching project data."),url_for('logout')
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

'''Next Topic: Insert data or edit data --> Day_35.py'''