import jsonapi as jsonapi
from flask import url_for
from flask_login import current_user, login_user

from app import app, render_template, flash, redirect
from app.data_models.bounty_models import User, BountySubmission
from app.data_models.forms import LoginForm
from app.utils import *



# App Globals
bounties: [Bounty] = []
b_themes: [str] = []
b_theming: {}


@app.route('/')
def home():  # put application's code here
    global bounties, b_themes, b_theming
    if len(bounties) == 0:
        bounties = get_bounties()
        b_themes = get_themes(bounties)
        b_theming = get_bounty_theming()
    return render_template("bounties.html", bounties=bounties, bounty_themes=b_themes,
                           bounty_theming=b_theming)


@app.route('/login', methods=['GET', 'POST'])
def login():
    flash("Test")
    if current_user.is_authenticated:
        return redirect(url_for('user_dashboard'))
    form = LoginForm()
    flash("Login Attempt")
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid User or Pass')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("user_dashboard"))
    return render_template("login.html", form=form, title="Login")

@app.route('/user_login')
def logout():
    pass

@app.route('/dashboard')
def user_dashboard():
    return render_template("dashboard.html", title="Dashboard")

if __name__ == '__main__':
    app.run(debug=True)
