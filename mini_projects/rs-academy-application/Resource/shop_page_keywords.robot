*** Settings ***
Documentation    Shop Page keywords
Library    SeleniumLibrary
Library    ScreenCapLibrary
Library    Collections
Library    String

*** Keywords ***
Verify if the cart titles in the shop page
    [Arguments]    ${expectedItems}
#    @{expectedList}=     Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements}=    Get Webelements    //h4[@class="card-title"]
    @{ActualList} =     Create List
    FOR    ${element}    IN    @{elements}
        Log    ${element.text}
        Append To List    ${ActualList}    ${element.text}
    END
    Log    ${ActualList}
    Lists Should Be Equal    ${expectedItems}    ${ActualList}
    Take Screenshot

select the product
    [Arguments]    ${item}
    ${elements}=    Get Webelements    //h4[@class="card-title"]
    ${index} =    Set Variable    1
    FOR    ${element}    IN    @{elements}
        Exit For Loop If    '${item}' == '${element.text}'
        ${index}=    Evaluate    ${index} + 1
    END
    Take Screenshot
    Click Button    (//div[@class="card-footer"])[${index}]//button
    Click Element    //a[@class="nav-link btn btn-primary"]

Click on checkout
    Take Screenshot
    Click Element    css:.btn-success

Fill details in Confirmation page and purchase
    [Arguments]    ${country_name}
    Input Text    id:country     ${country_name}
    Take Screenshot
    Wait Until Element Is Visible    //a[contains(text(),"${country_name}")]    10s
    Click Element    //a[contains(text(),"${country_name}")]
#    Sleep    5s
    Click Element    css:.checkbox-primary
    Click Element    css:.btn-success
    Page Should Contain    Success!

verify items in checkout page and proceed
    [Arguments]    ${ListOFProducts}
    ${elements}=    Get Webelements    //h4[@class="media-heading"]
    @{ActualList} =     Create List
    FOR    ${element}    IN    @{elements}
        Log    ${element.text}
        Append To List    ${ActualList}    ${element.text}
    END
    Log    ${ActualList}
    Take Screenshot
    Lists Should Be Equal    ${ListOFProducts}    ${ActualList}