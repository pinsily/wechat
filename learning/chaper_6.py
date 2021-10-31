from fastapi import APIRouter, Depends, Header, HTTPException
from typing import Optional
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from starlette import status

app06 = APIRouter()

"""密码和账号换token"""

# 接受URL作为参数，验证username和password，返回token，只是指明地址
# fastapi会检查请求的AUthorization头信息，如果没有头信息，返回401状态码
oauth2_schema = OAuth2AuthorizationCodeBearer(tokenUrl="/chaper06/token", authorizationUrl="")


@app06.get("password_bearer")
async def password_bearer(token: str = Depends(oauth2_schema)):
    return {"token": token}


"""认证"""

fake_users_db = {
    "snow": {
        "username": "snow",
        "password": "snow",
        "email": "13160724868@163.com",
        "disabled": True
    }
}


def fake_hash_password(password: str):
    """伪代码加密密码"""
    return password

class User(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDb(User):
    password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDb(**user_dict)
    pass

def fake_decode_token(token: str):
    user = get_user(fake_users_db, token)
    return user

def get_current_user(token: str=Depends(oauth2_schema)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="",
            headers={"WWW-Authenticate": "Bearer"})
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="不是活跃用户")
    return current_user

@app06.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户不存在")

    user = UserInDb(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="密码错误")
    return {"access_token": user.username, "token_type": "bearer"}
