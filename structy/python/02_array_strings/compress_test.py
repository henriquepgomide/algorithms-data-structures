from compress import compress


def test_00():
    assert compress("ccaaatsss") == "2c3at3s"


def test_01():
    assert compress("ssssbbz") == "4s2bz"


def test_02():
    assert compress("ppoppppp") == "2po5p"


def test_03():
    assert compress("nnneeeeeeeeeeeezz") == "3n12e2z"
