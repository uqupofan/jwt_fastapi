from beanie import Document
from pydantic import Field
from enum import Enum

class Role(str, Enum):
    user = 'USER'
    admin = 'ADMIN'

    class Settings:
        name = "roles"