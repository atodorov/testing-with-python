import pytest

@pytest.fixture(scope='class')
def tester():
    return 'Alex'


@pytest.mark.usefixtures("tester")
class TestCase:
    def test_scenario_one(self, tester):
        assert 1 == 1
        assert 'Alex' == tester

    @pytest.mark.xfail
    def test_sceanrio_two(self, tester, session_id):
        assert 2 == 1
        assert 'Alex' == tester
        assert 1 == session_id

    def test_scenario_three(self):
        assert True


class TestCaseForSomethingElse:
    def test_scenario_four(self, tester, session_id):
        assert 1 == 1
        assert 'Alex' == tester
        assert 1 == session_id

    def test_scenario_five(self):
        assert True


def test_account_id_in_another_module(account_id, say_goodbye, session_id):
    assert 123456 == account_id
    assert 1 == session_id
