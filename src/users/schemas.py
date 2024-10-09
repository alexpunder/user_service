from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class MyPhone(PhoneNumber):
    pass


class BaseUser(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: MyPhone


class UserBD(BaseUser):
    user_id: int
