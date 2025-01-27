from flaskblog import db, app
# from flaskblog.models import db, app 

# Wrap the database creation in the application context
with app.app_context():
    db.create_all()
    print("Database created successfully!")
