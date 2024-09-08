from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


# class represents a registration form for a user to create an account
class Registration(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=6, max=100)])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=100)])
	confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Register")

	# check if user already exists
	def validate_username(self, username):
		# query database for first instance of username
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('This username already exists.')

	# check if email already exists
	def validate_email(self, email):
		# query database for first instance of email
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('This email is already in use.')


# class represents a login form for a user to create an account
class Login(FlaskForm):
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=100)])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")


# class represents a form for updating user information
class UpdateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    pic = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # function makes sure that the new username is not already taken. 
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    # function makes sure that the new email is not already taken. 
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


# class represents the form for making a post on the website
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
