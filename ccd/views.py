'''
Views
'''

# Imports ---------------------------------------------------------------------
import re, os
from flask import request, session, redirect, url_for, render_template, flash, send_file
from sqlalchemy.sql import text
from forms import *
from models import *

# Home ------------------------------------------------------------------------

@app.route('/',methods=['GET','POST'])
def main():
   #news = News.query.order_by("id desc")
   news = News.query.order_by(text('id desc'))
   return render_template('home_slideshow.html',news=news)

@app.route('/news_add',methods=['GET','POST'])
def news_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = NewsAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = News()
        form.populate_obj(new)
        # Check if the news already exists in the db
        exists = News.query.filter_by(entry=new.entry).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('main'))
    return render_template('news_add.html',form=form)

@app.route('/news_delete',methods=['GET','POST'])
def news_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    news = News.query.order_by("entry desc")
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = News.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('main'))
    return render_template('news_delete.html',news=news)


def validate_signup(email,username,password1,password2):
      user = UserAccount.query.filter(UserAccount.email == email).first()
      email_format = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
      if password2:
        if user:
          
          return 'user already exists'
        else:
          if len(username) < 5:
            
            return 'user name should have more than 4 characters'

          elif not (re.match(email_format,email)):
            return 'email format should be correct'

          elif password1 != password2:
            
            return 'passwords should be the same'
          
          elif len(password1) < 5:
            return 'password should have more than 4 characters'
          
          else:
            return 'success!'

      else:
        return 'please fill out re-enetr password'


@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
   form = SignUpForm()
   if request.method == 'POST':
      
      email = request.form.get('email')
      username = request.form.get('username')
      password1 = request.form.get('password')
      password2 = request.form.get('ReEnterPassword')

      message = validate_signup(email, username, password1, password2)
      flash(message)


      if form.validate_on_submit():
        new = UserAccount()
        form.populate_obj(new)
        
        flash(message)
        # Check if the member already exists in the db
        exists = UserAccount.query.filter_by(email=new.email).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return render_template('sign_up_success.html')
   return render_template('sign_up.html',form=form)

@app.route('/roc_add',methods=['GET','POST'])
def roc_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = ROC_memberAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = ROC_members()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = ROC_members.query.filter_by(email=new.email).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('roc_member'))
    return render_template('roc_add.html',form=form)

# Login / Logout ---------------------------------------------------------------

@app.route('/login',methods=['GET','POST'])
@app.route('/login/<condition>',methods=['GET','POST'])
def login(condition = 10000):
   form = LoginForm()
   if request.method == 'POST':
        if form.cancel.data:  # if cancel button is clicked
            return redirect(url_for('main'))
   if form.validate_on_submit():
      session['logged_in'] = True
      return redirect(url_for('main'))
   return render_template('login.html',form=form)

@app.route('/Data_Archive_Login',methods=['GET','POST'])
def data_archive_login():
   form = DataArchiveLoginForm()
   if request.method == 'POST':
        if form.cancel.data:  # if cancel button is clicked
            return redirect(url_for('data_archive'))

   if form.validate_on_submit():
      session['Data_Archive_logged_in'] = True
      return redirect(url_for('data_archive_portal'))
   
      
   return render_template('data_archive_login.html',form=form)

@app.route('/logout')
def logout():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    session.pop('logged_in', None)
    return redirect(url_for('main'))

# RDC ------------------------------------------------------------------------

@app.route('/rdc',methods=['GET','POST'])
def rdc():
   rdcs = RDC.query.all()
   return render_template('rdc.html',rdcs=rdcs)

@app.route('/rdc_add',methods=['GET','POST'])
def rdc_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = RdcAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = RDC()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = RDC.query.filter_by(centre=new.centre).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('rdc'))
    return render_template('rdc_add.html',form=form)


@app.route('/rdc_delete',methods=['GET','POST'])
def rdc_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    rdcs = RDC.query.order_by("centre asc")
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = RDC.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
           db.session.delete(exists)
           db.session.commit()        
           return redirect(url_for('rdc'))
    return render_template('rdc_delete.html',rdcs=rdcs)

# Budget --------------------------------------------------------------------

