from flash_learning import db
from flash_learning.models.flashcard import Grade, Subject, Flashcard, Deck
from flash_learning.models.student import Student


class DummyData:
    grades = {'K', '1', '2', '3', '4', '5', '6', '7', '8'}
    subjects = {"Arts", "English", "Math", "Science", "Social Studies"}
    students = [
        {
            "first_name": "Betty",
            "last_name": "Boop",
            "username": "betty_boop",
            "email": "betty@boop.com",
            "password": "BoopTheSnoot123!",
            "grade": "K"
        },
        {
            "first_name": "Bugs",
            "last_name": "Bunny",
            "username": "bugs_bunny",
            "email": "bugs@bunny.com",
            "password": "Buggie789!!",
            "grade": "K"
        },
        {
            "first_name": "Charlie",
            "last_name": "Brown",
            "username": "charlie_brown",
            "email": "charlie@brown.com",
            "password": "BrownieCake4&!",
            "grade": "K"
        },
        {
            "first_name": "Daffy",
            "last_name": "Duck",
            "username": "daffy_duck",
            "email": "daffy@duck.com",
            "password": "QuackQuack67@@1",
            "grade": "K"
        },
        {
            "first_name": "Spongebob",
            "last_name": "Squarepants",
            "username": "spongebob_squarepants",
            "email": "spongebob@squarepants.com",
            "password": "IMREADy1!!",
            "grade": "K"
        },
        {
            "first_name": "Squidward",
            "last_name": "Tentacles",
            "username": "squidward_tentacles",
            "email": "squidward@tentacles.com",
            "password": "ClarinetIsLove333##",
            "grade": "1"
        },
        {
            "first_name": "Eugene",
            "last_name": "Krabs",
            "username": "eugene_krabs",
            "email": "eugene@krabs.com",
            "password": "MOneyMoneyM0ney!!",
            "grade": "1"
        },
        {
            "first_name": "Scooby",
            "last_name": "Doo",
            "username": "scooby_doo",
            "email": "scooby@doo.com",
            "password": "Ruff&&1111",
            "grade": "1"
        },
        {
            "first_name": "Tom",
            "last_name": "Cat",
            "username": "tom_cat",
            "email": "tom@cat.com",
            "password": "CatMix123!!",
            "grade": "1"
        },
        {
            "first_name": "Jerry",
            "last_name": "Mouse",
            "username": "jerry_mouse",
            "email": "jerry@mouse.com",
            "password": "CanttouchThis!#@!3",
            "grade": "1"
        },
        {
            "first_name": "Mickey",
            "last_name": "Mouse",
            "username": "mickey_mouse",
            "email": "mickey@mouse.com",
            "password": "HippityHoopla1234$$",
            "grade": "2"
        },
        {
            "first_name": "Winnie",
            "last_name": "Pooh",
            "username": "winnie_the_pooh",
            "email": "winnie@thepooh.com",
            "password": "HoneyLove&&1243",
            "grade": "2"
        },
        {
            "first_name": "Homer",
            "last_name": "Simpson",
            "username": "homer_simpson",
            "email": "homer@simpson.com",
            "password": "WOOHooo!@3",
            "grade": "2"
        },
        {
            "first_name": "Wile E.",
            "last_name": "Coyote",
            "username": "wile_e_coyote",
            "email": "wile@ecoyote.com",
            "password": "FallingFromabove123$",
            "grade": "3"
        },
        {
            "first_name": "Shaggy",
            "last_name": "Rogers",
            "username": "shaggy_rogers",
            "email": "shaggy@rogers.com",
            "password": "YOINKs!32",
            "grade": "3"
        },
        {
            "first_name": "Shrek",
            "last_name": "Ogre",
            "username": "shrek_the_ogre",
            "email": "shrek@ogre.com",
            "password": "ONionZ1#11",
            "grade": "3"
        },
        {
            "first_name": "Fred",
            "last_name": "Flinstone",
            "username": "fred_flinstone",
            "email": "fred@flinstone.com",
            "password": "YabaDabado00!",
            "grade": "4"
        },
        {
            "first_name": "Bart",
            "last_name": "Simpson",
            "username": "bart_simpson",
            "email": "bart@simpson.com",
            "password": "Hehehe&&132",
            "grade": "4"
        },
        {
            "first_name": "Pink",
            "last_name": "Panther",
            "username": "pink_panther",
            "email": "pink@panther.com",
            "password": "SneakyPink11^&",
            "grade": "4"
        },
        {
            "first_name": "Stewie",
            "last_name": "Griffin",
            "username": "stewie_griffin",
            "email": "stewie@griffin.com",
            "password": "WhatIsthisN0neSen$e",
            "grade": "5"
        },
        {
            "first_name": "Patrick",
            "last_name": "Star",
            "username": "patrick_star",
            "email": "patrick@star.com",
            "password": "Dr.ProfessorP4trick",
            "grade": "5"
        },
        {
            "first_name": "Timmy",
            "last_name": "Turner",
            "username": "timmy_turner",
            "email": "timmy@turner.com",
            "password": "IwishIhad&3abird",
            "grade": "5"
        },
        {
            "first_name": "Sandy",
            "last_name": "Cheeks",
            "username": "sandy_cheeks",
            "email": "sandy@cheeks.com",
            "password": "MadScIent1st!",
            "grade": "6"
        },
        {
            "first_name": "Mr.",
            "last_name": "Burns",
            "username": "mr_burns",
            "email": "mr@burns.com",
            "password": "IBr3atheEv!l",
            "grade": "6"
        },
        {
            "first_name": "Jimmy",
            "last_name": "Neutron",
            "username": "jimmy_neutron",
            "email": "jimmy@neutron.com",
            "password": "Sup3rGen!us",
            "grade": "6"
        },
        {
            "first_name": "Jake",
            "last_name": "The Dog",
            "username": "jake_the_dog",
            "email": "jake@thedog.com",
            "password": "Sl1nkey&1",
            "grade": "7"
        },
        {
            "first_name": "Lilo",
            "last_name": "Pelekai",
            "username": "lilo_pelekai",
            "email": "lilo@pelekai.com",
            "password": "Wh3resSt!tch?",
            "grade": "7"
        },
        {
            "first_name": "Johnny",
            "last_name": "Bravo",
            "username": "johnny_bravo",
            "email": "johnny@bravo.com",
            "password": "I4mMusc!e",
            "grade": "7"
        },
        {
            "first_name": "Inspector",
            "last_name": "Gadget",
            "username": "inspector_gadget",
            "email": "inspector@gadget.com",
            "password": "GogoG4dget!",
            "grade": "8"
        },
        {
            "first_name": "Gumball",
            "last_name": "Watterson",
            "username": "gumball_watterson",
            "email": "gumball@watterson.com",
            "password": "Haha!33455",
            "grade": "8"
        },
        {
            "first_name": "Angelica",
            "last_name": "Pickles",
            "username": "angelica_pickles",
            "email": "angelica@pickles.com",
            "password": "I4mBully#@",
            "grade": "8"
        }
    ]
    decks = [
        {
            "name": "Colors",
            "subject": "Arts",
            "grade": 'K'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": 'K'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": 'K'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": 'K'
        },
        {
            "name": "Addition",
            "subject": "Math",
            "grade": 'K'
        },
        {
            "name": "Counting",
            "subject": "Math",
            "grade": 'K'
        },
        {
            "name": "Animals",
            "subject": "Science",
            "grade": 'K'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '1'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '1'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '1'
        },
        {
            "name": "Addition",
            "subject": "Math",
            "grade": '1'
        },
        {
            "name": "Shapes",
            "subject": "Math",
            "grade": '1'
        },
        {
            "name": "Weather",
            "subject": "Science",
            "grade": '1'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '1'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '2'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '2'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '2'
        },
        {
            "name": "Subtraction",
            "subject": "Math",
            "grade": '2'
        },
        {
            "name": "Shapes",
            "subject": "Math",
            "grade": '2'
        },
        {
            "name": "Earth Science",
            "subject": "Science",
            "grade": '2'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '3'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '3'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '3'
        },
        {
            "name": "Multiplication",
            "subject": "Math",
            "grade": '3'
        },
        {
            "name": "Geometry",
            "subject": "Math",
            "grade": '3'
        },
        {
            "name": "Earth Science",
            "subject": "Science",
            "grade": '3'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '3'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '4'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '4'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '4'
        },
        {
            "name": "Division",
            "subject": "Math",
            "grade": '4'
        },
        {
            "name": "Geometry",
            "subject": "Math",
            "grade": '4'
        },
        {
            "name": "Earth Science",
            "subject": "Science",
            "grade": '4'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '4'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '5'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '5'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '5'
        },
        {
            "name": "Multiplication",
            "subject": "Math",
            "grade": '5'
        },
        {
            "name": "Geometry",
            "subject": "Math",
            "grade": '5'
        },
        {
            "name": "Earth Science",
            "subject": "Science",
            "grade": '5'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '5'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '6'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '6'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '6'
        },
        {
            "name": "Division",
            "subject": "Math",
            "grade": '6'
        },
        {
            "name": "Geometry",
            "subject": "Math",
            "grade": '6'
        },
        {
            "name": "Biology",
            "subject": "Science",
            "grade": '6'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '6'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '7'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '7'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '7'
        },
        {
            "name": "Word Problems",
            "subject": "Math",
            "grade": '7'
        },
        {
            "name": "Statistics",
            "subject": "Math",
            "grade": '7'
        },
        {
            "name": "Chemistry",
            "subject": "Science",
            "grade": '7'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '7'
        },
        {
            "name": "Grammar",
            "subject": "English",
            "grade": '8'
        },
        {
            "name": "Spelling",
            "subject": "English",
            "grade": '8'
        },
        {
            "name": "Vocabulary",
            "subject": "English",
            "grade": '8'
        },
        {
            "name": "Graphs",
            "subject": "Math",
            "grade": '8'
        },
        {
            "name": "Geometry",
            "subject": "Math",
            "grade": '8'
        },
        {
            "name": "Physics",
            "subject": "Science",
            "grade": '8'
        },
        {
            "name": "History",
            "subject": "Social Studies",
            "grade": '8'
        },
    ]
    flashcards = [
        {

        }
    ]

    def populate_database(self):
        for grade in self.grades:
            g = Grade(grade=grade)
            db.session.add(g)
            db.session.commit()

            for subject in self.subjects:
                grade_id = db.session.query(Grade).filter(Grade.grade == grade).first().id
                s = Subject(name=subject, grade_id=grade_id)
                db.session.add(s)
                db.session.commit()

                decks = [d for d in self.decks if d["grade"] == grade]
                for deck in decks:
                    subject_id = db.session.query(Subject).filter(Subject.name == subject).first().id
                    d = Deck(name=deck["name"], subject_id=subject_id)
                    db.session.add(d)
                    db.session.commit()

                    for card in self.flashcards:
                        pass

        for student in self.students:
            u = Student(first_name=student["first_name"],
                        last_name=student["last_name"],
                        username=student["username"],
                        grade=student["grade"],
                        email=student["email"],
                        password=student["password"])
            db.session.add(u)
            db.session.commit()

