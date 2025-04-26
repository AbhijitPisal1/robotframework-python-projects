*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    ../resources/testdata.robot

*** Keywords ***
Application is opened in browser
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --incognito
    Open Browser    ${URL}    ${browser}    options=${options} 
    Maximize Browser Window  
    Sleep    1s    
    Take Screenshot   
           
Navigate to Manager Actions
        Click Element    //button[@ng-click='manager()']
        Sleep    1s 
        Take Screenshot         
 
Proceed for Customer Login
        Click Element    //button[@ng-click='customer()']
        Sleep    1s 
        Take Screenshot         

Select the User Profile
       [Arguments]        ${fname}    ${Lname}
        Sleep    1s    
        Page Should Contain Element    //select[@id='userSelect']    
        Select From List By Label    //select[@id='userSelect']     ${fname} ${Lname} 
        Sleep    1s       
    
Log into the application
        Click element     //button[@type='submit' and contains(text(),"Login")]
        Sleep     1s
        Take screenshot
        
Check if user successfully logged in application
    [Arguments]        ${fname}    ${Lname}
    Sleep    1s    
    ${user_xpath}=    Set Variable    //span[contains(text(),"${fname} ${Lname}")]
    page should contain element    ${user_xpath}
    ${sibling_xpath}=    Set Variable    ${user_xpath}//parent::strong//parent::div//following-sibling::div
    ${Account_num}=    Get Text     ${sibling_xpath}//strong[2]
    log to console    Account number is : ${Account_num}
    ${balance_text}=    Get Text    ${sibling_xpath}//strong[2]
    ${balance}=    Convert To Number    ${balance_text}
    Set Global Variable    ${balance}  

Close the Browser
       Close Browser