import pytest

from client.petstore import ApiPetStore


api = ApiPetStore()


@pytest.mark.parametrize("username", ["wrong", "error"])
def test_positive(username):
    response = api.get_user(username)
    resp_dict = response.json()

    assert response.status_code == 404, "Код ответа не соответствует ожидаемому."
    assert resp_dict["type"] == "error", "поле type не соответствует ожидаемому"
    assert resp_dict["message"] == "User not found"
