from uncompress import uncompress


def test_00():
    assert uncompress("2c3a1t") == "ccaaat"


def test_01():
    assert uncompress("4s2b") == "ssssbb"


def test_02():
    assert uncompress("2p1o5p") == "ppoppppp"


def test_03():
    assert uncompress("3n12e2z") == "nnneeeeeeeeeeeezz"
