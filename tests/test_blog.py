from blog import app
from config import Config
from blog.forms import LoginForm
from blog.models import Entry, db


# Helpers

def _login(client, username, password):
    app.config['WTF_CSRF_ENABLED'] = False

    response = client.post('/login/', follow_redirects=True, data={
        "username": username,
        "password": password,
    })

    return response


def _is_redirected(response, path='/'):
    return len(response.history) == 1 and response.request.path == path


def _add_entry(client, title, body, is_published):
    response = client.post('/posts/', follow_redirects=True, data={
        "title": title,
        "body": body,
        "is_published": is_published
    })
    return response


# Unit tests

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_about(client):
    response = client.get('/about/')
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    print(content)
    assert '<h3>About</h3>' in content


def test_login_form(client):
    response = client.get('/login/')
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    assert '<label for="title">Username</label>' in content
    assert '<label for="body">Password</label>' in content


def test_login_with_valid_credentials(client):
    response = _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    assert 'You are now logged in' in content

    assert _is_redirected(response)


def test_login_with_invalid_credentials(client):
    response = _login(client, 'dummy-user', 'dummy-password')
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    assert 'Invalid username' in content
    assert 'Invalid password' in content

    assert not _is_redirected(response)


def test_logout(client):
    response = client.post('/logout/', follow_redirects=True)
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    assert 'You are now logged out' in content

    assert _is_redirected(response)


def test_list_drafts(client):
    response = _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
    assert response.status_code == 200

    response = client.get('/drafts/', follow_redirects=True)
    content = response.get_data().decode('utf-8')
    assert '<th scope="col">Data</th>' in content



def test_create_entry_form_wihout_login(client):
    response = client.get('/posts/', follow_redirects=True)
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    assert '<label for="title">Username</label>' in content
    assert '<label for="body">Password</label>' in content

    assert _is_redirected(response, path='/login/')


def test_create_entry_form_wih_login(client):
    _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

    response = client.get('/posts/', follow_redirects=True)
    assert response.status_code == 200

    content = response.get_data().decode('utf-8')
    assert '<label for="title">Title</label>' in content
    assert '<label for="body">Content</label>' in content


def test_create_draft(client):
    _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

    response = _add_entry(client, 'dummy-title1', 'dummy-body1', 'false')
    assert response.status_code == 200

    response = client.get('/drafts/', follow_redirects=True)
    content = response.get_data().decode('utf-8')
    assert 'dummy-title1' in content


def test_create_entry(client):
    _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

    response = _add_entry(client, 'dummy-title2', 'dummy-body2', 'true')
    assert response.status_code == 200

    response = client.get('/', follow_redirects=True)
    content = response.get_data().decode('utf-8')
    assert 'dummy-title2' in content


# def test_edit_entry(client):
#     _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
#     _add_entry(client, 'dummy-title1', 'dummy-body1', 'false')

#     # TODO: Get ID
#     response = client.get('/', follow_redirects=True)
#     content = response.get_data().decode('utf-8')
#     print(content)

#     response = client.post('/posts/1', follow_redirects=True, data={
#         "title": "dummy-123",
#         "body": "dummy-123",
#         "is_published": "true"
#     })
#     assert response.status_code == 200

#     response = client.get('/posts/1', follow_redirects=True)
#     assert response.status_code == 200

#     content = response.get_data().decode('utf-8')
#     assert '<input class="form-control" id="title" name="title" required type="text" value="dummy-123">' in content


# def test_delete_entry(client):
#     _login(client, Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
#     _add_entry(client, 'dummy-title1', 'dummy-body1', 'false')

#     response = client.post('/posts/1/delete', follow_redirects=True)
#     assert response.status_code == 200

#     response = client.get('/posts/1', follow_redirects=True)
#     assert response.status_code == 404
