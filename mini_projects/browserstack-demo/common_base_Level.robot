*** Settings ***
Library    SeleniumLibrary
Library    ScreenCapLibrary
Library    Collections
Library    String
*** Variables ***
### initialize the variables as Empty ###
### The values will be later updated within script and set as Global variable ###
${user}    ${EMPTY}
${Category_locator}    ${EMPTY}
${asc_sorted}    ${EMPTY}   
${desc_sorted}    ${EMPTY}
${mobile_locator}    ${EMPTY}
${Name}    ${EMPTY}

*** Keywords ***
Application was opened in browser
    [Arguments]       ${URL}    ${browser} 
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_argument    --incognito
    # Call Method    ${options}    add_argument    --disable-application-cache
    Call Method    ${options}    add_argument    --disable-cache
    Open Browser    ${URL}    ${browser}    options=${options} 
    Maximize Browser Window  
    Sleep    1s    
    Take Screenshot
User provided the user credentials
    [Arguments]    ${user}    ${pass}
    ${Usr_locator}=    Set Variable    //input[@id='react-select-2-input']
    ${Pass_locator}=    Set Variable    //input[@id="react-select-3-input"]
    Enter Credential Details    ${Usr_locator}    ${user}
    Set Global Variable    ${user}  
    Enter Credential Details    ${Pass_locator}    ${pass}

Enter Credential Details
    [Arguments]   ${loc}    ${cred}    
    input text    ${loc}    ${cred}
    Press Keys    ${loc}    ENTER
    Sleep    1s    
    Take Screenshot    
    
User proceeded with login 
    Click Element    //button[@id="login-btn"] 
    Sleep    1s    
    Take Screenshot   

Verified if user successfully logged in application
    Variable Should Exist    ${user}    
    ${text}=    Get Text    //span[@class="username"]
    ${Status}=    Run Keyword And Return Status    Should Be Equal As Strings    ${text}    ${user}    
    run keyword if     '${Status}'=='True'    Log To Console    User is successfully Logged in the application    ELSE    Fail   
    Sleep    1s   
    Take Screenshot 

User Closed the browser
    Close Browser     
              
Selected the Mobile Category as ${category} 
    ${Mobile_category}=    Remove Quotes    ${category}
    Log To Console    This is the category ${Mobile_category}    
    Set Global Variable    ${Mobile_category}    
    ${Category_locator}=    Set Variable    //span[@class='checkmark' and contains(text(),'${Mobile_category}')] 
    Click Element    ${Category_locator} 
    Set Global Variable    ${Category_locator}        
    Sleep    1s    
    Take Screenshot

Verified that only mobiles with text ${expected_text} are displayed
    Log To Console    ${expected_text} should be present among all mobile devices     
    # [Arguments]    ${expected_text}
    ${mobiles}=    Get WebElements    //p[@class='shelf-item__title']
    :FOR    ${mobile}     IN     @{mobiles}
    \    ${text}=    Get Text    ${mobile}
    \    Log To Console    ${text}    
    \    Should Contain    ${text}    ${expected_text}    
    Take Screenshot
    
Unselected the category   
    Variable Should Exist    ${Category_locator}     
    Click Element    ${Category_locator}
    Sleep    1s    
    Take Screenshot

Remove Quotes
    [Arguments]    ${text}
    ${cleaned_text}=    Replace String    ${text}    "    ${EMPTY}   # Remove double quotes
    [Return]    ${cleaned_text}
    
Got the orders of items displayed      
    ${item_price}=    get Item prices
    ${asc_sorted} =     Copy List    ${item_price}    
    Sort List    ${asc_sorted}     #  initial sort will be ascending
    Set Global Variable    ${asc_sorted}   
    Log    Ascending order of prices is ${asc_sorted}              
     ${desc_sorted} =     Copy List    ${asc_sorted} 
    Reverse List    ${desc_sorted}       #  this will reverse the ascending list
    Set Global Variable    ${desc_sorted}   
    Log    Descending order of prices is ${desc_sorted}    
    
get Item prices 
    @{Item_price_list}=    Create List
    ${prices}=    Get WebElements    //div[@class='val']//b
    :FOR    ${item}     IN     @{prices}
    \    ${text}=    Get Text    ${item}
    \    ${price}=    Convert To Number    ${text}    
    \   Append To List    ${Item_price_list}    ${price}
    Take Screenshot
    [Return]     @{Item_price_list} 
           
