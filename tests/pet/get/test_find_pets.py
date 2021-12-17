import pytest
import allure


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_positive(base_fixture, status):
    with allure.step("Find pets by status."):
        response = base_fixture.api.get_pets_by_status(status)
        resp_dict = response.json()

    with allure.step("Проверка ответа."):
        assert response.status_code == 200, "Код ответа не соответствует ожидаемому."

        check_resp = base_fixture.checker.validate_json(resp_dict[0], "schemas/pet.json")
        assert check_resp is True, "тело ответа не соответствует схеме pet.json"
        assert base_fixture.checker.check_find_pets_by_status(resp_dict, status)
