import pytest
from src.main import Main
from src.exceptions import *

DEFAULT_HOST = 'localhost'
DEFAULT_TICKETS = 'dummy_tickets'
DEFAULT_T_MAX = '0'
DEFAULT_T_MIN = '0'
DEFAULT_DATABASE = 'dummy_database'
DEFAULT_DATABASE_USER = 'dummy_user'
DEFAULT_DATABASE_PASSWORD = 'dummy_password'
DEFAULT_DATABASE_HOST = 'localhost'


def test_constructor_default_values():
    # test default values, test is launched in a container
    # without any defined environment variables
    main_app = Main()
    assert main_app.HOST == DEFAULT_HOST
    assert main_app.TOKEN is None
    assert main_app.TICKETS == DEFAULT_TICKETS
    assert main_app.T_MAX == DEFAULT_T_MAX
    assert main_app.T_MIN == DEFAULT_T_MIN
    assert main_app.DATABASE == DEFAULT_DATABASE
    assert main_app.DATABASE_HOST == DEFAULT_DATABASE_HOST
    assert main_app.DATABASE_USER == DEFAULT_DATABASE_USER
    assert main_app.DATABASE_PASSWORD == DEFAULT_DATABASE_PASSWORD    


def test_token_validation():
    # test default values, test is launched in a container
    # without any defined environment variables
    main_app = Main()
    with pytest.raises(NullTokenException):
        main_app.validate_token()
    
    main_app.TOKEN = 'dummy_token'
    main_app.validate_token()
