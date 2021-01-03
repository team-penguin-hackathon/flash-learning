import os

from sqlalchemy import exc

from flash_learning import create_app, db
from flash_learning.dummy_data import DummyData


app = create_app()


@app.before_first_request
def create_tables() -> None:
    """
    Populate the database with dummy data on initial app startup.
    """

    if os.path.exists("flash_learning/site.db"):
        return

    db.create_all()

    try:
        dummy_data = DummyData()
        dummy_data.populate_database()

    # Database is already populated with dummy data.
    except exc.IntegrityError:
        db.session.rollback()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
