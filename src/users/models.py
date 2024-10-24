from sqlalchemy import Column, String

from src.database import Base


class User(Base):
    """Модель для работы с пользователями."""
    # Важные для аутентификации/авторизации данные
    username: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, nullable=False, unique=True)
    hashed_password: str = Column(String(length=1024), nullable=False)
    # Данные связанные с отображением в приложении
    display_name: str = Column(String, nullable=True)
