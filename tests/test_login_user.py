from data import RandomString, Responses


class TestCreateUser:

    def test_login_user_success(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        assert 200 <= login_user['status_code'] < 300 and login_user['response']['success'] == True
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_login_user_without_login(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user_error = user.login_user('', data_new_user['password'])
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_login_user_without_password(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user_error = user.login_user(data_new_user['email'], '')
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_login_user_with_error_in_login(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user_error = user.login_user(data_new_user['email']+'a', data_new_user['password'])
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_login_user_with_error_in_password(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user_error = user.login_user(data_new_user['email'], data_new_user['password']+'a')
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

