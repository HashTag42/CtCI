'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 3.4 Queue via Stacks

Implement a MyQueue class which implements a queue using two stacks.
'''
from Stack import Stack
from typing import Generic, TypeVar
T = TypeVar("T")


class MyQueue(Generic[T]):
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self) -> None:
        """Initialize a MyQueue object"""
        self._stacks = [Stack(), Stack()]
        self._active = 0
        self._inactive = 1
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def add(self, data: T) -> None:
        """Add an item to the end of the queue"""
        self._stacks[self._active].push(data)

    def remove(self) -> T:
        """Remove and return the first item in the queue. Return None if the queue is empty"""
        if len(self) == 0:
            return None
        items = list(self._stacks[self._active])
        items.reverse()
        data = items[0]
        for i in range(1, len(items)):
            self._stacks[self._inactive].push(items[i])
        self._stacks[self._active].clear()
        self._switch_stacks()
        return data
    # endregion
    ################################################################################

    ################################################################################
    # region PRIVATE INTERFACE
    def _switch_stacks(self):
        """Switches the active and inactive stacks"""
        if self._active == 0:
            self._active = 1
            self._inactive = 0
        else:
            self._active = 0
            self._inactive = 1
    # endregion
    ################################################################################

    ################################################################################
    # region DUNDER METHODS
    def __len__(self) -> int:
        """Return the number of items in the queue"""
        return len(self._stacks[self._active])

    def __repr__(self) -> str:
        """Return a developer-friendly string representation"""
        return f"MyQueue({str(list(self._stacks[self._active]))})"
    # endregion
    ################################################################################
