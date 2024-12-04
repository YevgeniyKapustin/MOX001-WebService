from sqlalchemy import Mapped

from src.database import Base
from src.utils.sql_columns import str_256, str_unique

class User(Base):
    """Модель для работы с пользователями."""
    # Authentication/authorization sensitive data
    username: Mapped[str_unique]
    email: Mapped[str_unique]
    hashed_password: Mapped[str_256]
    # Data related to display in the application
    display_name: Mapped[str]
