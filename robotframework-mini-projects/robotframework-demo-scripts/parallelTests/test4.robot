*** Settings ***
Documentation    this is test 4 file
*** Test Cases ***
Test case one of test file 4
    [Tags]    smoke    regression
    Log    This is Test case one of test file 4
Test case two of test file 4
    [Tags]    regression
    Log    This is Test case two of test file 4
Test case three of test file 4
    [Tags]    SIT
    Log   This is Test case three of test file 4
Test case four of test file 4
    [Tags]    smoke    regression
    Log    This is Test case four of test file 4