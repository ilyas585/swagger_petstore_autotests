import time
import pytest
import allure


def test_positive(user):
    with allure.step("Предусловие. подготовка данных."):
        new_password = user.helper.generate_password()
        username = user.username

        time.sleep(1)
        resp_prep = user.api.get_user(username)
        if resp_prep.status_code != 200:
            pytest.fail(f"не найден пользователь с username={username}")
        resp_dict = resp_prep.json()

    with allure.step("Выполнение запроса"):
        resp_dict["password"] = new_password
        response = user.api.put_user(username, resp_dict)

    with allure.step("Проверка ответа."):
        resp_get = user.api.get_user(username)
        assert response.status_code == 200, "Код ответа не соответствует ожидаемому."
        assert resp_dict["username"] == username, "поле username не соответствует ожидаемому"
        assert resp_get.json()["password"] == new_password, \
            f"password uncorrect exp={new_password}, actual={resp_get.json()['password']}"


