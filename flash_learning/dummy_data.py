import json
import os
from pathlib import Path

from flash_learning import db
from flash_learning.models.flashcard import Grade, Subject, Flashcard, Deck
from flash_learning.models.student import Student



class DummyData:
    """Generate a set of dummy data to populate the site's database."""

    def __init__(self):
        """Load all dummy files on initialization."""

        self.grades = self.load_data("grades")
        self.subjects = self.load_data("subjects")
        self.decks = self.load_data("decks")
        self.flashcards = self.load_data("flashcards")
        self.students = self.load_data("students")

    @staticmethod
    def load_data(filename):
        """Load json files containing sample data."""

        data_path = os.path.join("flash_learning", "data")

        with open(f"{data_path}/{filename}.json") as json_file:
            return json.load(json_file)

    def populate_database(self):
        """Populate the database."""

        self.add_flashcards()
        self.add_students()

    def add_flashcards(self):
        """Add flashcards to the database."""

        for grade in self.grades:
            g = Grade(grade=grade["level"])
            db.session.add(g)
            db.session.commit()

            for subject in self.subjects:
                grade_id = db.session.query(Grade).filter(Grade.grade == grade["level"]).first().id
                s = Subject(name=subject["name"], grade_id=grade_id)
                db.session.add(s)
                db.session.commit()

                decks = [d for d in self.decks if d["subject"] == subject["name"] and d["grade"] == grade["level"]]

                for deck in decks:
                    subject_id = db.session.query(Subject).filter(Subject.name == subject["name"],
                                                                  Subject.grade_id == grade_id).first().id
                    d = Deck(name=deck["name"], subject_id=subject_id)
                    db.session.add(d)
                    db.session.commit()

                    cards = [c for c in self.flashcards if c["subject"] == subject["name"] and
                             c["grade"] == grade["level"] and
                             c["deck"] == deck["name"]]

                    for card in cards:
                        deck_id = db.session.query(Deck).filter(Deck.name == deck["name"],
                                                                Deck.subject_id == subject_id).first().id
                        card_img_dir = Path("/static/img/flashcards")
                        card_path = f"{card['grade']}/{card['subject']}/{card['deck']}/{card['q_image']}"
                        flashcard_path = card_img_dir / card_path
                        c = Flashcard(number=card["number"],
                                      question=card["question"],
                                      answer=card["answer"],
                                      q_image=flashcard_path.as_posix(),
                                      deck_id=deck_id)
                        db.session.add(c)
                        db.session.commit()

    def add_students(self):
        """Add students to the database."""

        for student in self.students:
            u = Student(first_name=student["first_name"],
                        last_name=student["last_name"],
                        username=student["username"],
                        grade=student["grade"],
                        email=student["email"],
                        password=student["password"],
                        points=student["points"],
                        flashcards_attempted=student["flashcards_attempted"],
                        flashcards_correct=student["flashcards_correct"])

            db.session.add(u)
            db.session.commit()

