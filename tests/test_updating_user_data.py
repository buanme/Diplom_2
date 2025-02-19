import allure

from data import RandomString, Responses
from methods.user import User


class TestUpdatingUserData:

    @allure.title("Проверка, что проходит изменение эмейла")
    def test_updating_user_email_success(self, user):
        user_data = User.user_data_info(user['token'])
        data_to_update = {'email': RandomString.data_new_user()['email']}
        updated_user = User.updating_user_data(data_to_update, user['token'])
        assert (updated_user['status_code'] == 200 and
               user_data['response']['user']['email'] != updated_user['response']['user']['email'] and
               user_data['response']['user']['name'] == updated_user['response']['user']['name'])

    @allure.title("Проверка, что проходит изменение пароля")
    def test_updating_user_password_success(self, user):
        user_data = User.user_data_info(user['token'])
        data_to_update = {'password': RandomString.data_new_user()['password']}
        updated_user = User.updating_user_data(data_to_update, user['token'])
        assert (updated_user['status_code'] == 200 and
               user_data['response']['user']['email'] == updated_user['response']['user']['email'] and
               user_data['response']['user']['name'] == updated_user['response']['user']['name'])

    @allure.title("Проверка, что проходит изменение имени")
    def test_updating_user_name_success(self, user):
        user_data = User.user_data_info(user['token'])
        data_to_update = {'name': RandomString.data_new_user()['name']}
        updated_user = User.updating_user_data(data_to_update, user['token'])
        assert (updated_user['status_code'] == 200 and
               user_data['response']['user']['email'] == updated_user['response']['user']['email'] and
               user_data['response']['user']['name'] != updated_user['response']['user']['name'])

    @allure.title("Проверка, что приходит ошибка при попытке обновить эмейл на уже зарегистрированный")
    def test_updating_user_existing_email_error(self, user):
        data_new_user = user['data']
        User.create_user('new_'+data_new_user['email'], 'new_'+data_new_user['password'], 'new_'+data_new_user['name'])
        data_to_update = {'email': 'new_'+data_new_user['email']}
        updated_user = User.updating_user_data(data_to_update, user['token'])
        assert updated_user['status_code'] == 403 and updated_user['response']['message'] == Responses.UPDATING_EMAIL_ERROR
        # удаляем второго пользователя
        login_new_user = User.login_user('new_'+data_new_user['email'], 'new_'+data_new_user['password'])
        token_new_user = login_new_user['response']['accessToken']
        User.delete_user(token_new_user)

    @allure.title("Проверка, что приходит ошибка обновления эмейла для неавторизованного пользователя")
    def test_updating_user_email_without_auth_error(self):
        data_to_update = {'email': RandomString.data_new_user()['email']}
        updated_user = User.updating_user_data(data_to_update, '')
        assert updated_user['status_code'] == 401 and updated_user['response']['message'] == Responses.UPDATING_USER_DATA_ERROR_IN_AUTH

    @allure.title("Проверка, что приходит ошибка обновления пароля для неавторизованного пользователя")
    def test_updating_user_password_without_auth_error(self):
        data_to_update = {'password': RandomString.data_new_user()['password']}
        updated_user = User.updating_user_data(data_to_update, '')
        assert updated_user['status_code'] == 401 and updated_user['response']['message'] == Responses.UPDATING_USER_DATA_ERROR_IN_AUTH

    @allure.title("Проверка, что приходит ошибка обновления имени для неавторизованного пользователя")
    def test_updating_user_name_without_auth_error(self):
        data_to_update = {'name': RandomString.data_new_user()['name']}
        updated_user = User.updating_user_data(data_to_update, '')
        assert updated_user['status_code'] == 401 and updated_user['response']['message'] == Responses.UPDATING_USER_DATA_ERROR_IN_AUTH
