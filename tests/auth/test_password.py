async def test_get_hashed_password():
    # вписать сюда готовый хэш пароля
    hashed_password = None
    assert get_hashed_password('hhdf$yerdf') == hashed_password


async def test_verify_password():
    # вписать сюда готовый хэш пароля
    hashed_password = None
    assert verify_password('hhdf$yerdf', hashed_password)
