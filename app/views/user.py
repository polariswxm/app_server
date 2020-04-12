from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import RegisterForm, LoginForm
from app.models import User
from app.extensions import db
from flask_login import login_user, logout_user

user = Blueprint('user', __name__)


@user.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # create object
        u = User(username=form.username.data, password=form.password.data)
        # store in db
        db.session.add(u)
        db.session.commit()

        flash('URegistered successfully')
        return redirect(url_for('main.index'))
    return render_template('user/register.html', form=form)


@user.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None :
            flash('Invalid username or password')
            return redirect(url_for('user.login'))
        else:
            login_user(user)
            return redirect(url_for('main.index'))
    return render_template('user/login.html', form=form)


@user.route('/logout/')
def logout():
    logout_user()
    flash('Logout')
    return redirect(url_for('main.index'))
