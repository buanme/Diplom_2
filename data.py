import random
import string


class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    CREATE_USER = '/auth/register'
    LOGIN_USER = '/auth/login'
    DATA_USER = '/auth/user'
    ORDER = '/orders'
    INGREDIENTS = '/ingredients'


class RandomString:

    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def data_new_user():
        # генерируем email, пароль и имя пользователя
        email = RandomString.generate_random_string(10)+'@'+RandomString.generate_random_string(5)+'.ru'
        password = RandomString.generate_random_string(10)
        name = RandomString.generate_random_string(10)

        # собираем тело запроса
        data = {
            "email": email,
            "password": password,
            "name": name
        }

        return data


class Responses:

    CREATE_USER_ALREADY_EXISTS = 'User already exists'
    CREATE_USER_WITHOUT_REQUIRED_FIELD = 'Email, password and name are required fields'
    LOGIN_USER_ERROR = 'email or password are incorrect'
    UPDATING_EMAIL_ERROR = 'User with such email already exists'
    UPDATING_USER_DATA_ERROR_IN_AUTH = 'You should be authorised'
    CREATE_ORDER_WITHOUT_INGREDIENT = 'Ingredient ids must be provided'
    GET_ORDERS_BY_USER_UNAUTH = 'You should be authorised'

class Ingredients:

    BUN = '61c0c5a71d1f82001bdaaa6d'
    MAIN = '61c0c5a71d1f82001bdaaa71'
    SAUCE = '61c0c5a71d1f82001bdaaa72'
    INVALID = '71c0c5a71d1f82001bdaaa72'
