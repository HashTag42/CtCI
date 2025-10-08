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
