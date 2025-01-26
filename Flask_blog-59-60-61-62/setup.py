from flaskblog import db, app  # Import db and app from your Flask app

# Wrap the database creation in the application context
with app.app_context():
    db.create_all()
    print("Database created successfully!")
