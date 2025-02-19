import allure

from data import RandomString, Responses
from methods.user import User


class TestLoginUser:

    @allure.title("Проверка, что происходит авторизация существующего пользователя")
    def test_login_user_success(self, user):
        login_user = user['login']
        assert login_user['status_code'] == 200 and login_user['response']['success'] == True

    @allure.title("Проверка, что вернётся ошибка при отсутствии эмейла")
    def test_login_user_without_email(self):
        data_new_user = RandomString.data_new_user()
        login_user_error = User.login_user('', data_new_user['password'])
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR

    @allure.title("Проверка, что вернётся ошибка при отсутствии пароля")
    def test_login_user_without_password(self, user):
        data_new_user = user['data']
        login_user_error = User.login_user(data_new_user['email'], '')
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR

    @allure.title("Проверка, что что вернётся ошибка при вводе некорректного эмейла")
    def test_login_user_with_error_in_login(self, user):
        data_new_user = user['data']
        login_user_error = User.login_user(data_new_user['email']+'a', data_new_user['password'])
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR

    @allure.title("Проверка, что вернётся ошибка при вводе некорректного пароля")
    def test_login_user_with_error_in_password(self, user):
        data_new_user = user['data']
        login_user_error = User.login_user(data_new_user['email'], data_new_user['password']+'a')
        assert login_user_error['status_code'] == 401 and login_user_error['response']['message'] == Responses.LOGIN_USER_ERROR
