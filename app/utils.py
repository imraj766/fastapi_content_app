

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password: str) -> str:
    hased_pwd = pwd_context.hash(password)
    return hased_pwd

def verify_password(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)