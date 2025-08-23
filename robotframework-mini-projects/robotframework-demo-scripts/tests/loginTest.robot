*** Settings ***
Documentation    this will test positive and negative scenarios for login functionality
Resource    ../resources/basefile.resource
Resource    ../resources/dataFile.robot
*** Test Cases ***
Log into the application
    [Tags]    Smoke
    Given The application is opened in browser    ${url}    ${browser}
    When Credentials are entered    ${username}    ${pass}
    And login button is clicked    
    Then Verify if User is logged in successfully


