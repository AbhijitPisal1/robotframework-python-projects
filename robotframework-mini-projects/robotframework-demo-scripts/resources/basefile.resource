*** Settings ***
Library    SeleniumLibrary
Library    Screenshot
*** Keywords ***
The application is opened in browser
    [Arguments]    ${url}    ${browser}
    Open Browser    ${url}    ${browser}    options=add_argument("--incognito")
    Maximize Browser Window
    Sleep    3s
   Take Screenshot

Credentials are entered
    [Arguments]    ${username}    ${pass}
    Wait Until Page Contains Element    //input[@id='user-name']    3s
    Input Text    //input[@id='user-name']    ${username}
    Sleep    3s
    Wait Until Page Contains Element    //input[@id='password']    3s
    Input Password    //input[@id='password']    ${pass}
    Sleep    1s
    Take Screenshot

login button is clicked
    Click Element    //input[@name='login-button']
    Sleep    3s
    Take Screenshot

Verify if User is logged in successfully
    ${login_status}=    Run Keyword And Return Status     Wait Until Page Contains Element    //span[@data-test="title"]
    Run Keyword If    ${login_status} == True    Login Successful    ELSE    Login Failed
Login Successful
    ${page}=    Get Text    //span[@data-test="title"]
    Run Keyword If    '${page}'== 'Products'    Log To Console    The products page is displayed    ELSE    Fail
    Take Screenshot
Login Failed
    Wait Until Page Contains Element    //h3[@data-test="error"]
    ${error_message}=    Get Text    //h3[@data-test="error"]
    Log To Console    login failed with error message : ${error_message}
    Should Contain    ${error_message}    Username and password do not match
    Take Screenshot