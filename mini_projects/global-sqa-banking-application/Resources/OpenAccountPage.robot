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

Open the Open Account Form
        Click Element    //button[@ng-click='openAccount()']
        Sleep    1s 
        Take Screenshot    
        
Select the Customer Profile
        Variable Should Exist    ${FName}   
        Variable Should Exist    ${LName} 
        Sleep    1s    
        Page Should Contain Element   //select[@id='userSelect']
        Select From List By Label    //select[@id='userSelect']     ${FName} ${LName} 
        Sleep    1s 
        Take Screenshot
Select Currency for Account
        Page Should Contain Element    //select[@id='currency']
        Select From List By Value   //select[@id='currency']     ${currency}
        Sleep    1s 
        Take Screenshot
       
Complete the Account Creation Process
        Click Element    //button[@type='submit']
        Sleep    1s        
Confirm if new Account is created
        ${message} =    Handle Alert    ACCEPT
       Should Contain    ${message}   Account created successfully  
       Sleep    1s             

