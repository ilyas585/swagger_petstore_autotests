import pytest


@pytest.mark.parametrize("new_user", [True, False])
def test_positive(user, new_user):
    username = "string"

    if new_user:
        username = user.username

    response = user.api.get_user(username)
    resp_dict = response.json()

    assert response.status_code == 200, "Код ответа не соответствует ожидаемому."
    assert resp_dict["username"] == username, "поле username не соответствует ожидаемому"
