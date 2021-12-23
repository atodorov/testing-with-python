def function_under_test(a, b):
    if b % 2 == 1:
        return a + b

    return a / b


def test_function():
    result = function_under_test(1, 1)
    assert 2 == result
