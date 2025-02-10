from data import RandomString, Responses


class TestUpdatingUserData:

    def test_updating_user_email_success(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user_data = user.user_data_info(token_user)
        data_to_update = {'email': RandomString.data_new_user()['email']}
        updated_user = user.updating_user_data(data_to_update, token_user)
        assert 200 <= updated_user['status_code'] < 300 and \
               user_data['response']['user']['email'] != updated_user['response']['user']['email'] and \
               user_data['response']['user']['name'] == updated_user['response']['user']['name']
        user.delete_user(token_user)

    def test_updating_user_password_success(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user_data = user.user_data_info(token_user)
        data_to_update = {'password': RandomString.data_new_user()['password']}
        updated_user = user.updating_user_data(data_to_update, token_user)
        assert 200 <= updated_user['status_code'] < 300 and \
               user_data['response']['user']['email'] == updated_user['response']['user']['email'] and \
               user_data['response']['user']['name'] == updated_user['response']['user']['name']
        user.delete_user(token_user)

    def test_updating_user_name_success(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user_data = user.user_data_info(token_user)
        data_to_update = {'name': RandomString.data_new_user()['name']}
        updated_user = user.updating_user_data(data_to_update, token_user)
        assert 200 <= updated_user['status_code'] < 300 and \
               user_data['response']['user']['email'] == updated_user['response']['user']['email'] and \
               user_data['response']['user']['name'] != updated_user['response']['user']['name']
        user.delete_user(token_user)

    def test_updating_user_existing_email_error(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        user.create_user('new_'+data_new_user['email'], 'new_'+data_new_user['password'], 'new_'+data_new_user['name'])
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        data_to_update = {'email': 'new_'+data_new_user['email']}
        updated_user = user.updating_user_data(data_to_update, token_user)
        assert updated_user['status_code'] == 403 and updated_user['response']['message'] == Responses.UPDATING_EMAIL_ERROR
        user.delete_user(token_user)

    def test_updating_user_email_without_auth_error(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        data_to_update = {'email': RandomString.data_new_user()['email']}
        updated_user = user.updating_user_data(data_to_update, '')
        assert updated_user['status_code'] == 401 and updated_user['response']['message'] == Responses.UPDATING_USER_DATA_ERROR_IN_AUTH
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_updating_user_password_without_auth_error(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        data_to_update = {'password': RandomString.data_new_user()['password']}
        updated_user = user.updating_user_data(data_to_update, '')
        assert updated_user['status_code'] == 401 and updated_user['response']['message'] == Responses.UPDATING_USER_DATA_ERROR_IN_AUTH
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)

    def test_updating_user_name_without_auth_error(self, user):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        data_to_update = {'name': RandomString.data_new_user()['name']}
        updated_user = user.updating_user_data(data_to_update, '')
        assert updated_user['status_code'] == 401 and updated_user['response']['message'] == Responses.UPDATING_USER_DATA_ERROR_IN_AUTH
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        user.delete_user(token_user)
