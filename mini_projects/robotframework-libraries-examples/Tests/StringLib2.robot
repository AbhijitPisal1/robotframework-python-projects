*** Settings ***
Documentation    This test deals with common keywords used from String library
...            A library providing keywords for string manipulation and verification.
...            official documentation : https://robotframework.org/robotframework/latest/libraries/String.html
Suite Setup    Log    This Suite deals with test cases for String scenario.
Library    String
Library    Collections

*** Variables ***
&{USER}    name=john    email=john@example.com

*** Test Cases ***
Test for Convert Case keywords
    ${str1}=    Convert To Lowercase    ABC    #abc
    ${str2}=    Convert To Lowercase    1A2C30HJI    #1a2c30hji
    
    ${str3}=    Convert To Uppercase    xyz    #XYZ
    ${str4}=    Convert To Uppercase    12sa5uid    #12SA5UID
    
    ${str5}=    Convert To Title Case    hello world    #Hello World
    ${str6}=    Convert To Title Case    distance is 1 km    exclude=is, km    #Distance is 1 km
## If a word is already fully uppercase, it is assumed to be an acronym or proper noun and will remain unchanged when converting to title case.
# Only the first letter of each word gets capitalized in title case.
    ${str6}=    Convert To Title Case    It's an OK IPhone     #It's An OK IPhone
    ${str8}=    Convert To Title Case    UPPER CASE LETTERS WILL NOT BE CHANGED    #UPPER CASE LETTERS WILL NOT BE CHANGED

Test For Should Match RegExp keyword
# What is Regular expression-
# sequence of characters that specifies a match pattern in text.
# Used for "find" or "find and replace" operations on strings, or for input validation.
# "*" to match any sequence of characters
# "?" to match a single character
# "|"	Separates alternate possibilities.
# "\s"	Matches a whitespace character
# "\d"	Matches a digit
    Should Match Regexp    123456    \\d{6}    #regexp for 6 numbers
    Should Match Regexp    Foo: 42    Foo: \\d+    #Regexp for some number \\d+
    Should Match Regexp    ABC\nDEFG    ab.*fg    flags=IGNORECASE|DOTALL

Test For Should Not Match RegExp keyword
    Should Not Match Regexp    dfa12a345a6    \\d{6}
    Should Not Match Regexp    Foo: 42    Food: \\d+
    Should Not Match Regexp    AD\nDEFG    ab.*fg    flags=IGNORECASE|DOTALL

Test For Format String keyword with positional arguments
     #Formats a template using the given positional and named arguments.
   ${result}=    Format String    uploaded File: {} should not be bigger than {file_size}.    photo.jpg    file_size=5 MB
   Should Be Equal    ${result}    uploaded File: photo.jpg should not be bigger than 5 MB.
   #it replaced the arguments in sequential positions

   ${result}=    Format String    ${user.name}<${user.email}>    user=${USER}
   Should Be Equal    ${result}    john<john@example.com>

   # replaces values based on the arguments provided in variable
   ${result}=    Format String    ${user.email}<${user.name}>    user=${USER}
   Should Be Equal    ${result}    john@example.com<john>

   #using [] to provide arguments
   ${result}=    Format String    {user[name]}<{user[email]}>    user=${USER}
   Should Be Equal    ${result}    john<john@example.com>

   ${result}=    Format String    {0:{width}{base}}    ${42}    base=X    width=10
   Should Be Equal    ${result}    ${SPACE*8}2A

Test format string for character alignment
    Log    test for central alignment
    ${result}=    Format String    {:*^10}    test     #central alignment
    Should Be Equal    ${result}    ***test***        #total length will be 10

    ${var1}=    Set Variable    a
    ${result}=    Format String    {:${var1}^10}    1234
    Should Be Equal    ${result}    aaa1234aaa

    Log    test for Right Alignment
    ${result}=    Format String    {:*>10}    test
    Should Be Equal    ${result}    ******test

    Log    test for left alignment
    ${result}=    Format String    {:*<10}    test
    Should Be Equal    ${result}    test******

