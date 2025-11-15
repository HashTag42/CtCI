from SetOfStacks import SetOfStacks, INCORRECT_CAPACITY
import pytest


################################################################################
# region SetOfStacks.__init__()
@pytest.mark.parametrize("capacity", [
    (1),
    (99),
])
def test_SetOfStacks__init__(capacity):
    SoS = SetOfStacks(capacity)
    assert isinstance(SoS, SetOfStacks)


@pytest.mark.parametrize("capacity, expected", [
    (-1, ValueError),
    (0, ValueError),
    ("A", ValueError),
])
def test_SetOfStacks__init__raises(capacity, expected):
    with pytest.raises(expected) as exc_info:
        SetOfStacks(capacity)
    assert str(exc_info.value) == INCORRECT_CAPACITY
# endregion
################################################################################


################################################################################
# region SetOfStacks.push()
def test_SelfOfStacks_push():
    SoS = SetOfStacks(3)
    SoS.push(1)
    assert SoS.peek() == 1
# endregion
################################################################################


################################################################################
# region SetOfStacks.push_from_list()
def test_SetOfStacks_push_from_list():
    SoS = SetOfStacks(3)
    SoS.push_from_list([1, 2, 3, 4, 5, 6])
    assert SoS.peek() == 6
# endregion
################################################################################


################################################################################
# region SetOfStacks.pop()
def test_SetOfStacks_pop():
    SoS = SetOfStacks(3)
    SoS.push_from_list([1, 2, 3, 4, 5, 6, 7])
    assert SoS.pop() == 7
    assert SoS.pop() == 6
    assert SoS.pop() == 5
    assert SoS.pop() == 4
    assert SoS.pop() == 3
    assert SoS.pop() == 2
    assert SoS.pop() == 1
    assert SoS.pop() is None
# endregion
################################################################################


################################################################################
# region SetOfStacks.pop_at()
def test_SetOfStacks_pop_at():
    SoS = SetOfStacks(3, [1, 2, 3, 4, 5, 6, 7])
    SoS.pop_at(1)
    assert repr(SoS) == "SetOfStacks(Capacity=3:[3, 2, 1][5, 4][7])"


@pytest.mark.parametrize("index, expected", [
    (-1, IndexError),
    (1, IndexError),
])
def test_SetOfStacks_pop_at_raises(index, expected):
    SoS = SetOfStacks(3)
    with pytest.raises(expected):
        SoS.pop_at(index)
# endregion
################################################################################


################################################################################
# region SetOfStacks.peek()
@pytest.mark.parametrize("capacity, items, expected", [
    (3, [], None),
    (3, [1], 1),
    (3, [1, 2, 3, 4, 5], 5),
    (3, [1, 2, 3, 4, 5, 6], 6),
    (3, [1, 2, 3, 4, 5, 6, 7], 7),
])
def test_SetOfStacks_peek(capacity, items, expected):
    SoS = SetOfStacks(capacity, items)
    assert SoS.peek() == expected
# endregion
################################################################################


################################################################################
# region SetOfStacks.__repr__()
@pytest.mark.parametrize("capacity, items, expected", [
    (3, [], "SetOfStacks(Capacity=3:[])"),
    (3, [1, 2, 3, 4, 5, 6], "SetOfStacks(Capacity=3:[3, 2, 1][6, 5, 4])"),
    (3, [1, 2, 3, 4, 5, 6, 7], "SetOfStacks(Capacity=3:[3, 2, 1][6, 5, 4][7])"),
])
def test_SetOfStacks__repr__(capacity, items, expected):
    SoS = SetOfStacks(capacity, items)
    assert repr(SoS) == expected
# endregion
################################################################################
