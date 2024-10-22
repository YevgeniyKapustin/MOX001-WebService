from httpx import AsyncClient
from starlette.status import HTTP_200_OK, HTTP_201_CREATED


async def test_new_register(async_session: AsyncClient):
    response = await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test1',
            'email': 'dev1@test.com',
            'password': 't%&wtgdf235grdr',
        }
    )

    assert response.status_code == HTTP_201_CREATED


async def test_register_already_exist(async_session: AsyncClient):
    await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test2',
            'email': 'dev2@test.com',
            'password': 'tgre5^@#hfd',
        }
    )
    response = await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test2',
            'email': 'dev2@test.com',
            'password': 'tgre5^@#hfd',
        }
    )

    assert response.status_code == HTTP_200_OK


async def test_bad_password(async_session: AsyncClient):
    response = await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test3',
            'email': 'dev3@test.com',
            'password': 'pass',
        }
    )

    assert response.status_code == HTTP_200_OK


async def test_update_refresh_token(async_session: AsyncClient):
    await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test4',
            'email': 'dev4@test.com',
            'password': 'df&35grdr',
        }
    )

    response = await async_session.post(
        '/api/v1/token/refresh',
        data={
            'email': 'dev4@test.com',
            'password': 'df&35grdr',
        }
    )

    assert response.json.get('access_token') == access_token
    assert response.json.get('refresh_token') == refresh_token
    assert response.status_code == HTTP_200_OK


async def test_update_access_token(async_session: AsyncClient):
    await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test5',
            'email': 'dev5@test.com',
            'password': 'df&35grdr',
        }
    )
    response = await async_session.post(
        '/api/v1/token/refresh',
        data={
            'email': 'dev5@test.com',
            'password': 'df&35grdr',
        }
    )
    refresh_token = response.json.get('refresh_token')

    response = await async_session.post(
        '/api/v1/token/access',
        data={
            'refresh_token': refresh_token,
        }
    )

    assert response.json.get('access_token') == access_token
    assert response.status_code == HTTP_200_OK


async def test_verify_access_token(async_session: AsyncClient):
    await async_session.post(
        '/api/v1/auth/registration',
        json={
            'username': 'Test5',
            'email': 'dev5@test.com',
            'password': 'df&35grdr',
        }
    )
    response = await async_session.post(
        '/api/v1/token/refresh',
        data={
            'email': 'dev5@test.com',
            'password': 'df&35grdr',
        }
    )
    access_token = response.json.get('access_token')

    response = await async_session.post(
        '/api/v1/token/verify',
        headers={
            'access_token': access_token
        }
    )

    assert response.status_code == HTTP_200_OK
