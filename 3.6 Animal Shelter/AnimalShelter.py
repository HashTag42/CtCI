'''
Cracking the Coding Interview - 6th Edition - https://www.crackingthecodinginterview.com/

Question 3.6 Animal Shelter
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out basis". People must adopt
either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer
a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would
like. Create the data structures to maintain this system and implement operations such as `enqueue`, `dequeueAny`,
`dequeueDog`, and `dequeueCat`. You may use the built-in `LinkedList` data structure.

LinkedList is implemented at https://github.com/HashTag42/Python/blob/master/Python101/LinkedList.py
'''
from LinkedList import LinkedList
from typing import List, Optional
from enum import Enum
import time


class AnimalType(Enum):
    CAT = 1
    DOG = 2


class Animal():
    def __init__(self, type: AnimalType, name: str) -> None:
        self.type: AnimalType = type
        self.time_admitted = time.time()
        self.name: str = name

    def __str__(self) -> str:
        result: str = "("
        match self.type:
            case AnimalType.CAT:
                result += "CAT"
            case AnimalType.DOG:
                result += "DOG"
            case _:
                result += "UNKNOWN"
        result += f":{self.name})"
        return result


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(AnimalType.CAT, name)


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(AnimalType.DOG, name)


class AnimalShelter(LinkedList):
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, animals: Optional[List[Animal]] = None) -> None:
        super().__init__(animals)
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def enqueue(self, animal: Animal):
        self.append(animal)

    def dequeueAny(self) -> Animal:
        return super().pop_head()

    def dequeueCat(self) -> Cat:
        return self._dequeueAnimal(AnimalType.CAT)

    def dequeueDog(self) -> Dog:
        return self._dequeueAnimal(AnimalType.DOG)
    # endregion
    ################################################################################

    ################################################################################
    # region PRIVATE INTERFACE
    def _dequeueAnimal(self, animal_type: AnimalType) -> Animal:
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data.type == animal_type:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next is None:
                    self.tail = previous_node
                return current_node.data
            previous_node = current_node
            current_node = current_node.next
        return None
    # endregion
    ################################################################################
