*** Settings ***
Documentation    This test deals with common keywords used from Dialogs library
...            library providing dialogs for interacting with users
...            provides means for pausing the test or task execution and getting input from users
...            official documentation : https://robotframework.org/robotframework/latest/libraries/Dialogs.html
Library    Dialogs
Library    Collections

*** Test Cases ***
Test for Execute Manual Stop Passing
    [Documentation]    This will show a popup window where user input is required
    Execute Manual Step    Dialog box is opened. click on PASS to pass the test case    This error message will automatically appear in error box if clicked on FAIL
    #if clicked on FAIL, test case will fail and user needs to enter error message
    
    #keyboard action to pass
#    Execute Manual Step    Press <P> or <p> on keyboard to interact with dialog
#
#    #Keyboard action to fail
#    Execute Manual Step    Press FAIL or <F> or <f> on keyboard to Fail the dialog box    This will open when Fail is triggered by clicking on FAIL or <F> or <f>
#
    #keyboard action to esc    pressing on ESC on keyboard will fail the test case with error message No value provided by user.
#    Execute Manual Step    Press on <ESC> button to escape this dialog       

Test for Pause Execution keyword
    #waits until some user action is provided
    Pause Execution    Press OK button
    Pause Execution    Press <enter> key
    Pause Execution    Press <o> Key
    Pause Execution    Press <O> key
    #no effect of arguments, actions performed or even if dialog closed still it will pass
Test for Get Selection from user
    ${value}=    Get Selection From User    
    ...    select single 'demo value' and press OK. \n\n
    ...    apple    mango    banana
    ...    end string
    log     ${value}
        #if no value selected or dialog is closed this will fail
    
Test for Get Selections from user
    ${value}=    Get Selections From User
    ...    select multiple 'demo values' and press OK. \n\n
    ...    apple    mango    banana        oranges
    ...    end string
    log     ${value}
    Should Be True    type($value)    is list
    # if no value selected or dialog is closed this will fail

Test for Get value from user
    ${value}=    Get Value From User      Enter some text and press ok
