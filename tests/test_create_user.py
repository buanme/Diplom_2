from data import RandomString, Responses


class TestCreateUser:

    def test_create_user_success(self, user):
        data_new_user = RandomString.data_new_user()
        new_user = user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        assert 200 <= new_user['status_code'] < 300
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_create_user_already_exists(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        user_already_exists = user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        assert user_already_exists['status_code'] == 403 and user_already_exists['response']['message'] == Responses.CREATE_USER_ALREADY_EXISTS
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_create_user_without_email(self, user):
        data_new_user = RandomString.data_new_user()
        new_user = user.create_user('', data_new_user['password'], data_new_user['name'])
        assert new_user['status_code'] == 403 and new_user['response']['message'] == Responses.CREATE_USER_WITHOUT_REQUIRED_FIELD

    def test_create_user_without_password(self, user):
        data_new_user = RandomString.data_new_user()
        new_user = user.create_user(data_new_user['email'], '', data_new_user['name'])
        assert new_user['status_code'] == 403 and new_user['response']['message'] == Responses.CREATE_USER_WITHOUT_REQUIRED_FIELD

    def test_create_user_without_name(self, user):
        data_new_user = RandomString.data_new_user()
        new_user = user.create_user(data_new_user['email'], data_new_user['password'], '')
        assert new_user['status_code'] == 403 and new_user['response']['message'] == Responses.CREATE_USER_WITHOUT_REQUIRED_FIELD



