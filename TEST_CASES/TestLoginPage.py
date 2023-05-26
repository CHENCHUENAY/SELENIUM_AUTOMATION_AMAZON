import time
import conftest
import pytest
from selenium.webdriver.common.by import By

from Locators.HomePageLocators import HomePageLocators
from Locators.LoginPageLocators import LoginPageLocators
from Locators.ItemLocators import ItemLocators
from Locators.UtilitiesLocators import UtilitiesLocators




class TestLoginPage:
    @pytest.mark.usefixtures("setup_teardown")
    def test_amazon_Purchase(self,setup_teardown):
        driver = setup_teardown
        driver.implicitly_wait(10)

        driver.find_element(By.CSS_SELECTOR, value=HomePageLocators.signin_option).click()
        driver.find_element(By.CSS_SELECTOR, value=LoginPageLocators.id_).send_keys(UtilitiesLocators.useridd)
        driver.find_element(By.CSS_SELECTOR, value=LoginPageLocators.contin).click()
        driver.find_element(By.CSS_SELECTOR, value=LoginPageLocators.pw_).send_keys(UtilitiesLocators.pw)
        driver.find_element(By.CSS_SELECTOR, value=LoginPageLocators.signin).click()


        driver.find_element(By.CSS_SELECTOR, value = HomePageLocators.search_bar)\
            .send_keys(UtilitiesLocators.item_name)
        driver.find_element(By.CSS_SELECTOR,value=HomePageLocators.search_button).click()
        driver.find_element(By.XPATH, value=ItemLocators.apsara_pencil).click()
        driver.find_element(By.CSS_SELECTOR, value=UtilitiesLocators.add_to_cart).click()
        driver.find_element(By.CSS_SELECTOR,value = UtilitiesLocators.go_to_cart).click()
        driver.find_element(By.CSS_SELECTOR,value= UtilitiesLocators.checkout).click()




        time.sleep(5)
