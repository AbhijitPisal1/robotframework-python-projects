*** Settings ***
Documentation    This test validates the login and item purchase flow in the shop module. 
...              It ensures selected products are added, verified, and successfully purchased.
Library    SeleniumLibrary
Library    Collections
Library    String
Library    ../Library/shop_library.py
Library    ../Library/test.py
Test Setup        Open the Application in chrome browser    ${URL}
#Test Teardown    Close Browser session    #keyword execute at end
Resource    ../Resource/reusable_keywords.resource
Resource    ../Resource/landing_page_keywords.robot
Resource    ../Resource/shop_page_keywords.robot

*** Test Cases ***
Login and purchase items from shop
    landing_page_keywords.User filled the login form    ${username}    ${valid_password}
    shop_page_keywords.Verify if the cart titles in the shop page    ${expectedList}
    Add Items To Cart And Checkout    ${ListOFProducts}
    shop_page_keywords.verify items in checkout page and proceed    ${ListOFProducts}
    shop_page_keywords.Click on checkout
    shop_page_keywords.Fill details in Confirmation page and purchase    ${country_name}
