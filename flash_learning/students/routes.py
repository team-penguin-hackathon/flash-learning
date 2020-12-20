from flask import Blueprint, render_template
from flask_login import login_required

from flash_learning import db
from flash_learning.models.flashcard import Grade, Subject
from flash_learning.models.student import Student


students = Blueprint("student", __name__)


@students.route("/student/<username>/home", methods=["GET"])
@login_required
def home(username):
    # Get the subjects for the student's grade level.
    student = Student.query.filter_by(username=username).first()
    grade_id = db.session.query(Grade).filter(Grade.grade == student.grade).first().id
    subjects = Subject.query.filter_by(grade_id=grade_id).all()

    return render_template("home.html", title="Home", user=student, subjects=subjects)


@students.route("/student/<username>/profile", methods=["GET"])
@login_required
def profile(username):
    student = Student.query.filter_by(username=username).first()
    return render_template("profile.html", title="Profile", user=student)


@students.route("/student/<username>/stats", methods=["GET"])
@login_required
def stats(username):
    student = Student.query.filter_by(username=username).first()
    return render_template("stats.html", title="Stats", user=student)


@students.route("/student/<username>/leaderboard", methods=["GET"])
@login_required
def leaderboard(username):
    student = Student.query.filter_by(username=username).first()
    return render_template("leaderboard.html", title="Leaderboard", scores=scores)
