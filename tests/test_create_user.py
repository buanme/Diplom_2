import allure

from data import RandomString, Responses
from methods.user import User


class TestCreateUser:

    @allure.title("Проверка, что создается уникальный пользователь")
    def test_create_user_success(self, user):
        create_user = user['create']
        assert create_user['status_code'] == 200 and create_user['response']['success']

    @allure.title("Проверка, что приходит ошибка при попытке создать существующего пользователя")
    def test_create_user_already_exists(self, user):
        data_new_user = user['data']
        user_already_exists = User.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        assert user_already_exists['status_code'] == 403 and user_already_exists['response']['message'] == Responses.CREATE_USER_ALREADY_EXISTS

    @allure.title("Проверка, что вернется ошибка при попытке создать пользователя без эмейла")
    def test_create_user_without_email(self):
        data_new_user = RandomString.data_new_user()
        new_user = User.create_user('', data_new_user['password'], data_new_user['name'])
        assert new_user['status_code'] == 403 and new_user['response']['message'] == Responses.CREATE_USER_WITHOUT_REQUIRED_FIELD

    @allure.title("Проверка, что вернется ошибка при попытке создать пользователя без пароля")
    def test_create_user_without_password(self):
        data_new_user = RandomString.data_new_user()
        new_user = User.create_user(data_new_user['email'], '', data_new_user['name'])
        assert new_user['status_code'] == 403 and new_user['response']['message'] == Responses.CREATE_USER_WITHOUT_REQUIRED_FIELD

    @allure.title("Проверка, что вернется ошибка при попытке создать пользователя без имени")
    def test_create_user_without_name(self):
        data_new_user = RandomString.data_new_user()
        new_user = User.create_user(data_new_user['email'], data_new_user['password'], '')
        assert new_user['status_code'] == 403 and new_user['response']['message'] == Responses.CREATE_USER_WITHOUT_REQUIRED_FIELD



