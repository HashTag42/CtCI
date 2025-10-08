from CheckPermutation import CheckPermutation


def test_CheckPermutation_1():
    assert CheckPermutation("abc", "cba") is True


def test_CheckPermutation_2():
    assert CheckPermutation("aaa", "bbb") is False


def test_CheckPermutation_3():
    assert CheckPermutation("apple", "papel") is True


def test_CheckPermutation_4():
    assert CheckPermutation("carrot", "tarroc") is True


def test_CheckPermutation_5():
    assert CheckPermutation("", "") is True
