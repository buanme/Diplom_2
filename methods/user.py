import allure
import requests

from data import Urls


class User:

    @staticmethod
    @allure.step("Метод создания пользователя")
    def create_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(f'{Urls.BASE_URL}{Urls.CREATE_USER}', data=payload)

        new_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return new_user

    @staticmethod
    @allure.step("Метод авторизации пользователя")
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password,
        }

        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_USER}', data=payload)

        auth_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return auth_user

    @staticmethod
    @allure.step("Метод удаления пользователя")
    def delete_user(token):
        response = requests.delete(f'{Urls.BASE_URL}{Urls.DATA_USER}', headers={"Authorization": token})

        delete_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return delete_user

    @staticmethod
    @allure.step("Метод получения данных пользователя")
    def user_data_info(token):
        response = requests.get(f'{Urls.BASE_URL}{Urls.DATA_USER}', headers={"Authorization": token})

        user_info = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return user_info

    @staticmethod
    @allure.step("Метод обновления данных пользователя")
    def updating_user_data(data, token):
        response = requests.patch(f'{Urls.BASE_URL}{Urls.DATA_USER}', json=data, headers={"Authorization": token})

        updated_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return updated_user
