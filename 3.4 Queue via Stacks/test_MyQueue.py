from MyQueue import MyQueue


################################################################################
# region MyQueue
def test_MyQueue():
    mq = MyQueue()
    mq.add(1)
    mq.add(2)
    mq.add(3)
    assert mq.remove() == 1
    assert repr(mq) == "MyQueue([3, 2])"
    assert mq.remove() == 2
    assert repr(mq) == "MyQueue([3])"
    assert mq.remove() == 3
    assert repr(mq) == "MyQueue([])"
    assert mq.remove() is None
    assert repr(mq) == "MyQueue([])"
    assert mq.remove() is None
    assert repr(mq) == "MyQueue([])"
    mq.add(4)
    assert repr(mq) == "MyQueue([4])"
    mq.add(5)
    assert repr(mq) == "MyQueue([5, 4])"
    assert mq.remove() == 4
    assert repr(mq) == "MyQueue([5])"
    assert mq.remove() == 5
    assert repr(mq) == "MyQueue([])"
    assert mq.remove() is None
    assert repr(mq) == "MyQueue([])"
# endregion
################################################################################


################################################################################
# region MyQueue.__init__() -> None
def test_MyQueue__init__():
    mq = MyQueue()
    assert isinstance(mq, MyQueue)
# endregion
################################################################################


################################################################################
# region MyQueue._add_(data) -> None
def test_MyQueue_add_():
    mq = MyQueue()
    mq.add(1)
    assert repr(mq) == "MyQueue([1])"
    mq.add(2)
    assert repr(mq) == "MyQueue([2, 1])"
# endregion
################################################################################


################################################################################
# region MyQueue._remove() -> data
def test_MyQueue_remove():
    mq = MyQueue()
    mq.add(1)
    mq.add(2)
    mq.add(3)
    assert mq.remove() == 1
    assert repr(mq) == "MyQueue([3, 2])"
    assert mq.remove() == 2
    assert repr(mq) == "MyQueue([3])"
    assert mq.remove() == 3
    assert repr(mq) == "MyQueue([])"
    assert mq.remove() is None
    assert repr(mq) == "MyQueue([])"
# endregion
################################################################################
