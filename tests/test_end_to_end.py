import pytest
from blog import app
from config import Config
from blog.forms import LoginForm
from blog.models import Entry, db
from webtest import TestApp


@pytest.fixture
def client(app):
    with app.app_context():
        db.create_all()
    return TestApp(app)

class TestLogin:

    def test_can_login_and_add_entry(self, client):
        with app.app_context():
            entry_count = Entry.query.count()

            response = client.get("/")
            response = response.click("Log in")
            form = response.forms[0]
            form["username"] = Config.ADMIN_USERNAME
            form["password"] = Config.ADMIN_PASSWORD
            res = form.submit().follow()
            assert res.status_code == 200


            response = client.get("/")
            response = response.click("New post")
            form = response.forms[1]
            form["title"] = "test123"
            form["body"] = "test123"
            form["is_published"] = "true"
            res = form.submit()
            assert res.status_code == 200


            assert Entry.query.count() == entry_count + 1


    def test_cannot_login_with_invalid_username_and_password(self, client):
        with app.app_context():
            response = client.get("/")
            response = response.click("Log in")
            form = response.forms[0]
            form["username"] = "dummy-user"
            form["password"] = "dummy-password"
            res = form.submit()
            assert res.status_code == 200

            assert 'Invalid username' in str(res.html)
            assert 'Invalid password' in str(res.html)
