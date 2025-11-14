'''
Unit tests for the ArrayStack class.
'''

from ArrayStack import ArrayStack
import pytest


################################################################################
# region ArrayStack.__init__(items0, items1, items2)
@pytest.mark.parametrize("items0, items1, items2, expected", [
    ([], [], [], "ArrayStack([], [], [])"),
    ([10], [20], [30], "ArrayStack([10], [20], [30])"),
    ([], [20, 21], [], "ArrayStack([], [21, 20], [])"),
    ([10, 11], [20, 21], [30, 31], "ArrayStack([11, 10], [21, 20], [31, 30])"),
])
def test_ArrayStack__init__(items0, items1, items2, expected):
    array_stack = ArrayStack(items0, items1, items2)
    assert isinstance(array_stack, ArrayStack)
    assert repr(array_stack) == expected
# endregion
################################################################################


################################################################################
# region ArrayStack.is_empty(stack_id)
@pytest.mark.parametrize("items1, items2, items3, stack_id, expected", [
    ([], [], [], 0, True),
    ([], [], [], 1, True),
    ([], [], [], 2, True),
    ([10], [20, 21], [30], 0, False),
    ([10], [20, 21], [30], 1, False),
    ([10], [20, 21], [30], 2, False),
])
def test_ArrayStack_is_empty(items1, items2, items3, stack_id, expected):
    array_stack = ArrayStack(items1, items2, items3)
    assert array_stack.is_empty(stack_id) == expected
# endregion
################################################################################


################################################################################
# region ArrayStack.peek(stack_id)
@pytest.mark.parametrize("items0, items1, items2, stack_id, expected", [
    ([10], [20], [30], 0, 10),
    ([10], [20], [30], 1, 20),
    ([10], [20], [30], 2, 30),
    ([], [20, 21], [], 1, 21),
    ([10, 11], [20, 21], [30, 31], 0, 11),
    ([10, 11], [20, 21], [30, 31], 1, 21),
    ([10, 11], [20, 21], [30, 31], 2, 31),
])
def test_ArrayStack_peek(items0, items1, items2, stack_id, expected):
    array_stack = ArrayStack(items0, items1, items2)
    assert array_stack.peek(stack_id) == expected


@pytest.mark.parametrize("items0, items1, items2, stack_id, expected", [
    ([], [], [], -1, ValueError),
    ([], [], [], 3, ValueError),
    ([], [], [], 0, IndexError),
    ([], [], [], 1, IndexError),
    ([], [], [], 2, IndexError),
    ([], [20, 21], [], 0, IndexError),
    ([], [20, 21], [], 0, IndexError),
])
def test_ArrayStack_peek_raises(items0, items1, items2, stack_id, expected):
    array_stack = ArrayStack(items0, items1, items2)
    with pytest.raises(expected):
        array_stack.peek(stack_id)
# endregion
################################################################################


################################################################################
# region ArrayStack.pop(stack_id)
@pytest.mark.parametrize("stack1, stack2, stack3, stack_id, popped, expected", [
    ([10, 11], [20, 21], [30, 31], 0, 11,
     "ArrayStack([10], [21, 20], [31, 30])"),
    ([10, 11], [20, 21], [30, 31], 1, 21,
     "ArrayStack([11, 10], [20], [31, 30])"),
    ([10, 11], [20, 21], [30, 31], 2, 31,
     "ArrayStack([11, 10], [21, 20], [30])"),
])
def test_ArrayStack_pop(stack1, stack2, stack3, stack_id, popped, expected):
    array_stack = ArrayStack(stack1, stack2, stack3)
    assert array_stack.pop(stack_id) == popped
    assert repr(array_stack) == expected


@pytest.mark.parametrize("items0, items1, items2, stack_id, expected", [
    ([], [], [], -1, ValueError),
    ([], [], [], 3, ValueError),
    ([], [], [], 0, IndexError),
    ([], [], [], 1, IndexError),
    ([], [], [], 2, IndexError),
    ([], [20, 21], [], 0, IndexError),
    ([], [20, 21], [], 0, IndexError),
])
def test_ArrayStack_pop_raises(items0, items1, items2, stack_id, expected):
    array_stack = ArrayStack(items0, items1, items2)
    with pytest.raises(expected):
        array_stack.pop(stack_id)

# endregion
################################################################################


################################################################################
# region ArrayStack.push(stack_id, data)
@pytest.mark.parametrize("stack1, stack2, stack3, stack_id, data, expected", [
    ([10, 11], [20, 21], [30, 31], 0, 12,
     "ArrayStack([12, 11, 10], [21, 20], [31, 30])"),
    ([10, 11], [20, 21], [30, 31], 1, 22,
     "ArrayStack([11, 10], [22, 21, 20], [31, 30])"),
    ([10, 11], [20, 21], [30, 31], 2, 32,
     "ArrayStack([11, 10], [21, 20], [32, 31, 30])"),
])
def test_ArrayStack_push(stack1, stack2, stack3, stack_id, data, expected):
    array_stack = ArrayStack(stack1, stack2, stack3)
    array_stack.push(stack_id, data)
    assert repr(array_stack) == expected


@pytest.mark.parametrize("stack_id", [
    (-1),
    (3),
])
def test_ArrayStack_push_raises(stack_id):
    array_stack = ArrayStack()
    with pytest.raises(ValueError):
        array_stack.push(stack_id, 0)
# endregion
################################################################################


################################################################################
# region ArrayStack._assert_stack_id(stack_id)
@pytest.mark.parametrize("stack_id, expected", [
    (0, True),
    (1, True),
    (2, True),
])
def test_ArrayStack__assert_stack_id(stack_id, expected):
    array_stack = ArrayStack()
    assert array_stack._assert_stack_id(stack_id) == expected


@pytest.mark.parametrize("stack_id", [
    (-1),
    (3),
])
def test_ArrayStack__assert_stack_id_raises(stack_id):
    array_stack = ArrayStack()
    with pytest.raises(ValueError):
        array_stack._assert_stack_id(stack_id)
# endregion
################################################################################


################################################################################
# region ArrayStack.__repr__()
@pytest.mark.parametrize("items1, items2, items3, expected", [
    ([], [], [],
     "ArrayStack([], [], [])"),
    ([10], [20], [30],
     "ArrayStack([10], [20], [30])"),
    ([], [20, 21], [],
     "ArrayStack([], [21, 20], [])"),
    ([10, 11], [20, 21], [30, 31],
     "ArrayStack([11, 10], [21, 20], [31, 30])"),
])
def test_ArrayStack__repr__(items1, items2, items3, expected):
    array_stack = ArrayStack(items1, items2, items3)
    assert repr(array_stack) == expected
# endregion
################################################################################
