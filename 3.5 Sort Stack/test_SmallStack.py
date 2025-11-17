from SmallStack import SmallStack
import pytest


################################################################################
# region SmallStack.__init__(nodes)
@pytest.mark.parametrize("nodes, expected", [
    ([1, 3, 2, 4], "Stack(->[1, 2, 3, 4])"),
])
def test_SmallStack__init__(nodes, expected):
    ss = SmallStack(nodes)
    assert isinstance(ss, SmallStack)
    assert str(ss) == expected
# endregion
################################################################################