Sorted the products as per ${sort_order} option
    ${order}=    Remove Quotes    ${sort_order}
    Sleep    1s    
    ${sort_locator}=    Set Variable    //div[@class='sort']//select
    Wait Until Page Contains Element     ${sort_locator}   
    Select From List By Label    ${sort_locator}     ${order}     
    Sleep    1s  

Verified That the products are sorted as per the sort order ${sort_order}
    ${order}=    Remove Quotes    ${sort_order}
    Variable Should Exist    ${asc_sorted}      
    Variable Should Exist    ${desc_sorted}    
   ${after_Sort_order}=    get Item prices
   Run Keyword If    '${order}' == 'Lowest to highest'    Lists Should Be Equal    ${after_Sort_order}    ${asc_sorted}
   ...    ELSE IF     '${order}' == 'Highest to lowest'    Lists Should Be Equal    ${after_Sort_order}    ${desc_sorted}
   ...    ELSE     Fail    Invalid sort order : ${order}
   
Selected the mobile with name ${mobile_name}
    ${Name}=    Remove Quotes    ${mobile_name}
    Set Global Variable    ${Name}    
    ${mobile_locator} =    Set Variable    //p[@class="shelf-item__title" and contains(text(),'${Name}')] 
    Set Global Variable    ${mobile_locator}    
    ${addToCartBTn} =    Set Variable    ${mobile_locator}//following-sibling::div[contains(text(),'Add to cart')]
    ${isMobilePresent} =    Run Keyword And Return Status    Wait Until Page Contains Element    ${addToCartBTn}          
     Run Keyword If    '${isMobilePresent}'=='True'    Click Element    ${addToCartBTn}        ELSE    Fail   ${Name} is not found, Please check if correct name provided.           
    
Verified if correct Item is added 
    # for getting price of mobile
    Variable Should Exist    ${Name}
    Variable Should Exist    ${mobile_locator}
    ${price_locator} =    Set Variable    ${mobile_locator}//following-sibling::div
    ${text}=    Get Text    ${price_locator}//small    # Get text from <small> tag
    ${value}=    Get Text    ${price_locator}//b    # Get text from <b> tag
    ${cents}=    Get Text    ${price_locator}//span    # Get text from <span> tag
    ${combined}=    Catenate    ${text}    ${value}    ${cents}    # Combine strings
    ${Initial_price} =    Replace String Using Regexp    ${combined}    ${SPACE}    ${EMPTY}     # Remove extra spaces     
    ${NameOfItemAdded}=    Get Text    //div[@class='shelf-item__details']//p[@class="title"]
    ${Price}=    Get Text    //div[@class='shelf-item__price']//p
    ${PriceOfItemAdded}=    Replace String Using Regexp    ${Price}    ${SPACE}    ${EMPTY}    # Remove extra spaces
    Should Be Equal    ${Name}    ${NameOfItemAdded}   
    Should Be Equal    ${Initial_price}     ${PriceOfItemAdded}  
    Set Global Variable    ${FinalPrice}    ${PriceOfItemAdded}         
    Take Screenshot    
    
Proceeded for checkout
    Click Element    //div[@class='buy-btn']
    Sleep    1s    
Entered User Details and Address
    [Arguments]    ${fName}        ${LName}     ${Address}     ${province}     ${Post} 
    Enter Details    firstNameInput    ${fName}
    Enter Details    lastNameInput    ${LName}
    Enter Details    addressLine1Input    ${Address}
    Enter Details    provinceInput    ${province}
    Enter Details    postCodeInput    ${Post}
Enter Details 
    [Arguments]    ${Locator_id}    ${input_text}
    Input Text    //input[@id='${Locator_id}']    ${input_text}    
Clicked on Submit Buton
    click element     //button[@id="checkout-shipping-continue"]
    Sleep    1s    
   
Verified if Correct Product order is place successfully
    Variable Should Exist    ${FinalPrice}
    variable Should Exist    ${Name}
    ${confirmation_Msg}=    Get Text    //legend[@id='confirmation-message']
    Run Keyword If    '${confirmation_Msg}' == 'Your Order has been successfully placed.'    Log    order placed    ELSE    Fail    confirmation message does not match
    
    ${Item_title}=    Get Text    //h5[contains(@class, "product-title")]
    Run Keyword If    '${Item_title}' == '${Name}'    Log    order placed    ELSE    Fail    confirmation message does not match
    ${final_price}=    Get Text    //span[@class="cart-priceItem-value"]
    Run Keyword If    '${final_price}' == '${FinalPrice}'    Log    order placed    ELSE    Fail    confirmation message does not match