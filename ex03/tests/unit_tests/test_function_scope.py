import pytest


def test_scenario_one(say_hello, say_goodbye):
    assert 1 == 1


@pytest.mark.xfail
def test_sceanrio_two(say_hello, say_goodbye):
    assert 2 == 1


def test_scenario_three(say_goodbye):
    assert True


def test_account_id(account_id, session_id):
    assert 123456 == account_id
    assert 1 == session_id
