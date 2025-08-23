*** Settings ***
Documentation    Perform data driven testing using Test template
Test Template    User Logged into the application
Resource    ../resources/basefile.resource
Resource    ../resources/dataFile.robot
Test Teardown    Close Browser

*** Test Cases ***
valid login        standard_user    secret_sauce
invalid username    wrongUser    secret_sauce
invalid password    standard_user    Wrong password

*** Keywords ***
User Logged into the application
    [Arguments]    ${user}    ${password}
    The application is opened in browser     ${url}    ${browser}
    Credentials Are Entered    ${user}    ${password}
    Login Button Is Clicked
    Verify If User Is Logged In Successfully