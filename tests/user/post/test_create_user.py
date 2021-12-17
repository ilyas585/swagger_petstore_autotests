import random
import pytest


def test_positive(base_fixture):
    # предусловие
    id = random.randint(100, 999)
    username = base_fixture.helper.generate_name("Ilyas")
    firstName = base_fixture.helper.generate_name("Ilyas")
    lastName = base_fixture.helper.generate_name("Ilyas")
    email = base_fixture.helper.generate_email("Ilyas")
    password = base_fixture.helper.generate_password()
    phone = base_fixture.helper.generate_phone()
    userStatus = 0

    # Выполнение запроса
    response = base_fixture.api.post_user(id, username, firstName, lastName, email, password, phone, userStatus)
    resp_dict = response.json()
    print(response.status_code, response.text)

    # Проверка полученных данных
    assert response.status_code == 200, "Код ответа не соответствует ожидаемому."
    assert resp_dict["message"] == str(id), f"поле message не соответствует ожидаемому, exp={id}, actual={resp_dict['message']}"

