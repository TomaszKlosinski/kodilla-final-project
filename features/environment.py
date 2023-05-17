import pytest
from blog import app
from config import Config
from blog.forms import LoginForm
from blog.models import Entry, db
from behave import fixture, use_fixture


@pytest.fixture
def client(app):
    with app.app_context():
        db.create_all()
    return app


def before_feature(context, feature):
    use_fixture(client, context)
