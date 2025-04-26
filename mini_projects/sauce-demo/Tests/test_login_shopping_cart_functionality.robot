*** Settings ***
Documentation    This script tests the login and shopping cart functionalities using BDD. 
...              It covers adding, replacing items in the cart, and completing the checkout process.
Library    SeleniumLibrary
Library    ScreenCapLibrary
Suite Setup    Open the Application in chrome browser    ${url}    ${browser}
#Suite Teardown    Close Browser    #keyword execute at end
Resource    ../Resources/SauceDemo.resource
Resource   ../Resources/SauceShopPage.robot
Resource   ../Resources/CartPage.robot
Resource   ../Resources/CheckoutPage.robot

*** Test Cases ***
Validate Adding items into cart
    Fill the login form    ${user}    ${pass}
    Get all the item titles in the shop page
    Add item into cart    ${backpack}
    Verify if product title and price are matching with selected items

Validate Replacing items from cart
    Remove the product from cart
    Verify that item is removed from cart
    Navigate to the shops page
    Add item into cart    ${jacket}
    Verify if product title and price are matching with selected items

Provide all information and proceed to final checkout
    Proceed to user information page
    provide user info    ${first_name_id}    ${first_name}
    provide user info    ${last_name_id}    ${last_name}
    provide user info    ${postal_code_id}    ${postal_code}
    click on continue button

Complete the purchase and log out of application
    Verify final overview page is opened
    Verify if product title and price are matching with selected items
    Complete the purchase
    Click on logout
