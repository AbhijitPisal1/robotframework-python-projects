*** Settings ***
#Configure libraries, test setups, and teardown operations
Library    SeleniumLibrary
Library    OperatingSystem
Suite Setup    Setup Suite
Suite Teardown    Teardown Suite
Test Setup    Setup Test
Test Teardown    Teardown Test

*** Variables ***
#Store reusable values to make scripts more flexible and maintainable
${URL}    https://www.saucedemo.com/
${BROWSER}    Chrome
${TIMEOUT}    10s
${user}    standard_user
${Wrong_pass}    wrong_sauce1
${password}    secret_sauce

*** Test Cases ***
#Define the individual tests, the actions to perform, and the expected outcomes.
# Define the BDD scenarios here using Given, When, Then steps.
Test Valid Login
    [Documentation]    This test case is for testing a valid login scenario
    When Input Credentials    ${user}    ${password}
    And Submit Login Form
    Then Verify Login Success

Test Invalid Login
    [Documentation]    This test case is for testing an invalid login scenario
    When Input Credentials    ${user}    ${Wrong_pass}
    And Submit Login Form
    Then Verify Login Failure

*** Keywords ***
# Define custom reusable actions or steps which map directly to Given, When, Then in gherkin syntax
# help in making test scripts modular, more readable, and reusable
# can accept arguments to make them more flexible
# help reduce duplication by enabling reusable test steps across multiple test cases
Setup Suite
    [Documentation]    This keyword runs before the test suite starts
    Log    Suite Setup Started

Teardown Suite
    [Documentation]    This keyword runs after the test suite ends
    Log    Suite Teardown Completed

Setup Test
    [Documentation]    This keyword runs before each test case
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep        ${TIMEOUT}

Teardown Test
    [Documentation]    This keyword runs after each test case
    Close Browser

Input Credentials
    [Arguments]    ${username}    ${password}
    [Documentation]    Inputs the given username and password into the login form
    Input Text    //input[@id="user-name"]    ${username}
    Log    ${username}
    Input Text    //input[@name="password"]   ${password}
    Log    ${password}

Submit Login Form
    [Documentation]    Submits the login form
    Click Button    //input[@id="login-button"]

Verify Login Success
    [Documentation]    Verifies the login is successful by checking for a
    Wait Until Element Is Visible    //span[contains(text(),"Products")]   ${TIMEOUT}

Verify Login Failure
    [Documentation]    Verifies the login failed by checking for an error message
    Sleep    ${TIMEOUT}
    Page Should Contain    Epic sadface

