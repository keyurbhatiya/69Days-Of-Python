Here’s a **10-day roadmap** to create a Flask blog website with features like posts, likes, comments, follows, shares, and AI-based hashtag suggestions:  

---

### **Day 1: Setup and Project Initialization**  
1. Install necessary tools and libraries:
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-wtf nltk scikit-learn
   ```
2. Create the project folder structure:
   ```
   flask_blog/
   ├── static/           # For CSS, JS, images
   ├── templates/        # HTML templates
   ├── app.py            # Main application
   ├── models.py         # Database models
   ├── forms.py          # WTForms for handling forms
   ├── utils.py          # AI-based hashtag suggestion
   ├── config.py         # Configuration for the app
   ├── migrations/       # Database migrations
   └── requirements.txt  # Dependencies
   ```
3. Initialize a basic Flask app with SQLAlchemy integration.  
   ```python
   # app.py
   from flask import Flask
   from flask_sqlalchemy import SQLAlchemy

   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
   app.config['SECRET_KEY'] = 'your_secret_key'
   db = SQLAlchemy(app)

   if __name__ == "__main__":
       app.run(debug=True)
   ```

---

### **Day 2: Database Models**  
1. Define models in `models.py` for `User`, `Post`, `Comment`, `Like`, and `Follow`.  
2. Example `Post` model:  
   ```python
   from app import db

   class Post(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       title = db.Column(db.String(100), nullable=False)
       content = db.Column(db.Text, nullable=False)
       author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
       created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
   ```
3. Run migrations:  
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

---

### **Day 3: User Authentication**  
1. Add Flask-Login for authentication:
   ```bash
   pip install flask-login
   ```
2. Update `models.py` with a `User` model and add login functionality:
   ```python
   from flask_login import UserMixin

   class User(db.Model, UserMixin):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(50), unique=True, nullable=False)
       password = db.Column(db.String(200), nullable=False)
   ```
3. Add login and registration forms in `forms.py` using Flask-WTF.  

---

### **Day 4: CRUD for Posts**  
1. Create views for adding, editing, deleting, and viewing blog posts.  
2. Add templates for:
   - Post creation (`create_post.html`)
   - Post editing (`edit_post.html`)
   - Post listing (`index.html`)  

---

### **Day 5: Comments & Likes**  
1. Add a `Comment` model:
   ```python
   class Comment(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
       user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
       content = db.Column(db.Text, nullable=False)
   ```
2. Create routes for adding and displaying comments.  
3. Add functionality to like posts using a `Like` model.

---

### **Day 6: Followers and Social Features**  
1. Implement a `Follow` model:
   ```python
   class Follow(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
       followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   ```
2. Add follow/unfollow buttons to user profiles.  
3. Show the follower/following count on the user’s dashboard.  

---

### **Day 7: AI Hashtag Suggestion**  
1. Use **NLTK** or **Scikit-Learn** for AI-based hashtag suggestions in `utils.py`.  
2. Example implementation:  
   ```python
   import nltk
   from sklearn.feature_extraction.text import CountVectorizer

   def suggest_hashtags(content):
       words = nltk.word_tokenize(content)
       hashtags = [f"#{word.lower()}" for word in words if len(word) > 4]
       return hashtags[:5]
   ```
3. Integrate this feature when creating or editing a post.  

---

### **Day 8: Sharing and Social Media Integration**  
1. Add a "Share" button with links to platforms like Facebook, Twitter, and LinkedIn.  
2. Example share link:
   ```html
   <a href="https://twitter.com/intent/tweet?text={{ post.title }}&url={{ request.url }}" target="_blank">Share on Twitter</a>
   ```

---

### **Day 9: Styling with Bootstrap**  
1. Integrate **Bootstrap 5** for styling.  
2. Add responsive layouts for:
   - Navbar
   - Post cards
   - User dashboard  

---

### **Day 10: Testing and Deployment**  
1. Test all features thoroughly:
   - Registration/Login
   - Post creation/editing/deletion
   - Comments, likes, and follows  
2. Deploy using **Heroku** or **Render**:  
   - Create a `Procfile`:
     ```
     web: gunicorn app:app
     ```
   - Push your code to a GitHub repository.
   - Deploy on Heroku with:
     ```bash
     heroku create
     git push heroku main
     ```

---

This roadmap ensures you have a fully functional blog website with the requested features in 10 days! Let me know if you'd like code samples for any specific part.