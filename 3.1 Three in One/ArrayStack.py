'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 3.1 Three in One

Describe how you could use a single array to implement three stacks.
'''
from typing import Generic, List, Optional, TypeVar
T = TypeVar("T")


class ArrayStack(Generic[T]):
    """Uses an array to implement three stacks"""

    # Constructor
    def __init__(self,
                 items0: Optional[List[T]] = None,
                 items1: Optional[List[T]] = None,
                 items2: Optional[List[T]] = None,
                 ):
        """Initialize ArrayStack object. Optionally populates it with a list of items."""
        self.data = list()
        self.sizes = [0, 0, 0]

        if items0:
            for item in items0:
                self.data.insert(self.sizes[0], item)
            self.sizes[0] += len(items0)
        if items1:
            for item in items1:
                self.data.insert(self.sizes[0] + self.sizes[1], item)
            self.sizes[1] += len(items1)
        if items2:
            for item in items2:
                self.data.insert(self.sizes[0] + self.sizes[1] + self.sizes[2], item)
            self.sizes[2] += len(items2)

    # Public interface
    def is_empty(self, stack_id) -> bool:
        self._assert_stack_id(stack_id)
        return False if self.sizes[stack_id] > 0 else True

    def peek(self, stack_id) -> Optional[T]:
        """Return the data at the top of the indicated stack"""
        self._assert_stack_id(stack_id)
        if self.sizes[stack_id] == 0:
            raise IndexError("Nothing to peek at")
        index = 0
        for i in range(stack_id):
            index += self.sizes[i]
        return self.data[index]

    def pop(self, stack_id) -> Optional[T]:
        """Remove and return the data at the top of the indicated stack"""
        self._assert_stack_id(stack_id)
        if self.sizes[stack_id] == 0:
            raise IndexError("Nothing to pop")
        index = 0
        for i in range(stack_id):
            index += self.sizes[i]
        popped_value = self.data[index]
        self.data.pop(index)
        self.sizes[stack_id] -= 1
        return popped_value

    def push(self, stack_id, data: T) -> None:
        """Add an item to the indicated stack"""
        self._assert_stack_id(stack_id)
        index = 0
        for i in range(stack_id):
            index += self.sizes[i]
        self.data.insert(index, data)
        self.sizes[stack_id] += 1

    # Private methods
    def _assert_stack_id(self, stack_id):
        if 0 <= stack_id <= 2:
            return True
        else:
            raise ValueError(f"Incorrect stack id: {stack_id}")

    # Dunder methods
    def __repr__(self) -> str:
        """Return a developer-friendly string representation"""
        stack0 = list(self.data[0:self.sizes[0]])
        stack1 = list(self.data[self.sizes[0]:self.sizes[0] + self.sizes[1]])
        stack2 = list(self.data[self.sizes[0] + self.sizes[1]:self.sizes[0] + self.sizes[1] + self.sizes[2]])
        return f"ArrayStack({stack0}, {stack1}, {stack2})"
