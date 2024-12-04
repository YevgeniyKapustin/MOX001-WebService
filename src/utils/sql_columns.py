from typing import Annotated

from sqlalchemy.orm import mapped_column
from sqlalchemy_utils import EmailType


str_256 = Annotated[str, 256]
str_unique = Annotated[str, mapped_column(unique=True)]
email = Annotated[EmailType, mapped_column(unique=True)]
