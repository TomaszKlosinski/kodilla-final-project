from blog import app


def test_homepage():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200


# TODO

def test_login():
    pass


def test_logout():
    pass


def test_create_entry():
    pass


def test_create_draft():
    pass


def test_edit_entry():
    pass


def test_delete_entry():
    pass


def test_list_drafts():
    pass


def test_about():
    pass