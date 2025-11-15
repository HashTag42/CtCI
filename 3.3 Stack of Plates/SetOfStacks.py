'''
# Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

## Question 3.3 Stack of Plates

Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would
likely start a new stack when the previous stack exceeds some threshold. Implement a data structure `SetOfStacks` that
mimics this. `SetOfStacks` should be composed of several stacks and should create a new stack once the previous one
exceeds capacity. `SetOfStacks.push()` and `SetOfStacks.pop()` should behave identically to a single stack (that is
`pop()` should return the same values as it would if there were just a single stack).

### FOLLOW UP
Implement a function `popAt(int index)` which performs a pop operation on a specific sub-stack.
'''
from typing import Generic, List, Optional, TypeVar
from Stack import Stack
T = TypeVar("T")

INCORRECT_CAPACITY = "Capacity must be a positive number"


class SetOfStacks(Generic[T]):
    # Constructor
    def __init__(self, capacity: int, items: Optional[List[T]] = None) -> None:
        """Initialize a SetOfStacks object."""
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError(INCORRECT_CAPACITY)
        self.stacks: List[Stack] = [Stack()]
        self.active: int = 0
        self.capacity: int = capacity
        self.push_from_list(items)

    # Interface (public methods)
    def push(self, data: T) -> None:
        """Add an item at the top of the SetOfStacks"""
        if len(self.stacks[self.active]) == self.capacity:
            self.stacks.append(Stack())
            self.active += 1
        self.stacks[self.active].push(data)

    def push_from_list(self, items: List[T]) -> None:
        """Add a list of items to the SetOfStacks"""
        if items:
            for i in items:
                self.push(i)

    def pop(self) -> Optional[T]:
        """Remove and return the data at the top of the active stack"""
        data = self.stacks[self.active].pop()
        if self.active > 0 and len(self.stacks[self.active]) == 0:
            self.stacks.pop()
            self.active -= 1
        return data

    def pop_at(self, index: int) -> Optional[T]:
        """Remove and return the data at the top of the indicated stack"""
        if 0 <= index <= self.active:
            return self.stacks[index].pop()
        else:
            raise IndexError

    def peek(self) -> Optional[T]:
        """Return the data at the top of the stack, or None if empty"""
        return self.stacks[self.active].peek()

    # Dunder methods
    def __repr__(self) -> str:
        result = f"SetOfStacks(Capacity={self.capacity}:"
        for i in range(self.active + 1):
            result += str(list(self.stacks[i]))
        result += ")"
        return result
