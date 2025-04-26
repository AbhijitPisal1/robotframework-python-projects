*** Settings ***
Documentation    This test validates login functionality using a data-driven approach with invalid credentials. 
...              It checks for proper error handling across multiple username and password combinations.
Library    SeleniumLibrary
Test Setup        Open the Application in chrome browser    ${URL}
Test Teardown    Close Browser    #keyword execute at end
Test Template     Validate successful login
Resource    ../Resource/reusable_keywords.resource
Resource    ../Resource/landing_page_keywords.robot

*** Test Cases ***    username    password
invalid username        hdyguhr74hr    learing
invalid password        rahulshettyacademy    75578434343
special character        shu&1    hsy@1*!                            

*** Keywords ***
Validate successful login
    [Arguments]     ${username}     ${password}
    LandingPage.User filled the login form    ${username}     ${password}
    LandingPage.wait until it checks and display error message
    LandingPage.verify if error message is correct