@app.route('/budget',methods=['GET','POST'])
def budget():
   budget = Budget.query.all()
   return render_template('budget.html',budget=budget)

@app.route('/budget_add',methods=['GET','POST'])
def budget_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = BudgetAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Budget()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Budget.query.filter_by(comments=new.comments).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('budget'))
    return render_template('budget_add.html',form=form)

@app.route('/budget_delete',methods=['GET','POST'])
def budget_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    budget = Budget.query.order_by("comments asc")
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Budget.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('budget'))
    return render_template('budget_delete.html',budget=budget)

# Cost Categories ------------------------------------------------------------

@app.route('/cost_categories',methods=['GET','POST'])
def cost_categories():
   
   cost_categories = Cost_Categories.query.all()
   return render_template('cost_categories.html',cost_categories=cost_categories)

@app.route('/cost_category_add',methods=['GET','POST'])
def cost_category_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = CostCategoryAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Cost_Categories()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Cost_Categories.query.filter_by(description=new.description).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('cost_categories'))
    return render_template('cost_category_add.html',form=form)

@app.route('/cost_category_delete',methods=['GET','POST'])
def cost_category_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    cost_categories = Cost_Categories.query.order_by("description asc")
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Cost_Categories.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('cost_categories'))
    return render_template('cost_category_delete.html',cost_categories=cost_categories)

# Cost Subcategories ---------------------------------------------------------
@app.route('/cost_subcategories',methods=['GET','POST'])
def cost_subcategories():
   cost_subcategories = Cost_Subcategories.query.all()
   return render_template('cost_subcategories.html',cost_subcategories=cost_subcategories)

@app.route('/cost_subcategory_add',methods=['GET','POST'])
def cost_subcategory_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = CostSubcategoryAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Cost_Subcategories()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Cost_Subcategories.query.filter_by(description=new.description).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('cost_subcategories'))
    return render_template('cost_subcategory_add.html',form=form)

@app.route('/cost_subcategory_delete',methods=['GET','POST'])
def cost_subcategory_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    cost_subcategories = Cost_Subcategories.query.order_by("description asc")
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Cost_Subcategories.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('cost_subcategories'))
    return render_template('cost_subcategory_delete.html',cost_subcategories=cost_subcategories)

# Activities ------------------------------------------------------------------   
@app.route('/data_archive_portal',methods=['GET','POST'])
def data_archive_portal():
   return render_template('data_archive_portal.html')


# Activities ------------------------------------------------------------------
@app.route('/Progress',methods=['GET','POST'])
def Progress():
   
   return render_template('Progress.html')


@app.route('/activity_overview', methods=['GET', 'POST'])
def activity_overview():
    return render_template('activity_overview.html')


@app.route('/activity1',methods=['GET','POST'])
def activity1():
   
   return render_template('activity1.html')

@app.route('/activity2',methods=['GET','POST'])
def activity2():
   
   return render_template('activity2.html')

@app.route('/activity3',methods=['GET','POST'])
def activity3():
   
   return render_template('activity3.html')

@app.route('/activity4',methods=['GET','POST'])
def activity4():
   
   return render_template('activity4.html')

@app.route('/activity5',methods=['GET','POST'])
def activity5():
   
   return render_template('activity5.html')
   
# Milestones ------------------------------------------------------------------

@app.route('/milestones',methods=['GET','POST'])
def milestones():
   milestones = Milestones.query.all()
   return render_template('milestones.html',milestones=milestones)

@app.route('/milestone_add',methods=['GET','POST'])
def milestone_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = MilestoneAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Milestones()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Milestones.query.filter_by(milestone_id=new.milestone_id).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('milestones'))
    return render_template('milestone_add.html',form=form)


@app.route('/milestone_delete',methods=['GET','POST'])
def milestone_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    milestones = Milestones.query.order_by("milestone_id asc")
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Milestones.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('milestones'))
    return render_template('milestone_delete.html',milestones=milestones)


