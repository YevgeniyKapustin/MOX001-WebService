from passlib.context import CryptContext


password_context = CryptContext(
    schemes=["sha256_crypt"],
    deprecated="auto"
)


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Checks if the password matches the encrypted password."""
    return password_context.verify(plain_password, hashed_password)


async def get_password_hash(plain_password: str) -> str:
    """Returns a hash of the plain password."""
    return password_context.hash(plain_password)
