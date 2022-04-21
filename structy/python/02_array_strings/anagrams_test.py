from anagrams import is_anagram


def test_00():
    assert is_anagram("restful", "fluster") is True


def test_02():
    assert is_anagram("cats", "tocs") is False


def test_03():
    assert is_anagram("monkeyswrite", "newyorktimes") is True


def test_04():
    assert is_anagram("paper", "reapa") is False


def test_05():
    assert is_anagram("elbow", "below") is True


def test_06():
    assert is_anagram("tax", "taxi") is False


def test_07():
    assert is_anagram("taxi", "tax") is False


def test_08():
    assert is_anagram("night", "thing") is True


def test_09():
    assert is_anagram("abbc", "aabc") is False
