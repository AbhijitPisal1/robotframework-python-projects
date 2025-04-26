*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    ../resources/testdata.robot

*** Keywords ***
Open the transactions page
    Click Element    //button[@ng-click='transactions()']
    Take Screenshot    
    Sleep    1s 
Verify that Credited amount is correct
    [Arguments]    ${Amt}
    Set Global Variable    ${Amt}    
    Page Should Contain Element    //td[@class="ng-binding" and contains(text(),'Credit')]    
    ${amt_in_table}=    get text       //td[@class="ng-binding" and contains(text(),'Credit')]//preceding-sibling::td[1]
    log to console        ${amt_in_table}
    ${amt_table}=    Convert To Number    ${amt_in_table}
    Should Be Equal As Numbers    ${amt_table}    ${Amt}
    Take Screenshot    
Navigate back to main customer page
    Click Element    //button[@ng-click='back()']
    Sleep    1s    
    Take Screenshot 
Verify that Withdrawn amount is correct
    [Arguments]    ${Amt}
    Set Global Variable    ${Amt}    
    Page Should Contain Element    //td[@class="ng-binding" and contains(text(),'Debit')]    
    ${amt_in_table}=    get text       //td[@class="ng-binding" and contains(text(),'Debit')]//preceding-sibling::td[1]
    log to console        ${amt_in_table}
    ${amt_table}=    Convert To Number    ${amt_in_table}
    Should Be Equal As Numbers    ${amt_table}    ${Amt}
    Take Screenshot        
Customer Logged out
    Click Element    //button[contains(text(),'Logout')]
    Take Screenshot        