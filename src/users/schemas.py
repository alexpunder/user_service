from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class MyPhone(PhoneNumber):
    pass


class BaseUser(BaseModel):
    name: str
    surname: str | None
    email: EmailStr
    phone_number: MyPhone
    avatar: str | None


class UserBD(BaseUser):
    user_id: int
