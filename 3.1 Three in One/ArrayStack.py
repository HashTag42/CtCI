'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 3.1 Three in One

Describe how you could use a single array to implement three stacks.
'''
from typing import Generic, List, Optional, TypeVar
T = TypeVar("T")


class ArrayStack(Generic[T]):
    """Uses an array to implement three stacks"""

    # constructor
    def __init__(self,
                 items1: Optional[List[T]] = None,
                 items2: Optional[List[T]] = None,
                 items3: Optional[List[T]] = None,
                 ):
        """Initialize ArrayStack object. Optionally populates it with a list of items."""
        self.data = list()
        self.data.append("stack1")
        self.data.append("stack2")
        self.data.append("stack3")
        if items1:
            for item in items1:
                self.data.insert(self.data.index("stack1") + 1, item)
        if items2:
            for item in items2:
                self.data.insert(self.data.index("stack2") + 1, item)
        if items3:
            for item in items3:
                self.data.insert(self.data.index("stack3") + 1, item)

    # interface
    def push(self, stack, data: T) -> None:
        """Add an item to the indicated stack"""
        if stack not in ["stack1", "stack2", "stack3"]:
            raise ValueError(f"Incorrect stack id: {stack}")
        self.data.insert(self.data.index(stack) + 1, data)

    def pop(self, stack) -> Optional[T]:
        if stack not in ["stack1", "stack2", "stack3"]:
            raise ValueError(f"Incorrect stack id: {stack}")
        popped_value = self.data[self.data.index(stack)]
        self.data.pop(self.data.index(stack) + 1)
        return popped_value

    # Dunder methods
    def __repr__(self) -> str:
        """Return a developer-friendly string representation"""
        return f"ArrayStack({self.data})"