Test for Remove String Keyword
    ${str}=    Remove String    Robot Framework    work
    Should Be Equal    ${str}    Robot Frame

    ${str}=    Remove String    Robot Framework    o     bt    #removes all patterns given
    Should Be Equal    ${str}    R Framewrk

    ${str}=    Remove String    Robot Framework    class
    Should Be Equal    ${str}    Robot Framework    #if pattern does not match- does not remove anyting

    ${str}=    Remove String    Robot Framework    ${SPACE}
    Should Be Equal    ${str}    RobotFramework

Test for Remove String Using Regexp keyword
## matches pattern and removed it - case sensitive
    ${result}=    Remove String Using Regexp    Robot Framework    F.*k    #searches entire string and removes the string that start with f and ends with k
    Should Be Equal    ${result}    Robot${SPACE}

## matches pattern and removed it - ignores case using flags=I
    ${result}=    Remove String Using Regexp    Robot Framework    f.*k    flags=I
    Should Be Equal    ${result}    Robot${SPACE}

## matches pattern and removed it - ignores case and newline using flags=IGNORECASE|DOTALL
    ${result}=    Remove String Using Regexp    Robot Frame\nwork    f.*k    flags=IGNORECASE|DOTALL
    Should Be Equal    ${result}    Robot${SPACE}

## if pattern does not match then nothing is removed
    ${result}=    Remove String Using Regexp    Robot Framework    fnot.*k
    Should Be Equal    ${result}    Robot Framework

## here in first case C.*t begins at c of cat and ends at t of cart --- removes "cat", "in" and "cart"
    ${result}=    Remove String Using Regexp    put cat in cart    c.*t    flags=I
    Should Be Equal    ${result}    put${SPACE}

## if keyword removes everything is empty string is returned
    ${result}=    Remove String Using Regexp    cat in cart    c.*t    flags=I
    Should Be Equal    ${result}    ${EMPTY}

## remove strings matching multiple patterns
    ${result}=    Remove String Using Regexp    Robot Framework    o.o    r.*w    #removes '0'singlecharacter'o' and 'r'allcharacterstill'w'
    Should Be Equal    ${result}    Rt Fork

Test for Replace string keyword
## replaces string directly with given input
    ${str}=    Replace String    Hello, World!    World    India
    Should Be Equal    ${str}    Hello, India!
## replace string with input for given number of count
## for count=1, removes first instance from left
    ${str}=    Replace String    Hello, World!    l     ${empty}    count=1
    Should Be Equal    ${str}    Helo, World!
## for count=0 removes nothing
    ${str}=    Replace String    Hello, World!    l     ${empty}    count=0
    Should Be Equal    ${str}    Hello, World!
## if count is not specified  then all instances will be removed
    ${str}=    Replace String    Hello, World!    l     ${empty}
    Should Be Equal    ${str}    Heo, Word!
## if count is given -ve then all instances will be removed
    ${str}=    Replace String    Hello, World!    l     ${empty}    count=-1
    Should Be Equal    ${str}    Heo, Word!
Test for Replace String Using Regexp keyword
    ${str}=    Replace String Using Regexp    Robot Framework    F.*k    Class
    Should Be Equal    ${str}    Robot Class
    ${str}=    Replace String Using Regexp    Robot Framework    f.*K    Class    flags=I
    Should Be Equal    ${str}    Robot Class
    ${str}=    Replace String Using Regexp    Robot Framework    o\\w   foo    1
    Should Be Equal    ${str}    Rfooot Framework        #in Robot - ob replaced by foo left side first instance
     ${str}=    Replace String Using Regexp    Robot Framework    o\\w   AB    2
    Should Be Equal    ${str}    RABAB Framework        #in Robot - ob replaced by AB and ot by AB
    ${str}=    Replace String Using Regexp    Robot Framework    o\\w   AB        #all instances will be replaced
    Should Be Equal    ${str}    RABAB FramewABk
    