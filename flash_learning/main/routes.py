import os

from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from flask_login import login_user, current_user, logout_user
from werkzeug.urls import url_parse

from flash_learning.models.student import Student
from flash_learning.main.forms import LoginForm,SignupForm
from flash_learning import db
from base64 import b64encode


main = Blueprint("main", __name__)


@main.route('/', methods=["GET", "POST"])
def index():
    """The app's landing page."""
    return render_template("index.html")


@main.route('/login', methods=["GET", "POST"])
def login():
    """"Student login page."""

    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    # Redirect the student to their home page if username and password are correct, otherwise stay at the login page.
    if form.validate_on_submit():
        user = Student.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("main.login"))
        if request.form.get('remember')!=None:
            login_user(user,remember=True)
        else:
            session.permanent = True
            login_user(user)
        return redirect(url_for("student.home", username=user.username))

    return render_template("login.html", title="Sign In", form=form)


@main.route("/logout")
def logout():
    """Logout the current user."""
    logout_user()

    return redirect(url_for("main.index"))


@main.route('/signup', methods=['POST','GET'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignupForm()
    if form.validate_on_submit():
        user = Student(first_name=form.first_name.data,
                       last_name=form.last_name.data,
                       username=form.username.data,
                       grade=form.grade.data,
                       email=form.email.data,
                       password=form.password.data)
        alternative_id=b64encode(os.urandom(24)).decode('utf-8')
        while User.query.filter_by(alternative_id=alternative_id).first()!=None:
            alternative_id = b64encode(os.urandom(24)).decode('utf-8')
        user.set_password(form.password.data)
        user.alternative_id=alternative_id
        login_user(user, remember=False)
        db.session.add(user)
        db.session.commit()
        flash("Welcome to Flash Learning!")
        return redirect(url_for("main.login"))
    # else:

    return render_template("signup.html", title="Sign Up", form=form)


