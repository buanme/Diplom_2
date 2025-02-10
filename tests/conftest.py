import pytest

from methods.order import Order
from methods.user import User


@pytest.fixture
def user():
    user = User()
    return user


@pytest.fixture
def order():
    order = Order()
    return order
