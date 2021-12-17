import pytest


def test2_positive(user):
    username = "string"

    response = user.api.delete_user(username)
    resp_dict = response.json()

    assert response.status_code == 200, "Код ответа не соответствует ожидаемому."
    assert resp_dict["message"] == username, "поле username не соответствует ожидаемому"
