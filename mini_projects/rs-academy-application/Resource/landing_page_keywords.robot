*** Settings ***
Documentation    All the page objects and keywords of landing page
Library    SeleniumLibrary
Library    ScreenCapLibrary
Library    OperatingSystem
Library    Collections
Library    String
*** Variables ***
${error_message_locator}    css:.alert-danger
${Email}    ${EMPTY}

*** Keywords ***

User filled the login form
    [Arguments]     ${username}     ${password}
    Input Text    //input[@id="username"]    ${user_name}
    Take Screenshot    
    Input Password    //input[@id="password"]    ${password}
    Take Screenshot    
    Click Element    //input[@id="signInBtn"]
    Sleep    3s
wait until it checks and display error message
    Wait Until Element Is Visible    ${error_message_locator}
    Take Screenshot
verify if error message is correct
    Element Text Should Be    ${error_message_locator}    Incorrect username/password.

fill the login details and form
    [Arguments]     ${username}     ${password}    ${UserType}    ${value}
    Input Text    id:username    ${user_name}
    Take Screenshot
    Input Password    password    ${password}
    Click Element    //input[@value="${UserType}"]
    Wait Until Element Is Visible    css:.modal-body
    Take Screenshot
    Click Element    //button[@id="okayBtn"]
    Wait Until Element Is Not Visible    ss:.modal-body
    Select From List By Value    //select[@class="form-control"]    ${value}
    Take Screenshot
    Select Checkbox    id:terms
    Checkbox Should Be Selected    id:terms
    Take Screenshot
    Click Element    //input[@id="signInBtn"]

Select the link of child window
    Click Element    css:.blinkingText
    Sleep    5s
    Switch Window    NEW
    Element Text Should Be    CSS:h1    DOCUMENTS REQUEST
    Take Screenshot

grab the email id in the child window
    ${text}=    Get Text    css:.red
    @{words}=    Split String    ${text}    at
    ${Text_split}=    Get From List    ${words}    1
    log     ${Text_split}
    @{words_2}=    Split String    ${Text_split}
    ${Email}=    Get From List    ${words_2}    0
    Set Global Variable     ${Email}

switch to parent window and enter the email
    Switch Window    MAIN
    Title Should Be    LoginPage Practise | Rahul Shetty Academy
    Input Text    id:username    ${Email}
    Take Screenshot
    Close Browser