*** Settings ***
Documentation    This test validates a full user flow including login, selecting a mobile from the Apple category,
...              verifying the item, entering user details, and placing the order successfully.
Library        SeleniumLibrary
Library        ScreenCapLibrary
Resource        Data.robot
Suite Teardown    Close the browser session
Resource    common_mid_Level.robot


*** Test Cases ***   
User logged in the application 
    Given Application is opened in browser
    When User provides the user credentials
    And User proceeds with login
    Then Verify if user successfully logged in application
    
    Given Select the Mobile Category as "Apple"
    When Select the mobile with name "iPhone XR"
    And Verify if correct Item is added
    then Proceed for checkout
        
    Given Enter User Details and Address 
    When Click on Submit Buton
    Then Verify if Correct Product order is place successfully
