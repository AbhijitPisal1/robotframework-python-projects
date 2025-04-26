*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    Data.robot
Resource    common_base_Level.robot

*** Keywords ***
User logged in the application
    Application is opened in browser
    User provides the user credentials
    User proceeds with login
    
Application is opened in browser             
    Application was opened in browser    ${URL}    ${browser}
    Take Screenshot    
    
User provides the user credentials
    User provided the user credentials    ${username}    ${pass}
    Take Screenshot
     
User proceeds with login
    User proceeded with login  
    Take Screenshot 

Verify if user successfully logged in application
    Verified if user successfully logged in application
    Take Screenshot   
    
Close the browser session
    User Closed the browser
    
    
Select the Mobile Category as ${String}
    Selected the Mobile Category as ${String}
    Take Screenshot

Verify that only mobiles with text ${expected_text} are displayed
    Verified that only mobiles with text ${expected_text} are displayed
    Take Screenshot
    
Unselect the category
    Unselected the category
    Take Screenshot
    
The ascending & descending orders of items displayed are taken 
    Got the orders of items displayed 
    Take Screenshot
    
Sort the products as per ${sort_order} option
    Sorted the products as per ${sort_order} option
    Take Screenshot
    
Verify That the products are sorted as per the sort order ${sort_order}
    Verified That the products are sorted as per the sort order ${sort_order}
    Take Screenshot

Select the mobile with name ${mobile_name}
    Selected the mobile with name ${mobile_name}
    Take Screenshot
    
Verify if correct Item is added
    Verified if correct Item is added
    Take Screenshot
    
Proceed for checkout
    Proceeded for checkout
    Take Screenshot

Enter User Details and Address    
    Entered User Details and Address    ${fName}        ${LName}     ${Address}     ${province}    ${Pin}
    Take Screenshot

Click on Submit Buton
    Clicked on Submit Buton
    Take Screenshot
    
Verify if Correct Product order is place successfully
    Verified if Correct Product order is place successfully
    Take Screenshot