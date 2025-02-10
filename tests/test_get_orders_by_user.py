from data import RandomString, Responses, Ingredients


class TestGetOrderByUser:

    def test_get_orders_by_user_success(self, user, order):
        data_new_user = RandomString.data_new_user()
        user.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
        login_user = user.login_user(data_new_user['email'], data_new_user['password'])
        token_user = login_user['response']['accessToken']
        order.create_order(token_user, [Ingredients.BUN, Ingredients.MAIN])
        orders_by_user = order.get_orders_by_user(token_user)
        assert 200 <= orders_by_user['status_code'] < 300 and len(orders_by_user['response']['orders']) == 1

    def test_get_orders_by_user_unauth_error(self, user, order):
        orders_by_user = order.get_orders_by_user('')
        assert orders_by_user['status_code'] == 401 and orders_by_user['response']['message'] == Responses.GET_ORDERS_BY_USER_UNAUTH
