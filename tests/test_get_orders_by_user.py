import allure

from data import RandomString, Responses, Ingredients


class TestGetOrderByUser:

    @allure.title("Проверка, что можно получить список заказов конкретного пользователя")
    def test_get_orders_by_user_success(self, user, order):
        order.create_order(user['token'], [Ingredients.BUN, Ingredients.MAIN])
        orders_by_user = order.get_orders_by_user(user['token'])
        assert orders_by_user['status_code'] == 200 and len(orders_by_user['response']['orders']) == 1

    @allure.title("Проверка, что вернется ошибка при попытке получить список заказов неавторизованным пользователем")
    def test_get_orders_by_user_unauth_error(self, order):
        orders_by_user = order.get_orders_by_user('')
        assert orders_by_user['status_code'] == 401 and orders_by_user['response']['message'] == Responses.GET_ORDERS_BY_USER_UNAUTH
