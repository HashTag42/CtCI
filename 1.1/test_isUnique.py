from IsUnique import IsUnique1
from IsUnique import IsUnique2


def test_IsUnique_1():
    assert IsUnique1("ab") is True
    assert IsUnique2("ab") is True


def test_IsUnique_2():
    assert IsUnique1("aa") is False
    assert IsUnique2("aa") is False


def test_IsUnique_3():
    assert IsUnique1("") is True
    assert IsUnique2("") is True


def test_IsUnique_4():
    assert IsUnique1("abcdef0123456ABCDEFáñ☺️東京") is True
    assert IsUnique2("abcdef0123456ABCDEFáñ☺️東京") is True
