*** Settings ***
Documentation    This test deals with common keywords used from String library
...            A library providing keywords for string manipulation and verification.
...            official documentation : https://robotframework.org/robotframework/latest/libraries/String.html
Suite Setup    Log    This Suite deals with test cases for basic String scenario.
Library    String
Library    Collections

*** Variables ***
${column_text}    robot\tframework\ntool\tfor\ttesting
#robot    framework
#tool    for     testing
${line1}    robot\tframework
${Line2}    tool\tfor\ttesting
${input}    First Line\nSecond Line\nThird Line\n\nLast Line contains multiple words
#First Line
#Second Line
#Third Line

#Last Line contains multiple words
${new_input}    Line 1\nLine 2\nThird Line
*** Test Cases ***
Test Get Length of list
    ${list}=    Create List    1    2    3    4    5
    ${length}=    Get Length    ${list}
    Should Be Equal As Numbers    ${length}    5

Test Get Length of empty list
    ${empty_list}=    Create List
    ${length}=    Get Length    ${empty_list}
    Should Be Equal As Numbers    ${length}    0

Test Get Length of string
    ${string}=    Set Variable    Robotframework
    ${length}=    Get Length    ${string}
    Should Be Equal As Numbers    ${length}    14

Test Get Length of empty string
    ${empty_string}=    Set Variable
    ${length}=    Get Length    ${empty_string}
    Should Be Equal As Numbers    ${length}    0

Test Get Length of dictionary
    ${dict1}=    Create Dictionary    key1=value1    key2=value2
    ${length}=    Get Length    ${dict1}
    Should Be Equal As Numbers    ${length}    2

Test Get Length of nested list
    ${nested_list}=    Create List    ${EMPTY}    1    ${EMPTY}    2    ${EMPTY}    3
    ${length}=    Get Length    ${nested_list}
    Should Be Equal As Numbers    ${length}    6
    
Test for Fetch From Left keyword
    ${result}=    Fetch From Left    This_is_Robot_framework_program    Robot
    Should Be Equal    ${result}    This_is_
    ${result}=    Fetch From Left    This_is_Robot_framework_program    _framework
    Should Be Equal    ${result}    This_is_Robot
    ${result}=    Fetch From Left    This is Robot framework program    Robot
    Log    --${result}--
    Should Be Equal    ${result}    This is${SPACE}    #whitespace before robot will be also fetched
    ${result}=    Fetch From Left    This is Robot framework program    work
    Log    --${result}--
    Should Be Equal    ${result}    This is Robot frame

Test for Fetch From Right keyword
    ${result}=    Fetch From Right    This_is_Robot_framework_program    Robot_
    Should Be Equal    ${result}    framework_program

Test for Generate Random string keyword
   ${string}=          Generate Random String
   ${lower_string}=    Generate Random String    12    [LOWER]
   ${upper_string}=    Generate Random String    12    [UPPER]
   ${letters_string}=    Generate Random String    12    [LETTERS]
   ${numbers_string}=    Generate Random String    10    [NUMBERS]
   ${binary_string}=    Generate Random String    8    01
   ${string2}=    Generate Random String    5-10    #generates string of 5 to 10 characters

Test for Get Line keyword
    ${result}=    Get Line    ${column_text}    0    #index of line to be provided - for first line index is 0
    Should Be Equal    ${result}    ${line1}
     ${result}=    Get Line    ${column_text}    1    #for second line index is 1
    Should Be Equal    ${result}    ${line2}
     ${result}=    Get Line    ${column_text}    -1    #for last line index is -1
    Should Be Equal    ${result}    ${line2}

Test for Get Line Count keyword
    ${result}=    Get Line Count    ${column_text}
    Should Be Equal As Integers    ${result}    2
    ${result}=    Get Line Count    ${EMPTY}    #empty will return zero line
    Should Be Equal As Integers    ${result}    0
    ${result}=    Get Line Count    ${SPACE}    #single space is considered as one line
    Should Be Equal As Integers    ${result}    1

