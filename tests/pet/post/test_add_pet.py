import pytest
import random


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_positive(base_fixture, status):
    pet_id = random.randint(10, 99)
    category = {
        "id": random.randint(10, 99),
        "name": base_fixture.helper.generate_name()
    }
    name = base_fixture.helper.generate_name()
    photoUrls = ["anyurlToImage"]
    tags = [{
        "id": random.randint(10, 99),
        "name": base_fixture.helper.generate_name()
    }]

    response = base_fixture.api.post_pet(pet_id, category, name, photoUrls, tags, status)
    print(response.status_code, response.text, sep="\n")
    resp_dict = response.json()

    # Postcondition
    resp_post = base_fixture.api.delete_pet(pet_id)
    if resp_post.status_code != 200:
        pytest.fail(f"Постусловие не выполнилось, не удалился объект с id = {pet_id}")

    assert response.status_code == 200, "Код ответа не соответствует ожидаемому."
    assert base_fixture.checker.check_post_pet(resp_dict, pet_id, category, name, photoUrls, tags, status)
    assert resp_post.json()["message"] == str(pet_id), "поле message не соответствует ожидаемому"
