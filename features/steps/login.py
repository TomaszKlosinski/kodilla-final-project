# @given(u'user navigated to {endpoint}')
# def navigate_to(context, endpoint):
#     context.response = context.client.get(endpoint)
#     print(context.response)


# @given(u'user "{username}" exists')
# def create_user(context, username):
#     User(username='jdoe', email='sads').save()


# @when(u'fill registration form for user "{username}"')
# def step_impl(context, username):
#     form = context.response.forms["registerForm"]
#     form["username"] = username
#     form["email"] = "jdoe@example.com"
#     form["password"] = "secret"
#     form["confirm"] = "secret"
#     context.response = form.submit()


# @then(u'registration fails with error "Username already registered"')
# def step_impl(context):
#     assert "Username already registered" in context.response