Test for Get Line Containing string keyword
    Log    ${input}
    ${result}=    Get Lines Containing String    ${input}    Third    #gives entire line which has the given string
    Should Be Equal    ${result}     Third Line
     ${result}=    Get Lines Containing String    ${input}    Last    #gives entire line which has the given string
    Should Be Equal    ${result}     Last Line contains multiple words
    ${result}=    Get Lines Containing String    ${input}    second    ignore_case=True    #ignores character case
    Should Be Equal    ${result}     Second Line
    ${result}=    Get Lines Containing String    ${input}    Line
    Should Be Equal    ${result}     First Line\nSecond Line\nThird Line\nLast Line contains multiple words    #removes blank line

Test for Get Lines matching pattern keyword
# * --> matching everything
# ? --> Matching any single character
# [chars] --> Matches any chars inside the square brackets
# [!chars] --> Opposite of [chars], matches anything outside of square brackets
    ${result}=    Get Lines Matching Pattern    ${new_input}    Line ?
    Should Be Equal    ${result}  Line 1\nLine 2
    ${result}=    Get Lines Matching Pattern    ${new_input}    Third *
    Should Be Equal    ${result}  Third Line
    ${result}=    Get Lines Matching Pattern    ${new_input}    *line*    ignore_case=True
    Should Be Equal    ${result}  Line 1\nLine 2\nThird Line

Test for get Lines matching Regular expression pattern
    ${result}=    Get Lines Matching Regexp        ${new_input}    (Line | Wine)[1-9]    #changing patterns for regular expression
    Should Be Equal    ${result}  Line 1\nLine 2
    ${result}=    Get Lines Matching Regexp    ${new_input}    Third.*
    Should Be Equal    ${result}  Third Line
    ${result}=    Get Lines Matching Regexp    ${new_input}    (?i).*line.*
    Should Be Equal    ${result}  Line 1\nLine 2\nThird Line

Test For Get SubString keyword
    ${ignore_first}=    Get Substring    Hello Robot framework    1     #define range from where characters are required
    ${ignore_last}=    Get Substring    Hello Robot framework    0     -1
    ${5th_to_10th}=    Get Substring    Hello Robot framework    4     10
    ${first_two}=    Get Substring    Hello Robot framework    0    2
    ${last_two}=    Get Substring    Hello Robot framework    -2

Test for Split String keyword
    ${result}=    Split String    abc_def_ghi_jkl    _     #output ['abc', 'def', 'ghi', 'jkl']
    ${result}=    Split String    abc def ghi jkl        #default separator of space
    ${result}=    Split String    abc def ghi jkl    ${SPACE}    #works same as above
    ${result}=    Split String    abc def ghi jkl    max_split=2        #output ['abc', 'def', 'ghi_jkl']
    #splits string into given max split number and combines rest fo the data into a separator item
    ${result}=    Split String    abc_def_ghi_jkl    _     max_split=2    #output would be ['abc', 'def', 'ghi_jkl']

Test for Split String from right keyword
    ${result}=    Split String From Right        abc_def_ghi_jkl    _      #output ['abc', 'def', 'ghi', 'jkl']
    ${result}=    Split String From Right       abc_def_ghi_jkl    _    max_split=2        #output  ['abc_def', 'ghi', 'jkl']

Test for Split string to characters keyword
        @{chars}=    Split String To Characters    Hello robotframework
        #output [ H | e | l | l | o |   | r | o | b | o | t | f | r | a | m | e | w | o | r | k ]
        # whitespace also considered separate character

Test for Split to lines keyword
    @{result}=    Split To Lines     ${column_text}
    Length Should Be    ${result}    2
    Should Be Equal    ${result}[0]    ${line1}
    Should Be Equal    ${result}[1]    ${line2}

