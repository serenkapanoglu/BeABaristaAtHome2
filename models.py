
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime




bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User table"""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    first_name = db.Column(
        db.Text,
        nullable=False,
    )

    last_name = db.Column(
        db.Text,
        nullable=False,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable = False,
    )

    @classmethod
    def register(cls, username, password, first_name, last_name):
       

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
        )
        db.session.add(user)
        return user
   
    @classmethod
    def authenticate(cls, username, password):
        

        user = User.query.filter_by(username = username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

    


class Cocktail(db.Model):

    __tablename__ = "cocktails"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Cocktail {self.name}>"

  
    
    
    
class Comment(db.Model):
    __tablename__="comments"
    
    id=db.Column(db.Integer, primary_key=True)
    text=db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='comments')
    cocktail_id=db.Column(db.Integer, nullable=False)
    

class Favorite(db.Model):

    __tablename__ = 'favorites'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete= "cascade"),
    )

    cocktail_id = db.Column(
        db.Integer
    )






    
    



def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
