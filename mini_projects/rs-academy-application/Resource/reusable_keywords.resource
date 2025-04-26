*** Settings ***
Documentation    A resource file with reusable keywords and variables
Library    SeleniumLibrary
Library    OperatingSystem
Library    ScreenCapLibrary

*** Variables ***
${invalid_password}    12345
${URL}    https://rahulshettyacademy.com/loginpagePractise/
${username}    rahulshettyacademy
${Valid_password}    learning
${Student}    stud
${Teacher}    teach
${user}    user
@{ListOFProducts}    Nokia Edge    Blackberry
${country_name}    India
@{expectedList}    iphone X    Samsung Note 8    Nokia Edge    Blackberry

*** Keywords ***
Open the Application in chrome browser
    [Arguments]    ${URL}
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Take Screenshot    

Close Browser session
    Close Browser

Check for Alert and Handle if present
    ${Alert-status}=     Run Keyword And Return Status    Alert Should Be Present    10s
    Take Screenshot
    Run Keyword If    '${Alert-status}'=='True'    Handle Alert    ACCEPT    ELSE    Sleep    1s
