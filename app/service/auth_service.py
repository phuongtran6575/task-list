from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import select
from models.user_models import User
from passlib.context import CryptContext
from todolist.app.database.sqlite_database_config import SessionDepends

def get_user_by_username(session: SessionDepends, username: str):
    statement = select(User).where(User.username == username)
    user_data = session.exec(statement).first()
    if user_data:
        return 