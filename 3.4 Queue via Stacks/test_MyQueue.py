from MyQueue import MyQueue


################################################################################
# region MyQueue.__init__() -> None
def test_MyQueue__init__():
    mq = MyQueue()
    assert isinstance(mq, MyQueue)
# endregion
################################################################################


################################################################################
# region MyQueue.add(data) -> None
def test_MyQueue_add_():
    mq = MyQueue()
    mq.add(1)
    assert repr(mq) == "MyQueue([1])"
    mq.add(2)
    assert repr(mq) == "MyQueue([2, 1])"
# endregion
################################################################################


################################################################################
# region MyQueue.is_empty() -> bool
def test_MyQueue_is_empty():
    mq = MyQueue()
    assert mq.is_empty() is True
    mq.add(1)
    assert mq.is_empty() is False
    mq.remove()
    assert mq.is_empty() is True
# endregion
################################################################################


################################################################################
# region MyQueue.peek() -> T
def test_MyQueue_peek():
    mq = MyQueue()
    assert mq.peek() is None
    mq.add(1)
    assert mq.peek() == 1
    mq.remove()
    assert mq.peek() is None
    mq.add("A")
    assert mq.peek() == "A"
# endregion
################################################################################


################################################################################
# region MyQueue.remove() -> data
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


################################################################################
# region MyQueue
def test_MyQueue_multiple_operations():
    # initialize a MyQueue object
    mq = MyQueue()
    assert isinstance(mq, MyQueue)
    assert mq.is_empty() is True
    assert mq.peek() is None
    assert len(mq) == 0
    assert repr(mq) == "MyQueue([])"
    # add an item to the queue
    mq.add(1)
    assert mq.peek() == 1
    assert mq.is_empty() is False
    assert len(mq) == 1
    assert repr(mq) == "MyQueue([1])"
    # add another item to the queue
    mq.add(2)
    assert mq.peek() == 1
    assert mq.is_empty() is False
    assert len(mq) == 2
    assert repr(mq) == "MyQueue([2, 1])"
    # add another item to the queue
    mq.add(3)
    assert mq.peek() == 1
    assert mq.is_empty() is False
    assert len(mq) == 3
    assert repr(mq) == "MyQueue([3, 2, 1])"
    # remove an item from the queue
    assert mq.remove() == 1
    assert mq.peek() == 2
    assert mq.is_empty() is False
    assert len(mq) == 2
    assert repr(mq) == "MyQueue([3, 2])"
    # remove the next item from the queue
    assert mq.remove() == 2
    assert mq.peek() == 3
    assert mq.is_empty() is False
    assert len(mq) == 1
    assert repr(mq) == "MyQueue([3])"
    # empty the queue
    assert mq.remove() == 3
    assert mq.peek() is None
    assert mq.is_empty() is True
    assert len(mq) == 0
    assert repr(mq) == "MyQueue([])"
    # empty an empty queue
    assert mq.remove() is None
    assert mq.peek() is None
    assert mq.is_empty() is True
    assert len(mq) == 0
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
