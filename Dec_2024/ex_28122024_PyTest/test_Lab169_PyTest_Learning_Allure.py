import allure
import pytest


@allure.title("verify create booking positive")
@allure.description("This is to test positive case for create booking")
@pytest.mark.positive
def test_createbooking_positive():
    print("TC01")
    # assert 5==6
    assert 5 - 5 == 5


@allure.title("verify create booking negative1")
@allure.description("This is to test negative1 case for create booking")
@pytest.mark.negative1
def test_createbooking_negative1():
    print("TC02")
    # assert 5==6
    assert 5 + 0 == 5


@allure.title("verify create booking negative2")
@allure.description("This is to test negative2 case for create booking")
@pytest.mark.negative2
def test_createbooking_negative2():
    print("TC03")
    assert 5==6
    # assert 5 + 0 == 5
