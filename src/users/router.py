from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import (
    HTTP_201_CREATED, HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY
)

from src.database import get_async_session
from src.users import schemas
from src.utils.schemas import CreateScheme, OkScheme, UnpassableEntityScheme
from src.utils.responses import CreateJSONResponse

router = APIRouter(
    prefix='/api/v1/users',
    tags=['Пользователи'],
)


@router.post(
    '/sign_up',
    name='Регистрация',
    description='Добавляет пользователя в базу данных.',
    status_code=HTTP_201_CREATED,
    response_model=CreateScheme,
    responses={
        HTTP_200_OK: {
            'model': OkScheme,
            'description': 'Пользователь с такими параметрами уже существует.',
        },
        HTTP_201_CREATED: {
            'model': CreateScheme,
            'description': 'Пользователь успешно создан.',
        },
        HTTP_422_UNPROCESSABLE_ENTITY: {
            'model': UnpassableEntityScheme,
            'description': 'Ошибка валидации данных.',
        }
    }
)
async def register_user(
        user: schemas.UserCreate,

        session: AsyncSession = Depends(get_async_session)

) -> CreateScheme:
    # await create_user(session, user)
    return CreateJSONResponse
