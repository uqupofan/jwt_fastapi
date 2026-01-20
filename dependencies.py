from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from config import settings
from models.User import User

# Эта штука скажет Swagger UI, что у нас есть авторизация, и нарисует замочек 🔒
# tokenUrl="auth/login" - ссылка на вашу ручку логина
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def proverka_token(token: str = Depends(oauth2_scheme)):
    try:
        jwt_de = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        user_key = jwt_de.get('id')
        if user_key is None:
            raise 'Плохо'
    except:
        return 0
    user_date = await User.get(user_key)
    if user_date is None:
        raise "Дела плохи"
    return user_date