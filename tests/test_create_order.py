import allure

from data import Ingredients, RandomString, Responses


class TestCreateOrder:

    @allure.title("Проверка, что авторизованный пользователь может создать заказ с ингредиентами")
    def test_create_order_auth_user_with_ingredient_success(self, user, order):
        new_order = order.create_order(user['token'], [Ingredients.BUN, Ingredients.MAIN, Ingredients.SAUCE])
        assert new_order['status_code'] == 200 and new_order['response']['success']

    @allure.title("Проверка, что вернется ошибка при попытке создать заказ без ингредиентов")
    def test_create_order_auth_user_without_ingredient_error(self, user, order):
        new_order = order.create_order(user['token'], '')
        assert new_order['status_code'] == 400 and new_order['response']['message'] == Responses.CREATE_ORDER_WITHOUT_INGREDIENT

    @allure.title("Проверка, что вернется ошибка при попытке создать заказ с несуществующим ингредиентом")
    def test_create_order_auth_user_with_ingredient_invalid_error(self, user, order):
        new_order = order.create_order(user['token'], Ingredients.INVALID)
        assert new_order['status_code'] == 500 and new_order['response']['success'] == False

    @allure.title("Проверка, что неавторизованный пользователь не может создать заказ")
    def test_create_order_unauth_user_with_ingredient_error(self, order):
        new_order = order.create_order('', Ingredients.MAIN)
        assert new_order['status_code'] == 401 and new_order['response']['success'] == False
