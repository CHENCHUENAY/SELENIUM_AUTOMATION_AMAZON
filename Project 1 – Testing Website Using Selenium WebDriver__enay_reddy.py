import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


'''PASSED DETAILS FILLING'''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
driver.find_element(By.CSS_SELECTOR, value='[id="firstName"]').send_keys('CHENCHU')
driver.find_element(By.CSS_SELECTOR, value='[id="lastName"]').send_keys('ENAY')
driver.find_element(By.CSS_SELECTOR, value='[id="username"]').send_keys('ENAYREDDY')
time.sleep(3)
driver.quit()
print('''1-PASSED DETAILS FILLING''')


'''LOGIN_USERNAME_PASSWORD'''
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://amazon.in/")
idd = driver.find_element(By.CSS_SELECTOR, value='[data-nav-ref="nav_ya_signin"]')
idd.click()
driver.find_element(By.CSS_SELECTOR, value='[type="email"]').send_keys('chenchuenay97@gmail.com')
driver.find_element(By.CSS_SELECTOR, value='[id="continue"]').click()
driver.find_element(By.CSS_SELECTOR, value='[id="ap_password"]').send_keys('********')
driver.find_element(By.CSS_SELECTOR, value='[id="signInSubmit"]').click()
time.sleep(3)
driver.quit()
print('''2-PASSED LOGIN''')

'''PYTEST MODULE'''
@pytest.fixture()
def start_teardown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    yield driver
    time.sleep(3)
    driver.quit()

class TestProject:

    ''' passed Draggable_Slider'''
    @pytest.mark.usefixtures("start_teardown")
    def test_draggable_slider(self, start_teardown):
        driver = start_teardown
        sourse = driver.find_element(By.CSS_SELECTOR, value='[id="draggable"]')
        desti = driver.find_element(By.CSS_SELECTOR, value='[id="droppable"]')
        action = ActionChains(driver)
        action.drag_and_drop(sourse, desti).perform()
        slider = driver.find_element(By.CSS_SELECTOR, value='[class="ui-slider-handle ui-corner-all ui-state-default"]')
        action.drag_and_drop_by_offset(slider, 100, 0).perform()
        print(''' 3-passed Draggable_Slider''')

    '''passed Dropdown_Alerts'''
    @pytest.mark.usefixtures("start_teardown")
    def test_dropdown_alerts(self, start_teardown):
        driver = start_teardown
        '''Drop_Down'''
        drop_downn = Select(driver.find_element(By.NAME, value='speed'))
        drop_downn.select_by_visible_text('Medium')

        '''Alert'''
        driver.find_element(By.CSS_SELECTOR, value='[onclick="myFunction()"]').click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print('''4-passed Dropdown_Alerts''')

    '''PASSED Windows_handle'''
    @pytest.mark.usefixtures("start_teardown")
    def test_windows_handle(self, start_teardown):
        driver = start_teardown
        driver.find_element(By.XPATH, value='//*[@id="Attribution1"]/div[1]/a[2]').click()
        windows = driver.window_handles
        # print(windows)
        # print(driver.current_url)
        driver.switch_to.window(windows[1])
        # print(driver.current_url)
        driver.switch_to.window(windows[0])
        print('''5-PASSED Windows_handle''')











        # SELENIUM_AUTOMATION_AMAZON

Project Name : AMAZON_AUTOMATION
Test Senario : login and Purchace item in Amazon website
Test cases : open URL > Login > Search > Select item > Add to cart > Checkout > payment

Used Technologies :
Programming Language : Python 
Automation Tool : Selenium Webdriver 
Framework : Page Object Model


Project Summary :-
      In this Project the main agenda is to Purchsase a Product in Amazon website by Completely Automation.
Framework:
       As i used Page Object Module as a Framework ,Page Object model is an object design pattern in Selenium, where webpages are represented as classes, and the various elements on the page are defined as variables on the class. All possible user interactions can then be implemented as methods on the class:
       for that i have created indivudual Packages  like locators ,TestCases and conftect . I have inisiated Driver ,imported neecessary modules in  Conftest.py file 
       In Locators file created classes and objects which contains the necessary element Locators,utilities to access elements by webdriver Atomation
       In additionally, Test-Case file plays a Key role becoz it contains the actual scripts to execute the test-cases Automation steps.
 
Test-Case Steps :
  LOGIN -
      1. lets begin with opening the url by "driver.get('url')"
      2. click the 'sign in' button by "driver.find_element(by.xpath).click()"
      3. type 'Email' in textbox by  by "driver.find_element(by.xpath).send_keys('Email')"
      4. type 'PW' in textbox by  by "driver.find_element(by.xpath).send_keys('PW')"
      5. click the 'sign in' button by "driver.find_element(by.xpath).click()"
      
   ADDING ITEM TO CART -
      1. Search the item in textbox by "driver.find_element(by.xpath).send_keys('Item')'
      2. click the item  by "driver.find_element(by.Linked_text).click()"
      3. click the 'Add to cart ' button   by "driver.find_element(by.xpath).click()"
      
  CHECKOUT -
      1. click the ' cart ' button   by "driver.find_element(by.xpath).click()"
      2. click the 'checkout' button  by "driver.find_element(by.xpath).click()"
      3. click the 'cod' radio button by "driver.find_element(by.xpath).click()"
      4. click the 'Use thiz payment method ' button by "driver.find_element(by.xpath).click()"
      5.finally clicking 'confirm purchace' botton by "driver.find_element(by.xpath).click()"
     
     
                                      
                                                        Thanks & Regards ,
                                                            S.ENAY KUMAR.
      

      
      

      
       
       
       


