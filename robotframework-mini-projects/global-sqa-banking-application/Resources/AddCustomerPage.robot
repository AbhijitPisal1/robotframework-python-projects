*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    ../resources/testdata.robot

*** Keywords ***

Open the Add Customer Form
        Click Element    //button[@ng-click='addCust()']
        Take Screenshot    
        Sleep    1s 
        
Provide Customer Details 
        ${i}=  Evaluate    random.choice(range(100,2000))    random
        ${j}=  Evaluate    random.choice(range(500,1000))    random
        ${k}=  Evaluate    random.choice(range(100000,900000))    random
        Set Global Variable    ${FName}    Automation_${i}
        Set Global Variable    ${LName}    Tester_${j}
        Set Global Variable    ${PinCode}    ${k}
        Sleep    1s 
        Input Text    //input[@ng-model='fName']    ${FName}    
        Input Text    //input[@ng-model='lName']    ${LName}    
        Input Text    //input[@ng-model='postCd']    ${PinCode} 
        Sleep    1s   
        Take Screenshot     
      
Complete Adding New customer
        Sleep    1s    
        Click Element    //button[@type='submit']
        Sleep    1s    
        Take Screenshot    
       
Confirm if new customer added
        ${message} =    Handle Alert    ACCEPT
       Should Contain    ${message}   Customer added successfully              

