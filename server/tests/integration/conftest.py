from datetime import datetime
from datetime import timedelta

import pytest
from app import create_app
from app.db import connect_to_db
from app.db import db
from app.models.course_model import Course
from app.models.user_model import User
from app.utilities.init_db import create_db

# from app.utilities.init_db import drop_db


def load_test_data():
    """Load test data into db."""

    future_iso_date = datetime.isoformat(datetime.now() + timedelta(days=30))
    past_iso_date = datetime.isoformat(datetime.now() - timedelta(days=30))

    courses = [
        {
            "name": "Awesome Course",
            "link": "https://udemy.com/awesomecourse",
            "description": "Whatta course!",
            "coupons": [
                {
                    "code": "NOT_EXPIRED",
                    "expiration_iso_string": future_iso_date,
                },
                {
                    "code": "EXPIRED",
                    "expiration_iso_string": past_iso_date,
                },
            ],
            "review_quotes": [
                {"review_quote": "the best!"},
                {"review_quote": "meh"},
            ],
        },
    ]
    users = [{"username": "admin", "password": "abc123"}]

    for course in courses:
        Course(**course)

    for user in users:
        User(**user)


@pytest.fixture
def app():
    return create_app(flask_env="test")


@pytest.fixture
def test_db(app):
    create_db(app)

    db.init_app(app)
    connect_to_db(app)

    db.create_all()
    load_test_data()

    yield test_db

    # cleanup
    db.session.close()
    db.drop_all()
    # drop_db()  # TODO: get this working