Test for Length should be keyword
    Length Should Be    superman    8        #matches character count and matches
    ${dict}=    Create Dictionary    key1=val1    key2=val2
    Length Should Be    ${dict}    2
    ${expected_length}=    Set Variable    3
    ${list}=    Create List    Apple    banana    mango
    Length Should Be    ${list}    ${expected_length}        #compares variable

Test for Should be Empty keyword
    # asserts whether object is empty or not
    ${test}=    Set Variable
    Should Be Empty    ${test}
    ${list}=    Create List
    Should Be Empty    ${list}
    ${dict}=    Create Dictionary
    Should Be Empty    ${dict}

Test for Should not be Empty keyword
    # asserts whether object is empty or not
    ${test}=    Set Variable     test
    Should Not Be Empty    ${test}
    ${list}=    Create List    test1    test2    test3
    Should Not Be Empty    ${list}
    ${dict}=    Create Dictionary    key1=val1    key2=val2
    Should Not Be Empty    ${dict}

Test for should be equal keyword
    ${string1}=    Set Variable    hello
    ${string2}=    Set Variable    hello
    ${string3}=    Set Variable    HELLO

    Should Be Equal    ${string1}    ${string2}
    Should Be Equal    ${string1}    ${string2}    ignore_case=True
    Should Be Equal    42    42

    ${list1}=    Create List    1     2     3
    ${list2}=    Create List    1     2     3
    Should Be Equal    ${list1}    ${list2}        #matches each and every element with corresponding value in other list
    #same can used to match dictionary
    # test case for "Should Not be Equal" is same
    ${string4}=    Set Variable    hello world
    Should Not Be Equal    ${string1}    ${string4}

Test for Should contain keyword
    Should Contain    This is a test string    test
    Should Contain    This is a test string    TEST     ignore_case=True
    ${list}=    Create List    Apple    banana    Orange
    Should Contain    ${list}    Banana    ignore_case=True

Test for Should Not contain keyword
    Should Not Contain    This is a test string    TEST    #case-sensitive test
    Should Not Contain    This is a test string    ball     ignore_case=True

    ${list}=    Create List    Apple    banana    Pineapple
    Should Not Contain    ${list}    Orange    ignore_case=True

Test for Should Start with keyword
    Should Start With    Hello world, good afternoon !    Hello
     Should Start With    Hello world, good afternoon !    HELLO    ignore_case=True

Test for Should Not Start With keyword
    Should Not Start With      Hello world, good afternoon !    HELLO    #case-sensitive test
    Should Not Start With    Hello world, good afteroon !    Hi

Test for Should End With keyword
    Should End With       Hello world, good afternoon    afternoon
    Should End With       Hello world, good afternoon    noon
    Should End With    Hello world, good afternoon    AFTERNOON    ignore_case=True

Test for Should Not End with keyword
    Should Not End With    Hello world, good afternoon    AFTERNOON      #case-sensitive test

Test for Should Be String and Should Not Be String keywords
    Should Be String    India
    Should Be String    ${EMPTY}    #empty is also considered as string
    Should Be String    *    #special characters are considered string
    Should Be String    123    #numbers here considered as string with {}
    Should Be String    ${SPACE}
    Should Not Be String    ${123}     # numbers are not strings- so should not be string test passes here
    Should Not Be String    ${TRUE}    #boolean is not string

Test for Should Be Lower Case keyword
   Should Be Lowercase    test
   Should Be Lowercase    hello#123     #special characters have no effect
   #fails if Robot, roBot or roboT -- upper case present anywhere in string

Test for Should Be Upper Case keyword
   Should Be Uppercase    TEST
   Should Be Uppercase    TEST#1     #special characters have no effect
   #fails if rOBOT, RObOT or ROBOt -- lower case present anywhere in string

Test for Should Be TitleCase keyword
   Should Be Titlecase    TEST
   Should Be Titlecase    Test Title    #all words should be title case-- fails for Test title
   Should Be Titlecase    Test#1     #special characters have no effect
