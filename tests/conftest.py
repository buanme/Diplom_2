import pytest

from data import RandomString
from methods.order import Order
from methods.user import User


@pytest.fixture
def user():
    data_new_user = RandomString.data_new_user()
    create_user = User.create_user(data_new_user['email'], data_new_user['password'], data_new_user['name'])
    login_user = User.login_user(data_new_user['email'], data_new_user['password'])
    token_user = login_user['response']['accessToken']
    yield {'data': data_new_user, 'create': create_user, 'login': login_user, 'token': token_user}
    User.delete_user(token_user)


@pytest.fixture
def order():
    order = Order()
    return order
