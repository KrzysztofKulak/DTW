import factory

from . import models


class DogFactory(factory.Factory):
    class Meta:
        model = models.Dog

    name = factory.Sequence(lambda n: "Azor%s" % n)


class ParentFactory(factory.Factory):
    class Meta:
        model = models.Parent

    name = factory.Sequence(lambda n: "Zyzio%s" % n)
    email = factory.LazyAttribute(lambda obj: "%s@example.com" % obj.name)
    dog = factory.SubFactory(DogFactory)
