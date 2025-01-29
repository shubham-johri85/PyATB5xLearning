import pytest


@pytest.fixture()
def create_token():
    return "ABC"


@pytest.fixture()
def create_booking():
    return 123


def test_Update(create_token, create_booking):
    print(create_token)
    print(create_booking)
