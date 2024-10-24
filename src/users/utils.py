from passlib.context import CryptContext


password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет соответствие пароля хэшированному паролю."""
    return password_context.verify(plain_password, hashed_password)


async def get_string_hash(string: str) -> str:
    """Возвращает хэш от строки."""
    return password_context.hash(string)
