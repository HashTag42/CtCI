from IsPalindromePermutation import IsPalindromePermutation


def test_IsPalindromePermutation_1():
    assert IsPalindromePermutation("Tact Coa") is True


def test_IsPalindromePermutation_2():
    assert IsPalindromePermutation("Rats live on no evil star") is True


def test_IsPalindromePermutation_3():
    assert IsPalindromePermutation("A man, a plan, a canal, panama") is True


def test_IsPalindromePermutation_4():
    assert IsPalindromePermutation("") is True


def test_IsPalindromePermutation_5():
    assert IsPalindromePermutation(" ") is True


def test_IsPalindromePermutation_6():
    assert IsPalindromePermutation("abc") is False


def test_IsPalindromePermutation_7():
    assert IsPalindromePermutation("jhsabckuj ahjsbckj") is True


def test_IsPalindromePermutation_8():
    assert IsPalindromePermutation("Able was I ere I saw Elba") is True


def test_IsPalindromePermutation_9():
    assert IsPalindromePermutation("no x in nixon") is True


def test_IsPalindromePermutation_10():
    assert IsPalindromePermutation("azAZ") is True


def test_IsPalindromePermutation_11():
    assert IsPalindromePermutation("So patient a nurse to nurse a patient so") is False
