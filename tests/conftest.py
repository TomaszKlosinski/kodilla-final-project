import os
import pytest
from config import Config
from blog import app as blog_app
from blog.models import Entry, db
import data_generator


@pytest.fixture()
def app():
    blog_app.config.update({
        "TESTING": True
    })

    # Initilize test database
    with blog_app.app_context():
        db.create_all()
        if not Entry.query.all():
            data_generator.generate_entries()

    yield blog_app


@pytest.fixture()
def client(app):
    return app.test_client()
