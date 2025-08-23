*** Settings ***
Documentation    this is test 5 file

*** Variables ***
${var1}    SampleTest
*** Test Cases ***
Test case one of test file 5
    [Tags]    SIT
    Log    This is Test case one of test file 5 named ${var1}
Test case two of test file 5
    [Tags]    regression
    Log    This is Test case two of test file 5
Test case three of test file 5
    [Tags]    SIT
    Log    This is Test case three of test file 5
Test case four of test file 5
    [Tags]    smoke
    Log    This is Test case four of test file 5