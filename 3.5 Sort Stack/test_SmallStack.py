from SmallStack import SmallStack
import pytest


################################################################################
# region TEST: SmallStack.__init__(nodes) -> None
@pytest.mark.parametrize("nodes, expected", [
    ([], "Stack(->[])"),
    ([1], "Stack(->[1])"),
    ([1, 2], "Stack(->[1, 2])"),
    ([2, 1, 5, 4, 3], "Stack(->[1, 2, 3, 4, 5])"),
])
def test_SmallStack__init__(nodes, expected):
    ss = SmallStack(nodes)
    assert isinstance(ss, SmallStack)
    assert str(ss) == expected
# endregion
################################################################################


################################################################################
# region TEST: SmallStack.push(data) -> None
@pytest.mark.parametrize("value, expected", [
    (1, "Stack(->[1])"),
])
def test_SmallStack_push(value, expected):
    ss = SmallStack()
    ss.push(value)
    assert str(ss) == expected
# endregion
################################################################################


################################################################################
# region TEST: SmallStack.pop() -> Optional[T]
@pytest.mark.parametrize("nodes, pop_count, expected", [
    ([1], 1, "Stack(->[])"),
    ([1, 2], 2, "Stack(->[])"),
    ([2, 1, 5, 4, 3], 3, "Stack(->[4, 5])"),
])
def test_SmallStack_pop(nodes, pop_count, expected):
    ss = SmallStack(nodes)
    for _ in range(pop_count):
        ss.pop()
    assert str(ss) == expected
# endregion
################################################################################


################################################################################
# region TEST: SmallStack.peek() -> Optional[T]
@pytest.mark.parametrize("nodes, expected", [
    ([], None),
    ([1], 1),
])
def test_SmallStack_peek(nodes, expected):
    ss = SmallStack(nodes)
    assert ss.peek() == expected
# endregion
################################################################################


################################################################################
# region TEST: SmallStack.is_empty() -> bool
@pytest.mark.parametrize("nodes, expected", [
    ([], True),
    ([1], False),
])
def test_SmallStack_is_empty(nodes, expected):
    ss = SmallStack(nodes)
    assert ss.is_empty() == expected
# endregion
################################################################################
