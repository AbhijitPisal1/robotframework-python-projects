*** Settings ***
Documentation    This test will perfrom data driven testing using template format
Test Teardown    Close Browser
Resource    ../resources/basefile.resource
Resource    ../resources/dataFile.robot
*** Test Cases ***
Validation of Login
    [Template]    User Logged into the application
    standard_user    secret_sauce
    wrongUser    secret_sauce
    standard_user    Wrong password
    
*** Keywords ***
User Logged into the application
    [Arguments]    ${user}    ${password}
    The application is opened in browser     ${url}    ${browser}
    Credentials Are Entered    ${user}    ${password}
    Login Button Is Clicked
    Verify If User Is Logged In Successfully