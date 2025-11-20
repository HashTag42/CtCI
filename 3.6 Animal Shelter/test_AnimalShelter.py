from AnimalShelter import Animal, AnimalShelter, AnimalType, Cat, Dog
import pytest


################################################################################
# region Animal
def test_Animal__init():
    animal = Animal(AnimalType.CAT, "FIFI")
    assert isinstance(animal, Animal)


@pytest.mark.parametrize("type, name, expected", [
    (AnimalType.CAT, "Cat1", "(CAT:Cat1)"),
    (AnimalType.DOG, "Dog1", "(DOG:Dog1)"),
    (None, "Bird1", "(UNKNOWN:Bird1)"),
])
def test_Animal__str__(type, name, expected):
    animal = Animal(type, name)
    assert str(animal) == expected
# endregion
################################################################################


################################################################################
# region Cat
def test_Cat__init__():
    cat = Cat("FIFI")
    assert isinstance(cat, Cat)


def test_Cat__str__():
    cat = Cat("FIFI")
    assert str(cat) == "(CAT:FIFI)"
# endregion
################################################################################


################################################################################
# region Dog
def test_Dog__init__():
    dog = Dog("FIFI")
    assert isinstance(dog, Dog)


def test_Dog__str__():
    dog = Dog("FIFI")
    assert str(dog) == "(DOG:FIFI)"
# endregion
################################################################################


################################################################################
# region AnimalShelter
def test_AnimalShelter__init__():
    shelter = AnimalShelter()
    assert isinstance(shelter, AnimalShelter)


@pytest.mark.parametrize("animals, expected", [
    ([], ""),
    ([Cat("Cat1")], "(CAT:Cat1)"),
    ([Cat("Cat1"), Dog("Dog1")], "(CAT:Cat1) -> (DOG:Dog1)"),
    ([Cat("Cat1"), Dog("Dog1"), Dog("Dog2"), Cat("Cat2")], "(CAT:Cat1) -> (DOG:Dog1) -> (DOG:Dog2) -> (CAT:Cat2)"),
])
def test_AnimalShelter__init__with_animals(animals, expected):
    shelter = AnimalShelter(animals)
    assert str(shelter) == expected


def test_AnimalShelter_enqueue():
    shelter = AnimalShelter()
    animals = [Cat("Cat1"), Dog("Dog1"), Dog("Dog2"), Cat("Cat2")]
    for animal in animals:
        shelter.enqueue(animal)
    assert str(shelter) == "(CAT:Cat1) -> (DOG:Dog1) -> (DOG:Dog2) -> (CAT:Cat2)"


def test_AnimalShelter_dequeueAny():
    shelter = AnimalShelter([Cat("Cat1"), Dog("Dog1"), Dog("Dog2"), Cat("Cat2")])
    shelter.dequeueAny()
    assert str(shelter) == "(DOG:Dog1) -> (DOG:Dog2) -> (CAT:Cat2)"


def test_AnimalShelter_dequeueCat():
    shelter = AnimalShelter([Cat("Cat1"), Dog("Dog1"), Dog("Dog2"), Cat("Cat2")])
    shelter.dequeueCat()
    assert str(shelter) == "(DOG:Dog1) -> (DOG:Dog2) -> (CAT:Cat2)"


def test_AnimalShelter_dequeueDog():
    shelter = AnimalShelter([Cat("Cat1"), Dog("Dog1"), Dog("Dog2"), Cat("Cat2")])
    shelter.dequeueDog()
    assert str(shelter) == "(CAT:Cat1) -> (DOG:Dog2) -> (CAT:Cat2)"


def test_AnimalShelter_dequeue_all():
    shelter = AnimalShelter([Cat("Cat1"), Dog("Dog1"), Dog("Dog2"), Cat("Cat2")])
    shelter.dequeueDog()
    assert str(shelter) == "(CAT:Cat1) -> (DOG:Dog2) -> (CAT:Cat2)"
    shelter.dequeueAny()
    assert str(shelter) == "(DOG:Dog2) -> (CAT:Cat2)"
    shelter.dequeueCat()
    assert str(shelter) == "(DOG:Dog2)"
    shelter.dequeueCat()
    assert str(shelter) == "(DOG:Dog2)"
    shelter.dequeueDog()
    assert str(shelter) == ""
# endregion
################################################################################
