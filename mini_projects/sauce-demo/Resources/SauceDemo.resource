*** Settings ***
Documentation    A resource file with reusable keywords and variables
Library    SeleniumLibrary
Library    OperatingSystem
Library    ScreenCapLibrary

*** Variables ***
${error_message_locator}    //div[@class="error-message-container error"]
${Item_title_locator}    //div[@data-test="inventory-item-name"]
${user}    standard_user
${Wrong_pass}    wrong_sauce1
${pass}    secret_sauce
${url}    https://www.saucedemo.com/ 
${browser}    chrome
${first_name}   mark
${last_name}    jacobs
${postal_code}    282891
${first_name_id}    first-name
${last_name_id}    last-name
${postal_code_id}    postal-code
${first_name_error}    Error: First Name is required
${last_name_error}    Error: Last Name is required
${postal_code_error}    Error: Postal Code is required
${backpack}    Sauce Labs Backpack
${jacket}    Sauce Labs Fleece Jacket

*** Keywords ***
Open the Application in chrome browser
    [Arguments]    ${url}    ${browser}
    Open Browser       ${url}    ${browser}
    Maximize Browser Window
    Take Screenshot    

Fill the login form
    [Arguments]    ${user}    ${pass}
    Input Text    //input[@id="user-name" and @name="user-name"]    ${user}
    Take Screenshot    
    Input Password    //input[@name="password" and @id="password"]    ${pass}        #secret_sauce
    Take Screenshot    
    Click Element    //input[@type="submit" and @id="login-button"]
    Sleep    1s
    Take Screenshot

Click on logout
    Click Element        //button[@id="react-burger-menu-btn"]
    Sleep    1s
    Take Screenshot
    Click Element    //a[@id="logout_sidebar_link"]
    Sleep    1s
    Take Screenshot