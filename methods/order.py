import requests

from data import Urls


class Order:

    def create_order(self, token, ingredient):

        payload = {"ingredients": ingredient}
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDER}', headers={"Authorization": token}, data=payload)

        new_order = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return new_order

    def get_orders_by_user(self, token):

        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDER}', headers={"Authorization": token})

        orders_by_user = {
            "status_code": response.status_code,
            "response": response.json()
        }
        return orders_by_user
