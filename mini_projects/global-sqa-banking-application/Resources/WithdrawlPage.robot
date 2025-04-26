*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    ../resources/testdata.robot

*** Keywords ***
Open the withdrawl page
    Click Element    //button[@ng-click='withdrawl()']
    Take Screenshot    
    Sleep    1s 
Customer provides the withdrawl amount
    [Arguments]    ${amount}    
    Input Text    //input[@ng-model='amount']    ${Amount} 
    Sleep    1s
    Take Screenshot
Complete the Withdrawl process
    Click Element    //button[@type='submit' and contains(text(),'Withdraw')]   
    Sleep    1s    
Check if Withdrawl was successful
    Page Should Contain Element    //span[contains(text(),'Transaction successful')]     
    Take Screenshot    