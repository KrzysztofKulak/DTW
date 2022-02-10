import pydantic.error_wrappers
import pytest

from app.factories import DogFactory, ParentFactory
from app.models import Dog, Match, Parent


class TestDog:
    def test_dog_has_name(self):
        dog = Dog(name="Azor")
        assert dog.name == "Azor"
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            Dog()

    def test_dog_name_should_be_between_2_and_50_characters(self):
        DogFactory(name="Jo")
        DogFactory(name="F" * 50)
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            DogFactory(name="A")
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            DogFactory(name="A" * 51)


class TestParent:
    def test_parent_has_name_email_dog(self):
        dog = DogFactory()
        parent = Parent(name="Janusz", email="janusz@example.com", dog=dog)
        assert parent.name == "Janusz"
        assert parent.email == "janusz@example.com"
        assert parent.dog == dog
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            Parent()

    def test_parent_should_have_name_between_2_and_50_characters(self):
        ParentFactory(name="Su")
        ParentFactory(name="E" * 50)
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            ParentFactory(name="O")
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            ParentFactory(name="E" * 51)


class TestMatch:
    def test_match_has_two_different_dogs(self):
        one_dog = DogFactory()
        another_dog = DogFactory()
        match = Match(owner=one_dog, subject=another_dog)
        assert match.owner == one_dog
        assert match.subject == another_dog
        with pytest.raises(pydantic.error_wrappers.ValidationError):
            Match(owner=one_dog, subject=one_dog)