@app.route('/milestone_edit',methods=['GET','POST'])
def milestone_edit():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    milestones = Milestones.query.order_by("milestone_id asc")
    form = MilestoneAddForm()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        editID = request.form['editID']
        # Find the entry using the ID as a key
        exists = Milestones.query.filter_by(id=editID).first()
        # Populate the form with info from the entry
        form = MilestoneAddForm(obj=exists)
        if form.validate_on_submit():
          # Keep all info the same except for progress
          milestone_id = request.form.get('milestone_id')
          form.milestone_id.data = exists.milestone_id
          short_title = request.form.get('short_title')
          form.short_title.data = exists.short_title
          start_date = request.form.get('start_date')
          form.start_date.data = exists.start_date
          end_date = request.form.get('end_date')
          form.end_date.data = exists.end_date
          module = request.form.get('module')
          form.module.data = exists.module
          activity = request.form.get('activity')
          form.activity.data = exists.activity
          milestone = request.form.get('milestone')
          form.milestone.data = exists.milestone
          assigned_to = request.form.get('assigned_to')
          form.assigned_to.data = exists.assigned_to

          form.populate_obj(exists)
          db.session.add(exists)
          db.session.commit()
          return redirect(url_for('milestones'))
    return render_template('milestone_edit.html',milestones=milestones,form=form)

# Objectives ------------------------------------------------------------------

@app.route('/objectives',methods=['GET','POST'])
def objectives():
   objectives = Objectives.query.all()
   return render_template('objectives.html',objectives=objectives)

@app.route('/objective_add',methods=['GET','POST'])
def objective_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = ObjectiveAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Objectives()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Objectives.query.filter_by(order=new.order).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('objectives'))
    return render_template('objective_add.html',form=form)

@app.route('/objective_delete',methods=['GET','POST'])
def objective_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    objectives = Objectives.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Objectives.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('objectives'))
    return render_template('objective_delete.html',objectives=objectives)


# Collab ----------------------------------------------------------------------

@app.route('/collab',methods=['GET','POST'])
def collab():
   collabs = Collaborators.query.all()
   return render_template('collab.html',collabs=collabs)

@app.route('/roc_member',methods=['GET','POST']) 
def roc_member():
   roc_mem = ROC_members.query.all()
   return render_template('roc_member.html',roc_mem=roc_mem)

@app.route('/management_team',methods=['GET','POST'])
def management_team():
   
   return render_template('management_team.html')

@app.route('/research_team',methods=['GET','POST'])
def research_team():
   research = Research_Team.query.all()
   return render_template('research_team.html',research=research)

@app.route('/collab_add',methods=['GET','POST'])
def collab_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = CollabAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Collaborators()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Collaborators.query.filter_by(email=new.email).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('collab'))
    return render_template('collab_add.html',form=form)



@app.route('/research_team_add',methods=['GET','POST'])
def research_team_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = Research_TeamAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Research_Team()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Research_Team.query.filter_by(name=new.name).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('research_team'))
    return render_template('research_team_add.html',form=form)

@app.route('/roc_delete',methods=['GET','POST'])
def roc_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    roc_member = ROC_members.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = ROC_members.query.filter_by(name=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('roc_member'))
    return render_template('roc_delete.html',roc_member=roc_member)

@app.route('/research_team_delete',methods=['GET','POST'])
def research_team_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    research_team = Research_Team.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Research_Team.query.filter_by(name=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('research_team'))
    return render_template('research_team_delete.html',research_team=research_team)

@app.route('/collab_delete',methods=['GET','POST'])
def collab_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    collabs = Collaborators.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Collaborators.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('collab'))
    return render_template('collab_delete.html',collabs=collabs)

# Participants ----------------------------------------------------------------

@app.route('/participants',methods=['GET','POST'])
def participants():
   participants = Participants.query.all()
   return render_template('participants.html',participants=participants)

@app.route('/participant_add',methods=['GET','POST'])
def participant_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = ParticipantAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Participants()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Participants.query.filter_by(name_id=new.name_id).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('participants'))
    return render_template('participant_add.html',form=form)

@app.route('/participant_delete',methods=['GET','POST'])
def participant_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    participants = Participants.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Participants.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('participants'))
    return render_template('participant_delete.html',participants=participants)


# Support ---------------------------------------------------------------------

