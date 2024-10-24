from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    display_name: str | None
