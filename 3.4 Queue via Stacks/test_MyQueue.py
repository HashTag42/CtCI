from MyQueue import MyQueue


################################################################################
# region MyQueue
def test_MyQueue():
    # initialize a MyQueue object
    mq = MyQueue()
    assert isinstance(mq, MyQueue)
    assert mq.is_empty() is True
    # add an item to the queue
    mq.add(1)
    assert mq.peek() == 1
    assert mq.is_empty() is False
    # add more items to the queue
    mq.add(2)
    assert mq.peek() == 2
    mq.add(3)
    assert mq.peek() == 3
    # remove an item from the queue
    assert mq.remove() == 1
    assert mq.peek() == 3
    assert mq.is_empty() is False
    assert repr(mq) == "MyQueue([3, 2])"
    # remove the next item from the queue
    assert mq.remove() == 2
    assert mq.peek() == 3
    assert mq.is_empty() is False
    assert repr(mq) == "MyQueue([3])"
    # empty the queue
    assert mq.remove() == 3
    assert mq.is_empty() is True
    assert mq.peek() is None
    assert repr(mq) == "MyQueue([])"
    assert mq.remove() is None
    assert mq.is_empty() is True
    assert mq.peek() is None
    assert repr(mq) == "MyQueue([])"
    assert mq.remove() is None
    assert mq.is_empty() is True
    assert mq.peek() is None
    assert repr(mq) == "MyQueue([])"
    # add a couple of items to the queue
    mq.add(4)
    assert repr(mq) == "MyQueue([4])"
    mq.add(5)
    assert repr(mq) == "MyQueue([5, 4])"
    # empty the queue
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
