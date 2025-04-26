*** Settings ***
Documentation    Shop Page keywords
Library    SeleniumLibrary
Library    ScreenCapLibrary
Library    Collections
Library    String

*** Keywords ***
Proceed without providing info
    [Arguments]    ${expected_error}
    click on continue button
    ${Error_message}=    Get Text    //h3[@data-test="error"]
    Should Be Equal As Strings    ${Error_message}    ${expected_error}
    RETURN   ${Error_message}

click on continue button
    Click Element    //input[@id="continue"]

Provide user info
    [Arguments]    ${id}    ${value}
    Input Text    //input[@id="${id}"]    ${value}

Navigate to initial checkout page
    Click Element    //button[@id="cancel"]
    Sleep    1s
    Take Screenshot

Verify final overview page is opened
    Page Should Contain    Checkout: Overview
    Sleep    1s

Complete the purchase
    Scroll Element Into View    //button[@id="finish"]
    Take Screenshot
    Click Element    //button[@id="finish"]
    ${final_message}=     Get Text    //h2[@data-test="complete-header"]
    Run Keyword If    '${final_message}' == 'Thank you for your order!'    Log To Console    order placed successfully    ELSE    Fail
    Take Screenshot