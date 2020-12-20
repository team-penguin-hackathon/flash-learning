from werkzeug.security import check_password_hash, generate_password_hash

from flash_learning import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id):
    """Load a user from the database."""

    return Student.query.filter_by(id=id).first()


class Student(UserMixin, db.Model):
    """Student data model."""

    #static key for user
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String(64), index=True, unique=True)
    grade = db.Column(db.Integer, index=True)
    activated = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, username, grade, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.grade = grade
        self.set_password(password)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password: str) -> None:
        """Hash the user's password before storing it in the database."""

        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> None:
        """Check the password hash from the database against the given password."""

        return check_password_hash(self.password, password)


class StudentFlashcard(db.Model):
    id = db.Column(db.String, primary_key=True)
    last_reviewed = db.Column(db.DATE, index=True)