@app.route('/support',methods=['GET','POST'])
def support():
   supports = Support.query.all()
   return render_template('support.html',supports=supports)

@app.route('/support_add',methods=['GET','POST'])
def support_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = SupportAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Support()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Support.query.filter_by(name_id=new.name_id).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('support'))
    return render_template('support_add.html',form=form)


@app.route('/support_delete',methods=['GET','POST'])
def support_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    supports = Support.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Support.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('support'))
    return render_template('support_delete.html',supports=supports)

# Publications ----------------------------------------------------------------

@app.route('/publications',methods=['GET','POST'])
def publications():
    publications = Publications.query.all()
    return render_template('publications.html',publications=publications)

@app.route('/publication_add',methods=['GET','POST'])
def publication_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = PublicationAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Publications()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Publications.query.filter_by(title=new.title).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('publications'))
    return render_template('publication_add.html',form=form)

@app.route('/publication_delete',methods=['GET','POST'])
def publication_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    publications = Publications.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Publications.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('publications'))
    return render_template('publication_delete.html',publications=publications)

# Tools -----------------------------------------------------------------------

@app.route('/tools',methods=['GET','POST'])
def tools():
   tools = Tools.query.all()
   return render_template('tools.html',tools=tools)

@app.route('/tool_add',methods=['GET','POST'])
def tool_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = ToolAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Tools()
        form.populate_obj(new)
        # Check if the member already exists in the db
        exists = Tools.query.filter_by(title=new.title).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('tools'))
    return render_template('tool_add.html',form=form)

@app.route('/tool_delete',methods=['GET','POST'])
def tool_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    tools = Tools.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Tools.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('tools'))
    return render_template('tool_delete.html',tools=tools)

# Links ----------------------------------------------------------------------

@app.route('/links',methods=['GET','POST'])
def links():
   links = Links.query.all()
   return render_template('links.html',links=links)

@app.route('/link_add',methods=['GET','POST'])
def link_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = LinkAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Links()
        form.populate_obj(new)
        # Check if the link already exists in the db
        exists = Links.query.filter_by(software=new.software).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('links'))
    return render_template('link_add.html',form=form)

@app.route('/link_delete',methods=['GET','POST'])
def link_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    links = Links.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Links.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('links'))
    return render_template('link_delete.html',links=links)

# presentation -----------------------------------------------------------------

@app.route('/presentations',methods=['GET','POST'])
def Presentations():
   conferences = Conferences.query.all()
   return render_template('presentations.html',conferences=conferences)

@app.route('/presentations_add',methods=['GET','POST'])
def Presentations_add():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    form = ConferenceAddForm()
    if request.method == 'POST':
      if form.validate_on_submit():
        new = Conferences()
        form.populate_obj(new)
        # Check if the entry already exists in the db
        exists = Conferences.query.filter_by(title=new.title).first()
        # If it does not exist, add it to the db
        if exists is None:
          db.session.add(new)
          db.session.commit()
          return redirect(url_for('Presentations'))
    return render_template('presentations_add.html',form=form)

@app.route('/presentations_delete',methods=['GET','POST'])
def Presentations_delete():
    if not session.get('logged_in') :
      return redirect(url_for('login')) #user is not logged in sends user to login screen Kody 2018-01-08
    conferences = Conferences.query.all()
    # Retrieve user input from dropdown
    if request.method == 'POST':
        deleteID = request.form['deleteID']
        # Find the entry using the ID as a key
        exists = Conferences.query.filter_by(id=deleteID).first()
        # If the entry exists, delete it
        if exists:
            db.session.delete(exists)
            db.session.commit()
            return redirect(url_for('Presentations'))
    return render_template('presentations_delete.html',conferences=conferences)

# Data Archive --------------------------------------------------------------

@app.route('/data_archive',methods=['GET','POST'])
def data_archive():
   return render_template('data_archive.html')

@app.route('/data_archive_353_panel',methods=['GET','POST'])
def data_archive_353_panel():
   return render_template('data_archive_353_panel.html')

@app.route('/download_file/<path:filename>', methods=['GET','POST'])
def download_file(filename):
    print app.root_path;
    return send_file(filename, as_attachment=True)