import pytest

@pytest.fixture(scope='function')
def say_hello():
    pass


@pytest.fixture(scope='module')
def say_goodbye():
    pass


@pytest.fixture(scope='package')
def account_id():
    return 123456


@pytest.fixture(scope='session')
def session_id():
    return 1
