*** Settings ***
Documentation    This script tests the unsuccessful login scenario using BDD. 
...              It verifies that an appropriate error message is displayed for invalid credentials.
Library    SeleniumLibrary
Library    ScreenCapLibrary
Test Setup    Open the Application in chrome browser    ${url}    ${browser}
Test Teardown    Close Browser    #keyword execute at end
Resource    ../Resources/SauceDemo.resource

*** Test Cases ***
Validate unsuccessful login
    Fill the login form    ${user}    ${Wrong_pass}
    wait until it checks and display error message
    verify if error message is correct

*** Keywords ***
wait until it checks and display error message
    Wait Until Element Is Visible    ${error_message_locator}
    Take Screenshot
verify if error message is correct
#    ${result}=    Get Text    ${error_message_locator}
#    Should Be Equal As Strings    ${result}    Epic sadface: Username and password do not match any user in this service
    #Alternatively
    Element Text Should Be    ${error_message_locator}    Epic sadface: Username and password do not match any user in this service
