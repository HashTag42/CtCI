from URLify import URLify


def test_URLify_1():
    assert URLify("Mr John Smith      ", 13) == "Mr%20John%20Smith"


def test_URLify_2():
    assert URLify("", 0) == ""
