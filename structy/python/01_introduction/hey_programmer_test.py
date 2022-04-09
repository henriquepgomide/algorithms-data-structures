from hey_programmer import greet


def test_alvin():
    assert greet("alvin") == "hey alvin"


def test_jason():
    assert greet("jason") == "hey jason"


def test_how():
    assert greet("how now brown cow") == "hey how now brown cow"
