from LinkedList import Node
from findLoop import findLoop


def test_findLoop_loop_at_head():
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")

    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE
    nodeE.next = nodeA

    assert findLoop(nodeA) == nodeA


def test_findLoop_loop_in_middle():
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")

    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE
    nodeE.next = nodeC

    assert findLoop(nodeA) == nodeC


def test_findLoop_no_loop():
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")

    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE

    assert findLoop(nodeA) is None


def test_findLoop_empty_list():
    assert findLoop(None) is None
