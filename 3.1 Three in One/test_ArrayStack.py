'''
Unit tests for the ArrayStack class.
'''

from ArrayStack import ArrayStack
import pytest


################################################################################
# region ArrayStack.__init__(items1, items2, items3)
@pytest.mark.parametrize("items1, items2, items3, expected", [
    ([], [], [], "ArrayStack(['stack1', 'stack2', 'stack3'])"),
    ([10], [20], [30], "ArrayStack(['stack1', 10, 'stack2', 20, 'stack3', 30])"),
    ([10, 11], [20, 21], [30, 31], "ArrayStack(['stack1', 11, 10, 'stack2', 21, 20, 'stack3', 31, 30])"),
])
def test_ArrayStack__init__(items1, items2, items3, expected):
    array_stack = ArrayStack(items1, items2, items3)
    assert isinstance(array_stack, ArrayStack)
    assert repr(array_stack) == expected
# endregion
################################################################################


################################################################################
# region ArrayStack.push(stack, data)
@pytest.mark.parametrize("stack1, stack2, stack3, stack_id, data, expected", [
    ([10, 11], [20, 21], [30, 31], "stack1", 12,
     "ArrayStack(['stack1', 12, 11, 10, 'stack2', 21, 20, 'stack3', 31, 30])"),
    ([10, 11], [20, 21], [30, 31], "stack2", 22,
     "ArrayStack(['stack1', 11, 10, 'stack2', 22, 21, 20, 'stack3', 31, 30])"),
    ([10, 11], [20, 21], [30, 31], "stack3", 32,
     "ArrayStack(['stack1', 11, 10, 'stack2', 21, 20, 'stack3', 32, 31, 30])"),
])
def test_ArrayStack_push(stack1, stack2, stack3, stack_id, data, expected):
    array_stack = ArrayStack(stack1, stack2, stack3)
    array_stack.push(stack_id, data)
    assert repr(array_stack) == expected


def test_ArrayStack_push_raises():
    array_stack = ArrayStack()
    with pytest.raises(ValueError):
        array_stack.push("stack", 0)
# endregion
################################################################################


################################################################################
# region ArrayStack.pop(stack)
@pytest.mark.parametrize("stack1, stack2, stack3, stack_id, expected", [
    ([10, 11], [20, 21], [30, 31], "stack1",
     "ArrayStack(['stack1', 10, 'stack2', 21, 20, 'stack3', 31, 30])"),
    ([10, 11], [20, 21], [30, 31], "stack2",
     "ArrayStack(['stack1', 11, 10, 'stack2', 20, 'stack3', 31, 30])"),
    ([10, 11], [20, 21], [30, 31], "stack3",
     "ArrayStack(['stack1', 11, 10, 'stack2', 21, 20, 'stack3', 30])"),
])
def test_ArrayStack_pop(stack1, stack2, stack3, stack_id, expected):
    array_stack = ArrayStack(stack1, stack2, stack3)
    array_stack.pop(stack_id)
    assert repr(array_stack) == expected


def test_ArrayStack_pop_raises():
    array_stack = ArrayStack()
    with pytest.raises(ValueError):
        array_stack.pop("stack")
# endregion
################################################################################
