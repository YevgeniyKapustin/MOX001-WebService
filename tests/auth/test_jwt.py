async def test_create_access_token():
    user_json = {
        'name': 'developer',
        'email': 'email@test.com'
    }
    # вписать сюда готовый jwt
    ready_jwt = ''
    assert create_access_token(user_json) == ready_jwt


async def test_create_refresh_token():
    user_json = {
        'name': 'developer',
        'email': 'email@test.com'
    }
    # вписать сюда готовый jwt
    ready_jwt = ''
    assert create_refresh_token(user_json) == ready_jwt
