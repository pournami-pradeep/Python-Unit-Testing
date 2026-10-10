from main import addition


def test_addition_int():
    assert addition(2,3) == 5


def test_addition_float():
    assert addition(2.4, 3.0) == 5.4