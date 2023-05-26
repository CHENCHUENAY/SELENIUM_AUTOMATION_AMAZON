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
      

      
      

      
       
       
       
