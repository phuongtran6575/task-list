from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from service.auth_service import get_user_by_username
from database.sqlite_database_config import SessionDepends
from models.user_models import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

@router.post("/register")
async def register(user: User, session: SessionDepends):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/user")
async def get_user( token: str = Depends(oauth2_scheme) ):
        return token

@router.post("/token")
async def login( session: SessionDepends, form_data: OAuth2PasswordRequestForm = Depends() ):   
    user = get_user_by_username(session, form_data.username)
    password = form_data.password
    if user and user.password == password:   
        return {
        "access_token": user.username,  # chỉ giả lập, thực tế nên dùng JWT
        
    }