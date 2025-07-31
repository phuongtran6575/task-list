from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from database.sqlite_database_config import SessionDepends


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer("/auth/token")

@router.get("/user")
async def get_user(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return
