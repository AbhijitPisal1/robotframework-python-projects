*** Settings ***
Documentation    This test checks customer actions like login, deposit, withdrawal, 
...              and transaction history updates.
Library    SeleniumLibrary
Resource    ../Resources/DepositPage.robot
Resource    ../Resources/LoginPage.robot
Resource    ../Resources/TransactionsPage.robot
Resource    ../Resources/WithdrawlPage.robot
Resource    ../resources/testdata.robot
Suite Setup    Application is opened in browser
Suite Teardown  Close the Browser
*** Test Cases ***
Customer Logged in the Application
    Then Proceed for Customer Login
    Given Select the User Profile    ${FirstName}    ${LastName}
    When Log into the application
    Then Check if user successfully logged in application    ${FirstName}    ${LastName}
    
Customer Makes A Deposit in Account     
    Given Open the Add deposit Form
    When Customer provides the amount   100
    Then Complete the deposit process
    
    Given Deposit was successful
    Then Check if balance is updated correctly  
    
    Given Open the transactions page
    And Verify that Credited amount is correct    100
    Then Navigate back to main customer page
    
Customer Makes A Withdrawl in Account
    Given Open the withdrawl page
    When Customer provides the amount   50
    Then Complete the Withdrawl process
    
    Given Check if Withdrawl was successful
    Then Check if balance is updated correctly 
    
    Given Open the transactions page
    And Verify that Withdrawn amount is correct    50
    When Customer Logged out
      