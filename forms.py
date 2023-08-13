from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class UserAddForm(FlaskForm):
    """Form for adding users."""
    first_name = StringField('First name', validators=[DataRequired()] )
    last_name = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6), DataRequired()])

class SearchForm(FlaskForm):
    search = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Length(min=6, max=100), DataRequired()])
    submit = SubmitField('Submit')