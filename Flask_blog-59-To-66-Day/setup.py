from flaskblog import app, db  # Ensure you import your app and db instance

with app.app_context():  # Create an application context
    db.create_all()      # Create all tables in the database
    print("Database tables created successfully!")
