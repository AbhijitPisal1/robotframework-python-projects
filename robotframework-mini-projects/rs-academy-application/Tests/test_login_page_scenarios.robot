*** Settings ***
Documentation    This test validates various login page scenarios including unsuccessful login, 
...              navigating through forms, and handling child window interactions.
Library    SeleniumLibrary
Library    Collections
Library    String
Test Setup        Open the Application in chrome browser    ${URL}
Test Teardown    Close Browser session    #keyword execute at end
Resource    ../Resource/reusable_keywords.resource
Resource    ../Resource/landing_page_keywords.robot

*** Test Cases ***
Validate unsuccessful login
    [Tags]    SMOKE
    LandingPage.User filled the login form    ${username}     ${invalid_password}
    LandingPage.wait until it checks and display error message
    LandingPage.verify if error message is correct

Select the form and navigate to child window
    [Tags]    SMOKE
    LandingPage.fill the login details and form    ${username}    ${valid_password}    ${user}    ${Teacher}

validate child window functionality
    [Tags]    SMOKE
    Select the link of child window
    grab the email id in the child window
    switch to parent window and enter the email
