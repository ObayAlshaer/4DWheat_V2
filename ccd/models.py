'''
MODELS

NOTES:
To create and commit changes, uncomment the last two lines.

Here is a link to the sqlalchemy page that goes through how to
make models http://flask-sqlalchemy.pocoo.org/2.3/models/
That link also cover many to many relationships, and one to 
many relationships.
'''

# Imports -----------------------------------------------------------------------


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Setup -------------------------------------------------------------------------

app = Flask(__name__) # create the application instance
app.config.from_object('config') # load configurations from config.py
db = SQLAlchemy(app) # use SQLAlchemy to build the app's db

# Models ------------------------------------------------------------------------



'''
This model is for the budget. 

It is used in all the budget views and html files.

The BudgetAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the email field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Budget(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        year1 = db.Column(db.Integer)
        year2 = db.Column(db.Integer)
        category = db.Column(db.String(100))
        assigned_to = db.Column(db.String(100))
        comments = db.Column(db.String(1000))
        subcategory = db.Column(db.String(100))
        cost_type = db.Column(db.String(100))
        centre = db.Column(db.String(100))
        orig_proposal = db.Column(db.Integer)

        def __repr__(self):
                return '<Budget %r>' % self.budget


'''
This model is for th collaborators table

It is used in all the collab views and html files.

The CollabAddForm in the forms.py file is the form
that is used to collect the data to file this table.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the email field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;


'''

class Collaborators(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        name1 = db.Column(db.String(100))
        name2 = db.Column(db.String(100))
        title = db.Column(db.String(100))
        role_expertise = db.Column(db.String(1000))
        country = db.Column(db.String(100))
        type = db.Column(db.String(100))
        affiliation = db.Column(db.String(1000))
        email = db.Column(db.String(100))

        def __repr__(self):
                return '<Colaborators %r>' % self.colaborators


class ROC_members(db.Model):

        id = db.Column(db.String(100))
        name = db.Column(db.String(100))
        title = db.Column(db.String(100))
        affiliation = db.Column(db.String(1000))
        email = db.Column(db.String(100), primary_key=True)
        web_link = db.Column(db.String(1000))
        def __repr__(self):
                return '<ROC_members %r>' % self.roc_members



class Research_Team(db.Model):
        id = db.Column(db.String(45))
        name = db.Column(db.String(100),primary_key=True)
        title = db.Column(db.String(100))
        role = db.Column(db.String(100))
        description_of_responsibilities = db.Column(db.String(1000))
        affiliation = db.Column(db.String(1000))
        email = db.Column(db.String(100))
        website = db.Column(db.String(1000))
        def __repr__(self):
                return '<Research_Team %r>' % self.research_team
'''
This model is for the conferences table. 

It is used in all the conferences views and html files.

The ConferenceAddForm in the forms.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the attendees field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Conferences(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(1000))
        date = db.Column(db.String(100))
        location = db.Column(db.String(100))
        attendees = db.Column(db.String(1000))

        def __repr__(self):
                return '<Conferences %r>' % self.conferences


'''
This model is for the Cost_Categories table. 

It is used in all the Cost_Categories views and html files.

The CostCategoryAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the description field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Cost_Categories(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        code = db.Column(db.Integer)
        description = db.Column(db.String(100))

        def __repr__(self):
                return '<Cost_Categories %r>' % self.cost_categories


'''
This model is for the Cost_Subcategories table. 

It is used in all the cost_subcategory views and html files.

The CostSubcategoryAddForm in the forms.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the description field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Cost_Subcategories(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(100))

        def __repr__(self):
                return '<Cost_Subcategories %r>' % self.cost_subcategories


'''
This model is for the Links table. 

It is used in all the links views and html files.

The LinkAddForm in the forms.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the link field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Links(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        category = db.Column(db.String(100))
        subcategory = db.Column(db.String(100))
        software = db.Column(db.String(100))
        description = db.Column(db.String(1000))
        link = db.Column(db.String(1000))

        def __repr__(self):
                return '<Links %r>' % self.links

'''
This model is for the milestones table. 

It is used in all the milestone views and html files.

The MilestoneAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.
The edit view is a bit different than the add view for this one
so it is a good idea to check it out.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the variance field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Milestones(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        milestone_id = db.Column(db.Integer,unique=True)
        short_title = db.Column(db.String(100))
        start_date = db.Column(db.Date) # Changed these two from strings
        end_date = db.Column(db.Date)   # to Dates Kody 2018-01-08
        module = db.Column(db.String(100))
        activity = db.Column(db.String(1000))
        milestone = db.Column(db.String(1000))
        assigned_to = db.Column(db.String(1000))
        progress = db.Column(db.String(1000))
        variance = db.Column(db.String(1000))

        def __repr__(self):
                return '<Milestones %r>' % self.milestones


'''
This model is for the News table. 

It is used in all the news views and html files.

The NewsAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the entry field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class News(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        date = db.Column(db.DateTime, default=datetime.now())
        entry = db.Column(db.String(1000))

        def __repr__(self):
                return '<News %r>' % self.news


'''
This model is for the objectives table. 

It is used in all the objectives views and html files.

The ObjectiveAddForm in the forms.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the outcome field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Objectives(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        order = db.Column(db.Integer, unique=True)
        short = db.Column(db.String(100))
        description = db.Column(db.String(1000))
        outcome = db.Column(db.String(1000))

        def __repr__(self):
                return '<Objectives %r>' % self.objectives

'''
This model is for the participants table. 

It is used in all the participant views and html files.

The ParticipantAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the contribution_percent field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Participants(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        site = db.Column(db.String(100))
        name_id = db.Column(db.String(1000))
        cost_centre = db.Column(db.String(100))
        from_participant = db.Column(db.String(1))
        name1 = db.Column(db.String(100))
        name2 = db.Column(db.String(100))
        pi = db.Column(db.String(1))
        role = db.Column(db.String(100))
        responsibility = db.Column(db.String(1000))
        initials = db.Column(db.String(10))
        publishing_initials = db.Column(db.String(10))
        email = db.Column(db.String(100))
        contribution_percent = db.Column(db.Integer)

        def __repr__(self):
                return '<Participants %r>' % self.participants



'''
This model is for the Publications table. 

It is used in all the publications views and html files.

The PublicationAddForm in the forms.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the link field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Publications(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        year = db.Column(db.String(100))
        title = db.Column(db.String(1000))
        citation = db.Column(db.String(1000))
        link = db.Column(db.String(1000))

        def __repr__(self):
                return '<Publications %r>' % self.publications



'''
This model is for the RDC table. 

It is used in all the rdc views and html files.

The RdcAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the adrdt field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class RDC(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        centre = db.Column(db.String(100))
        director = db.Column(db.String(100))
        adrdt = db.Column(db.String(100))

        def __repr__(self):
                return '<RDC %r>' % self.rdc

'''
database for user account information table(UserAccount).
'''
class UserAccount(db.Model):
        email = db.Column(db.String(100), primary_key=True)
        username = db.Column(db.String(100))
        password = db.Column(db.String(100))
        

        def __repr__(self):
                return '<UserAccount %r>' % self.UserAccount


'''
This model is for the support table. 

It is used in all the support views and html files.

The SupportAddForm in the form.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the email field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Support(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        name_id = db.Column(db.String(1000))
        name1 = db.Column(db.String(100))
        name2 = db.Column(db.String(100))
        site = db.Column(db.String(100))
        team = db.Column(db.String(100))
        role = db.Column(db.String(100))
        responsibility = db.Column(db.String(1000))
        contribution_percent = db.Column(db.Integer)
        email = db.Column(db.String(100))

        def __repr__(self):
                return '<Participants %r>' % self.participants


'''
This model is for the Tools table. 

It is used in all the tool views and html files.

The ToolAddForm in the forms.py file is the form that
is used to collect info to put into a table made from this model.

Keep in mind that if you plan on using a textfile to populate this
table in mysql terminal that this model will make it so that
the primary_key is the first thing read in. This will mess up the 
operation. To fix this move the 'id' (primary_key) after the link field. 

The command you need to use is the one below but with the proper column and field.
ALTER TABLE table_name MODIFY COLUMN id  INTEGER NOT NULL AUTO_INCREMENT AFTER current_last_field;
'''
class Tools(db.Model):

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100))
        category = db.Column(db.String(100))
        description = db.Column(db.String(1000))
        link = db.Column(db.String(1000))

        def __repr__(self):
                return '<Tools %r>' % self.tools

'''
db.create_all()
db.session.commit()
'''
