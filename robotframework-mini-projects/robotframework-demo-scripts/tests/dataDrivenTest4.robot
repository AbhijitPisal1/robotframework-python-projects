*** Settings ***
Documentation    Perform data driven testing by fetching data from csv file
#Library    DataDriver   file:resources/externaldata.csv
Library    DataDriver    file=../resources/externaldata.csv    encoding=utf_8    dialect=unix
Test Template    User Logged into the application
Resource    ../resources/basefile.resource
Resource    ../resources/dataFile.robot
Test Teardown    Close Browser

*** Test Cases ***
user is logged in the application using ${username} and ${password}    Default    Default

*** Keywords ***
User Logged into the application
    [Arguments]    ${username}   ${password}
    The application is opened in browser     ${url}    ${browser}
    Credentials Are Entered    ${username}    ${password}
    Login Button Is Clicked
    Verify If User Is Logged In Successfully