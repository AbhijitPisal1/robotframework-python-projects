*** Settings ***
Documentation    This test validates that the product sorting feature works correctly for both ascending 
...              and descending order. It uses a data-driven approach to verify that items are displayed 
...              in the correct order based on the selected sort filter.
Library    SeleniumLibrary
Library    ScreenCapLibrary
Resource    Data.robot
Suite Setup    User logged in the application
Suite Teardown    Close the browser session
Resource    common_mid_Level.robot
Test Template     Test for Sort filter

*** Test Cases ***                    Sort Order        
Ascending Order test            Lowest to highest 
Descending Order test            Highest to lowest
    
*** Keywords ***
Test for Sort filter
    [Arguments]     ${sort_order}
    Given The ascending & descending orders of items displayed are taken 
    When Sort the products as per ${sort_order} option
    Then Verify That the products are sorted as per the sort order ${sort_order}
    