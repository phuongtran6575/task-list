from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


@router.get("/user")
async def get_user( token: str = Depends(oauth2_scheme) ):
        return token

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    

    return {
        "access_token": form_data.username,  # chỉ giả lập, thực tế nên dùng JWT
        
    }