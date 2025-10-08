from IsUnique2 import IsUnique


def test_case_1():
    assert IsUnique("ab") is True


def test_case_2():
    assert IsUnique("aa") is False


def test_case_3():
    assert IsUnique("") is True


def test_case_4():
    assert IsUnique("abcdef0123456ABCDEFáñ☺️東京") is True
