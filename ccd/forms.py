'''
Forms
'''

# Imports ---------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField,BooleanField, widgets
from wtforms.validators import DataRequired, ValidationError, InputRequired,Email,Length,EqualTo
from wtforms import validators
from models import *
from wtforms.fields import simple, core

# Setup -----------------------------------------------------------------------

USERNAME = 'admin'
PASSWORD = '4dwheatdb'

DATA_ARCHIVE_USERNAME = 'admin'
DATA_ARCHIVE_PASSWORD = '4dwheat!'

# Forms -----------------------------------------------------------------------

class BudgetAddForm(FlaskForm):
  year1 = StringField("Year 1")
  year2 = StringField("Year 2")
  category = StringField("Category")
  assigned_to = StringField("Assigned To")
  comments = TextAreaField("Comments")
  subcategory = StringField("Subcategory")
  cost_type = StringField("Cost Type")
  centre = StringField("Centre")
  orig_proposal = StringField("Original Proposal")
  submit = SubmitField("Save")


class CollabAddForm(FlaskForm):
  name1 = StringField("First Name")
  name2 = StringField("Last Name")
  title = StringField("Title")
  role_expertise = TextAreaField("Role Expertise")
  country = StringField("Country")
  type = StringField("Type")
  affiliation = StringField("Affiliation")
  email = StringField("Email")
  submit = SubmitField("Save")

class ROC_memberAddForm(FlaskForm):
  id = StringField("Id")
  name = StringField("Name")
  
  title = StringField("Title")
  affiliation = StringField("Affiliation")
  email = StringField("Email")
  web_link = StringField("Web Link")
  submit = SubmitField("Save")

class Research_TeamAddForm(FlaskForm):
  id = StringField("Id")
  name = StringField("Name")
  
  title = StringField("Title")
  role = StringField("Role")
  description_of_responsibilities = StringField("Description of Responsibilities")
  affiliation = StringField("Affiliation")
  email = StringField("Email")
  website = StringField("WebSite")
  submit = SubmitField("Save")

class ConferenceAddForm(FlaskForm):
  title = StringField("Title")
  date = StringField("Date")
  location = StringField("Location")
  attendees = StringField("Attendees")
  submit = SubmitField("Save")


class CostCategoryAddForm(FlaskForm):
  code = StringField("Code")
  description = StringField("Description")
  submit = SubmitField("Save")


class CostSubcategoryAddForm(FlaskForm):
  description = StringField("Description")
  submit = SubmitField("Save")


class LinkAddForm(FlaskForm):
  category = StringField("Category")
  subcategory = StringField("Subcategory")
  software = StringField("Software")
  description = StringField("Description")
  link = StringField("Link")
  submit = SubmitField("Save")

class DataArchiveLoginForm(FlaskForm):
  #change login title
    username = StringField("Data Archive Username", validators=[DataRequired()])

    password = PasswordField("Data Archive Password", validators=[DataRequired()])
    
    submit = SubmitField("Login")
    cancel = SubmitField("Cancel")
    #the name after validate_ should equal to field variable above!
    def validate_username(self, field):
        if field.data != DATA_ARCHIVE_USERNAME:
            raise ValidationError("Invalid username")

    def validate_password(self, field):
        if field.data != DATA_ARCHIVE_PASSWORD:
            raise ValidationError("Invalid password")


class LoginForm(FlaskForm):
  #change login title
    username = StringField("Username")

    password = PasswordField("Password")
    
    submit = SubmitField("Login")
    cancel = SubmitField("Cancel")
    def validate_username(self, field):
        if field.data != USERNAME:
            raise ValidationError("Invalid username")

    def validate_password(self, field):
        if field.data != PASSWORD:
            raise ValidationError("Invalid password")

class SignUpForm(FlaskForm):

  
  #change login title
    email = StringField("Email", validators=[InputRequired()])
    
    username = StringField("username", validators=[InputRequired(), Length(min=5, max=20, message='user name should have more than 4\
       characters')], id="username")
    
    password = simple.PasswordField("Password", validators=[InputRequired(), Length(min=5, max=20, message='password should have more than 4 \
      characters'), EqualTo('ReEnterPassword', message="Passwords don't match")], id="password", widget = widgets.PasswordInput(), render_kw= {'class': 'form-control'})
    
    ReEnterPassword = simple.PasswordField("Re-enter Password", validators=[validators.DataRequired(message='please enter password'),\
    validators.EqualTo('password', message='please enter the same password')], widget = widgets.PasswordInput(), render_kw= {'class': 'form-control'})
    
    
    submit = SubmitField("Summit")

    def validate_email(self, field):
        if UserAccount.query.filter_by(email=field.data).first():
            raise ValidationError('email is already exist')


    def validate_username(self, field):
        if UserAccount.query.filter_by(username=field.data).first():
            raise ValidationError('username is already exist')

    def validate_reenter_password(self, password, ReEnterPassword):
        if password.data != ReEnterPassword.data:
            raise ValidationError("the passwords you entered must be the same")

    

class MilestoneAddForm(FlaskForm):
  milestone_id = StringField("Milestone ID")
  short_title = StringField("Short Title")
  start_date = StringField("Start Date")
  end_date = StringField("End Date")
  module = StringField("Module")
  activity = TextAreaField("Activity")
  milestone = TextAreaField("Milestone")
  assigned_to = StringField("Assigned To")
  progress = TextAreaField("Progress")
  variance = TextAreaField("Variance")
  submit = SubmitField("Save")


class NewsAddForm(FlaskForm):
  entry = TextAreaField("News Entry")
  submit = SubmitField("Save")


class ObjectiveAddForm(FlaskForm):
  order = StringField("Order")
  short = StringField("Short")
  description = TextAreaField("Description")
  outcome = TextAreaField("Outcome")
  submit = SubmitField("Save")

class ParticipantAddForm(FlaskForm):
  site = StringField("Site")
  name_id = StringField("Name ID (Last,First)")
  name1 = StringField("First Name")
  name2 = StringField("Last Name")
  cost_centre = StringField("Cost Centre")
  from_participant = StringField("From Participant")
  pi = StringField("PI")
  role = StringField("Role")
  responsibility = TextAreaField("Responsibility")
  initials = StringField("Initials")
  publishing_initials = StringField("Publishing Initials")
  email = StringField("Email")
  contribution_percent = StringField("Contribution Percent")
  submit = SubmitField("Save")


class PublicationAddForm(FlaskForm):
  year = StringField("Year")
  title = TextAreaField("Title")
  citation = TextAreaField("Citation")
  link = StringField("Link (http://...)")
  submit = SubmitField("Save")


class RdcAddForm(FlaskForm):
  centre = StringField("Centre")
  director = StringField("Director")
  adrdt = StringField("ADRDT")
  submit = SubmitField("Save")



class SupportAddForm(FlaskForm):
  name_id = StringField("Name ID (Last,First)")
  name1 = StringField("First Name")
  name2 = StringField("Last Name")
  site = StringField("Site")
  team = StringField("Team")
  role = StringField("Role")
  responsibility = StringField("Responsibility")
  contribution_percent = StringField("Contribution Percent")
  email = StringField("Email")
  submit = SubmitField("Save")


class ToolAddForm(FlaskForm):
  title = StringField("Title")
  category = StringField("Category")
  description = TextAreaField("Description")
  link = StringField("Link (http://...)")
  submit = SubmitField("Save")

