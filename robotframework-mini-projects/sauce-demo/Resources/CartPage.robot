*** Settings ***
Documentation    Shop Page keywords
Library    SeleniumLibrary
Library    ScreenCapLibrary
Library    Collections
Library    String
Resource    SauceDemo.resource
*** Variables ***
### define some empty variables
${item}    ${EMPTY}
${item_price}    ${EMPTY}
*** Keywords ***
Verify if product title and price are matching with selected items
    Variable Should Exist    ${item}
    ${Title_of_item_in_cart}=     Get Text    //div[@class="inventory_item_name"]
    Run Keyword If    '${Title_of_item_in_cart}' == '${item}'    Log To Console    Item title macthed    ELSE    Fail
    Variable Should Exist      ${item_price}    #  ${item_price}
    ${Price_of_item_in_cart}=     Get Text    //div[@class="inventory_item_price"]
    Run Keyword If    '${Price_of_item_in_cart}' == '${item_price}'    Log To Console    Item Price macthed    ELSE    Fail
    ${Quantity_of_item_in_cart}=     Get Text    //div[@data-test="item-quantity"]
    Run Keyword If    '${Quantity_of_item_in_cart}' == '1'    Log To Console    Item quantity macthed    ELSE    Fail
    Take Screenshot

Remove the product from cart
      Click Element      //button[contains(@class,"btn_secondary") and contains(text(),"Remove")]

Verify that item is removed from cart
    Variable Should Exist    ${item}
    Page Should Not Contain Element    ${item}
    Take Screenshot

Navigate to the shops page
    Click Element    //button[@id="continue-shopping"]
    Sleep    1s
    Take Screenshot    
    
Proceed to user information page
    Click Element    //button[@id="checkout"]
    Sleep    1s
    Take Screenshot
    Page Should Contain    Checkout: Your Information
