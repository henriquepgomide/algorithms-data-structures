from is_prime import is_prime


def test_is_prime_2():
    assert is_prime(2)


def test_is_prime_3():
    assert is_prime(3) is True


def test_is_prime_4():
    assert is_prime(4) is False


def test_is_prime_5():
    assert is_prime(5) is True


def test_is_prime_6():
    assert is_prime(6) is False


def test_is_prime_7():
    assert is_prime(7) is True


def test_is_prime_8():
    assert is_prime(8) is False


def test_is_prime_25():
    assert is_prime(25) is False


def test_is_prime_31():
    assert is_prime(31) is True


def test_is_prime_2017():
    assert is_prime(2017) is True
