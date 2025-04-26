*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    testdata.robot
Resource    AddCustomerPage.robot

*** Variables ***
### define some empty variables
${fname}    ${EMPTY}
${Lname}    ${EMPTY}

*** Keywords ***
Open the Show Customer page
        Click Element    //button[@ng-click='showCust()']
        Sleep    1s 
        Take Screenshot   

Search for the customer
        Variable Should Exist    ${FName} 
        Page Should Contain Element    //input[@ng-model='searchCustomer']    
        Input Text    //input[@ng-model='searchCustomer']    ${FName}   
        Sleep    1s    
    
Check if Correct Customer is present
    Variable Should Exist    ${FName} 
    Variable Should Exist    ${LName} 
    Page Should Contain Element    //td[@class='ng-binding' and contains(text(),'${FName}')]    
    Take Screenshot    
    ${Actual_last_name}=    Get Text    //td[@class='ng-binding' and contains(text(),'${FName}')]//following-sibling::td
    Run Keyword If    '${Actual_last_name}' =='${LName}'    Log To Console    Correct user is identified    ELSE     Fail    
    Sleep    1s 
    
Delete the cutomer
    Variable Should Exist    ${FName} 
    Click Element    //td[@class='ng-binding' and contains(text(),'${FName}')]//following-sibling::td//button[@ng-click="deleteCust(cust)"] 
    Sleep    1s    
    Take Screenshot  
    Page Should Not Contain Element    //td[@class='ng-binding' and contains(text(),'${FName}')]        
    Sleep    1s 
