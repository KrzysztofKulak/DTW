from pydantic import (
    BaseModel,
    EmailStr,
    StrictStr,
    ValidationError,
    root_validator,
    validator,
)


def validate_name(name: str) -> str:
    if 2 <= len(name) <= 50:
        return name
    raise ValueError("username should be between 2 and 50 characters")


class Dog(BaseModel):
    name: StrictStr

    _validate_name = validator("name", allow_reuse=True)(validate_name)


class Parent(BaseModel):
    name: StrictStr
    email: EmailStr
    dog: Dog

    _validate_name = validator("name", allow_reuse=True)(validate_name)


class Match(BaseModel):
    owner: Dog
    subject: Dog

    @root_validator
    def owner_and_subject_have_to_be_different_doggos(cls, values):
        if values.get("owner") == values.get("subject"):
            raise ValidationError()
        return values
