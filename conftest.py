import pytest

from application import Application
from helper.user import UserHelper

fixture = Application()


@pytest.fixture(scope="session")
def base_fixture():
    return fixture


@pytest.fixture(scope="session")
def user(request):
    def fin():
        fixture.api.delete_user(fixture.username)

    fixture.username = UserHelper().create_user()

    request.addfinalizer(fin)
    return fixture
