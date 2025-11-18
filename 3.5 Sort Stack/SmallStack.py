'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 3.5 Sort Stack
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but
you may not copy the elements into any other data structure (such as an array). The stack supports the following
operations: `push`, `pop`, `peek`, and `isEmpty`.

Implementation relies on the Stack class: https://github.com/HashTag42/Python/blob/master/Python101/Stack.py
'''

from Stack import Stack
from typing import Generic, List, Optional, TypeVar
T = TypeVar("T")


class SmallStack(Stack, Generic[T]):
    """SmallStack keeps the stack sorted with the smallest items on top"""

    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, nodes: Optional[List[T]] = None) -> None:
        """Initializes a SmallStack object. Optionally populates it with a list of items."""
        super().__init__()
        if nodes:
            for val in nodes:
                super().push(val)
        self._sort()
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def push(self, data: T) -> None:
        super().push(data)
        self._sort()

    # pop(), peek(), and is_empty() are implemented by the superclass

    # endregion
    ################################################################################

    ################################################################################
    # region PRIVATE INTERFACE
    def _sort(self):
        """Sort stack items with smallest on top"""
        temp_stack: Stack = Stack()
        while not self.is_empty():
            temp_value: T = self.pop()
            while not temp_stack.is_empty() and temp_stack.peek() > temp_value:
                super().push(temp_stack.pop())
            temp_stack.push(temp_value)
        while not temp_stack.is_empty():
            super().push(temp_stack.pop())
    # endregion
    ################################################################################
