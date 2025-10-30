from return_kth_to_last import return_Kth_to_last1, return_Kth_to_last2, return_Kth_to_last3
from LinkedList import LinkedList
import pytest

positive_cases = [
    # list, Kth, expected
    ([1], 0, 1),
    ([1, 2, 3, 4, 5], 0, 5),
    ([1, 2, 3, 4, 5], 1, 4),
    ([1, 2, 3, 4, 5], 2, 3),
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 4, 1),
]

negative_cases = [
    # list, Kth, expected
    ([], 0, ValueError),
    ([1, 2, 3, 4, 5], -1, ValueError),
    ([1, 2, 3, 4, 5], 5, ValueError),
]


# return_Kth_to_last1
@pytest.mark.parametrize("list, Kth, expected", positive_cases)
def test_return_Kth_to_last1_positive_cases(list, Kth, expected):
    linked_list = LinkedList(list)
    assert return_Kth_to_last1(linked_list, Kth) == expected


@pytest.mark.parametrize("list, Kth, expected", negative_cases)
def test_return_Kth_to_last1_negative_cases(list, Kth, expected):
    linked_list = LinkedList(list)
    with pytest.raises(expected):
        return_Kth_to_last1(linked_list, Kth)


# return_Kth_to_last2
@pytest.mark.parametrize("list, Kth, expected", positive_cases)
def test_return_Kth_to_last2_positive_cases(list, Kth, expected):
    linked_list = LinkedList(list)
    assert return_Kth_to_last2(linked_list.head, Kth) == expected


@pytest.mark.parametrize("list, Kth, expected", negative_cases)
def test_return_Kth_to_last2_negative_cases(list, Kth, expected):
    linked_list = LinkedList(list)
    with pytest.raises(expected):
        return_Kth_to_last2(linked_list.head, Kth)


# return_Kth_to_last3
@pytest.mark.parametrize("list, Kth, expected", positive_cases)
def test_return_Kth_to_last3_positive_cases(list, Kth, expected):
    linked_list = LinkedList(list)
    assert return_Kth_to_last3(linked_list.head, Kth) == expected


@pytest.mark.parametrize("list, Kth, expected", negative_cases)
def test_return_Kth_to_last3_negative_cases(list, Kth, expected):
    linked_list = LinkedList(list)
    with pytest.raises(expected):
        return_Kth_to_last3(linked_list.head, Kth)
