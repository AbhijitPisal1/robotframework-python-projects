*** Settings ***
Documentation    This test validate that selecting amobile category filters product results correctly.
...                            This test uses a datadriven approach to iterate through multiple categories and verify
...                             that the expected text content is found within each item displayed for selected category
Library        SeleniumLibrary
Library        ScreenCapLibrary
Resource        Data.robot
Suite Setup    User logged in the application
Suite Teardown    Close the browser session
Test Template     Verify Mobile category Filter
Resource    common_mid_Level.robot


*** Test Cases ***    ProductCategory        ExpectedText
Apple test            Apple        iPhone 
samsung Test        Samsung        Galaxy 
Google Test        Google        Pixel 
Oneplus Test         OnePlus        One Plus
 
    
*** Keywords ***
Verify Mobile category Filter 
    [Arguments]     ${category}     ${expected}
    Given Select the Mobile Category as ${category}
    When Verify that only mobiles with text ${expected} are displayed
    Then Unselect the category
    