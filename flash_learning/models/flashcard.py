from flash_learning import db


class Grade(db.Model):
    """Database model for a grade from K-8 with multiple subjects."""

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String, index=True)
    subjects = db.relationship("Subject", backref="grade", lazy=True)

    def __init__(self, grade):
        self.grade = grade


class Subject(db.Model):
    """Database model for a single subject with multiple decks."""

    id = db.Column(db.Integer, primary_key=True)
    grade_id = db.Column(db.Integer, db.ForeignKey("grade.id"), nullable=False)
    name = db.Column(db.String, index=True)
    decks = db.relationship("Deck", backref="subject", lazy=True)

    def __init__(self, name, grade_id):
        self.name = name
        self.grade_id = grade_id


class Deck(db.Model):
    """Database model for a single deck with multiple flashcards."""

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)
    name = db.Column(db.String, index=True)
    cards = db.relationship("Flashcard", backref="deck", lazy=True)

    def __init__(self, name, subject_id):
        self.name = name
        self.subject_id = subject_id


class Flashcard(db.Model):
    """Database model for a single flashcard with a question and answer."""

    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.Integer, db.ForeignKey("deck.id"), nullable=False)
    number = db.Column(db.Integer, index=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)

    def __init__(self, number, question, answer, deck_id):
        self.number = number
        self.question = question
        self.answer = answer
        self.deck_id = deck_id

    def __repr__(self):
        return f"{self.number}) {self.question} : {self.answer}"
