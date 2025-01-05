import pytest
import allure
import requests


@allure.title("TC01- Verify 2-2==0")
@allure.description("This is basic Math Test")
@pytest.mark.smoke
def test_basic_math_test():
    assert 2 - 2 == 0


@allure.title("TC02 - Verify 3-3==0")
@allure.description("This is another test")
@pytest.mark.regression
def test_Sub1():
    assert 3 - 3 == 0


@allure.title("TC03 - Verify 5-5==0")
@allure.description("This is another test")
@pytest.mark.smoke
def test_Sub2():
    assert 5 - 5 == 0