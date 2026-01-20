from fastapi import Request, Response
from models.Role import Role
from models.User import User
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError
from config import settings

def getAccessToken(id, roles):
    to_encode = {"id": str(id),
                 "roles": roles}
    expire = datetime.now(timezone.utc) + timedelta(hours=24)
    to_encode.update({"exp": expire})
    print(to_encode)
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


class authController:
    async def registration(self, user_data: dict):
        try:
            candidate = await User.find_one(User.username == user_data['username'])
            if candidate:
                raise 'Такой пользователь уже есть'
            new_pass_hash = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())
            new_user = User(
                username =  user_data['username'],
                password = new_pass_hash.decode('utf-8')
            )
            await new_user.insert()
            return {'message': "Успех"}
        except Exception as e:
            return {'error': e}

    async def login(self, user_data: dict):
            candidate = await User.find_one(User.username == user_data['username'])
            if not candidate:
                raise 'гуляй'
            valid = bcrypt.checkpw(user_data['password'].encode('utf-8'), candidate.password.encode('utf-8'))
            if not valid:
                raise 'гуляй'

            token = getAccessToken(candidate.id, candidate.roles)
            return {
                "access_token": token,
                "token_type": "bearer"
            }

    async def getAll(self):
        users = await User.find().to_list()
        return users