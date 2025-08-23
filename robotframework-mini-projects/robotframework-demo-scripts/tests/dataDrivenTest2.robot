*** Settings ***
Documentation    Perform data driven test using for loop for different data sets
Test Teardown    Close Browser
Resource    ../resources/basefile.resource
Resource    ../resources/dataFile.robot
*** Test Cases ***
login with different data sets
    :FOR    ${user}    ${password}    IN
    ...    standard_user    secret_sauce
    ...    wrongUser    secret_sauce
    ...    standard_user    Wrong password
    \    User Logged Into The Application    ${user}    ${password}

*** Keywords ***
User Logged into the application
    [Arguments]    ${user}    ${password}
    The application is opened in browser     ${url}    ${browser}
    Credentials Are Entered    ${user}    ${password}
    Login Button Is Clicked
    Verify If User Is Logged In Successfully