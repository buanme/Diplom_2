import requests

from data import Urls


class User:

    def create_user(self, email, password, name):
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

    def login_user(self, email, password):
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

    def delete_user(self, token):
        response = requests.delete(f'{Urls.BASE_URL}{Urls.DATA_USER}', headers={"Authorization": token})

        delete_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return delete_user

    def user_data_info(self, token):
        response = requests.get(f'{Urls.BASE_URL}{Urls.DATA_USER}', headers={"Authorization": token})

        user_info = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return user_info

    def updating_user_data(self, data, token):
        response = requests.patch(f'{Urls.BASE_URL}{Urls.DATA_USER}', json=data, headers={"Authorization": token})

        updated_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return updated_user
