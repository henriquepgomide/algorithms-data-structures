from max_value import max_value


def test_max_one():
    assert max_value([4, 7, 2, 8, 10, 9])


def test_max_two():
    assert max_value([10, 5, 40, 40.3]) == 40.3


def test_max_three():
    assert max_value([-5, -2, -1, -11]) == -1


def test_max_four():
    assert max_value([42]) == 42


def test_max_five():
    assert max_value([1000, 8]) == 1000


def test_max_six():
    assert max_value([1000, 8, 9000]) == 9000


def test_max_seven():
    assert max_value([2, 5, 1, 1, 4]) == 5
