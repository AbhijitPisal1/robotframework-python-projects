*** Settings ***
Documentation    Shop Page keywords
Library    SeleniumLibrary
Library    ScreenCapLibrary
Library    Collections
Library    String
Resource    SauceDemo.resource

*** Keywords ***
Get all the item titles in the shop page
    ## get all webelements which match given locator
    ${item_titles}=    Get Webelements    ${Item_title_locator}
    ## create an empty list to store the element text
    @{ActualList} =     Create List
    FOR    ${item}    IN    @{item_titles}
        Append To List    ${ActualList}    ${item.text}
        Log    ${item.text}
        ## use for loop to iterate over all elements from ${item_titles} list
        ## and store the text/content in new list
    END
    Log To Console    ${ActualList}
    Set Global Variable    ${ActualList}
    ## set global variable for future use
    Take Screenshot

Add item into cart
    [Arguments]    ${item}
    ## setting item locator as a variable for further use
    Set Global Variable    ${item}
    ${item_desc}=    Set Variable    //div[contains(text(),"${item}")]//ancestor::div[@class="inventory_item_description"]
    ## checking if items is present in page
   Page Should Contain Element    ${item_desc}
   ## storing the item price in a variable
   ${price} =     Get Text    ${item_desc}//div[@class="inventory_item_price"]
   ${item_price1}=    Get Variable Value   ${price}
   Set Global Variable    ${item_price}    $${item_price1}
   ## adding the item to cart
   Click Button    ${item_desc}//button[contains(@class, "btn_inventory")]
    ## click on checkout option
    Click Element    //a[@class="shopping_cart_link"]


    
