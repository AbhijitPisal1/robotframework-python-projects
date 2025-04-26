*** Settings ***
Documentation    This test covers manager actions such as adding a customer, opening an account, 
...              and managing customer records to ensure core functionalities work as expected.
Library    SeleniumLibrary
Resource    ../Resources/AddCustomerPage.robot
Resource    ../Resources/LoginPage.robot
Resource    ../Resources/CustomerDirectoryPage.robot
Resource    ../Resources/OpenAccountPage.robot
Resource    ../resources/testdata.robot
Suite Teardown    Close the Browser
*** Test Cases ***
Manager logged in the Application
    Given Application is opened in browser
    When Navigate to Manager Actions
    
Manager adds new Customer  
    Given Open the Add Customer Form
    When Provide Customer Details    
    And Complete Adding New customer
    Then Confirm if new customer added
    
Manager Opens new account
    Given Open the Open Account Form
    When Select the Customer Profile
    And Select Currency for Account
    And Complete the Account Creation Process
    Then Confirm if new Account is created
    
Manager Checks for customer and deletes customer from list   
    Given Open the Show Customer page
    When Search for the customer
    And Check if Correct Customer is present
    Then Delete the cutomer