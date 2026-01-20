from typing import List
from beanie import Document, Link
from pydantic import Field
from models.Role import Role



class User(Document):
    username: str
    password: str
    roles: List[Role] = [Role.user]

    class Settings:
        name = "users"