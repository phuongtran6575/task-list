from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, select
from models.user_models import User
from passlib.context import CryptContext
from todolist.app.database.sqlite_database_config import SessionDepends
from passlib.context import  CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_hashed_passowrd(password: str):
    return pwd_context.hash(password)

def get_user_by_username(session: Session, username: str):
    statement = select(User).where(User.username == username)
    user_db = session.exec(statement).first()
    return user_db

def authenticate_user(session: Session, username: str):
    user = get_user_by_username(session, username)
    return user