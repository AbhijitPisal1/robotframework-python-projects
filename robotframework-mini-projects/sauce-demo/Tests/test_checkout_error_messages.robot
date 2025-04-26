*** Settings ***
Documentation    This script validates error messages for incomplete user information during the checkout process.
...              It checks for errors when first name, last name, or postal code is missing.
Library    SeleniumLibrary
Library    ScreenCapLibrary
Suite Teardown        Close Browser    #keyword execute at end
Resource    ../Resources/SauceDemo.resource
Resource    ../Resources/SauceShopPage.robot
Resource    ../Resources/CartPage.robot
Resource    ../Resources/CheckoutPage.robot

*** Test Cases ***
Validate Adding items into cart
    Given Open the Application in chrome browser    ${url}    ${browser}
    When Fill the login form    ${user}    ${pass}
    And Get all the item titles in the shop page
    Then Add item into cart    ${backpack}

Validate error when first name is not entered in user information
    Given Proceed to user information page
    When Proceed without providing info    ${first_name_error}
    Then Navigate to initial checkout page

Validate error when last name is not entered in user information
    Given Proceed to user information page
    When provide user info    ${first_name_id}    ${first_name}
    And Proceed without providing info    ${last_name_error}
    Then Navigate to initial checkout page

Validate error when Postal code is not entered in user information
    Given Proceed to user information page
    When provide user info    ${first_name_id}    ${first_name}
    and provide user info    ${last_name_id}    ${last_name}
    And Proceed without providing info    ${postal_code_error}
    and Navigate to initial checkout page
    then Click on logout


