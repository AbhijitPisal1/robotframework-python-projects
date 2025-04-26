*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    testdata.robot

*** Variables ***
### define some empty variables
${balance}    ${EMPTY}
${Amount}    ${EMPTY}

*** Keywords *** 
  
Open the Add deposit Form
    Click Element    //button[@ng-click='deposit()']
    Take Screenshot    
    Sleep    1s 
Customer provides the amount
    [Arguments]    ${Amount}
    Set Global Variable    ${Amount}    
    Input Text    //input[@ng-model='amount']    ${Amount} 
    Sleep    1s
    Take Screenshot    
Complete the deposit process
    Click Element    //button[@type='submit' and contains(text(),'Deposit')]   
    Sleep    1s    
Deposit was successful
    Page Should Contain Element    //span[contains(text(),'Deposit Successful')]     
    Take Screenshot    
Check if balance is updated correctly
    Variable Should Exist    ${balance}    
    ${expected_balance}=    Evaluate    ${balance} + ${Amount}
    ${updated_balance_text}=    Get Text    //div[@ng-hide='noAccount']//strong[2]
    ${updated_balance}=    Convert To Number    ${updated_balance_text}
    Should Be Equal As Numbers    ${updated_balance}    ${expected_balance}
    ${balance}=    Set Variable    ${updated_balance_text}