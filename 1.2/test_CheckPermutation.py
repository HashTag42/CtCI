from CheckPermutation import CheckPermutation1, CheckPermutation2


def test_CheckPermutation1_1():
    assert CheckPermutation1("abc", "cba") is True


def test_CheckPermutation1_2():
    assert CheckPermutation1("aaa", "bbb") is False


def test_CheckPermutation1_3():
    assert CheckPermutation1("apple", "papel") is True


def test_CheckPermutation1_4():
    assert CheckPermutation1("carrot", "tarroc") is True


def test_CheckPermutation1_5():
    assert CheckPermutation1("", "") is True


def test_CheckPermutation2_1():
    assert CheckPermutation2("abc", "cba") is True


def test_CheckPermutation2_2():
    assert CheckPermutation2("aaa", "bbb") is False


def test_CheckPermutation2_3():
    assert CheckPermutation2("apple", "papel") is True


def test_CheckPermutation2_4():
    assert CheckPermutation2("carrot", "tarroc") is True


def test_CheckPermutation2_5():
    assert CheckPermutation2("", "") is True
