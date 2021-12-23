import pytest


def test_scenario_ten():
    assert 1 == 1


@pytest.mark.xfail
def test_sceanrio_eleven():
    assert 2 == 1


def test_scenario_thirteen(say_goodbye):
    assert True


def test_scenario_fourteen(session_id):
    assert 2 > 1
    assert 1 == session_id
