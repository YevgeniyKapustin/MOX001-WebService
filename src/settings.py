from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Конфиг приложения."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.POSTGRES_URL: str = self.__get_postgres_dsn('async_fallback=True')
        print(self.POSTGRES_URL)

    # APP
    APP_TITLE: str

    # Postgres
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_URL: str | None = None

    # JWT
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    JWT_REFRESH_SECRET_KEY: str

    # CORS
    ORIGINS: list[str]

    def __get_postgres_dsn(self, query: str | None = None) -> str:
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
            query=query
        )

    # def __get_postgres_dsn(self) -> str:
    #     return (
    #         f'postgresql+asyncpg://'
    #         f'{self.POSTGRES_USER}:'
    #         f'{self.POSTGRES_PASSWORD}@'
    #         f'{self.POSTGRES_HOST}/'
    #         f'{self.POSTGRES_DB}'
    #     )

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'


settings = Settings()

