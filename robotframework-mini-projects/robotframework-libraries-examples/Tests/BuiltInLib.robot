*** Settings ***
Documentation    This test deals with common keywords used from BuiltIn library
...            Robot Framework's standard library that provides a set of generic keywords needed often
...            official documentation : https://robotframework.org/robotframework/latest/libraries/BuiltIn.html
Library  BuiltIn
Library    DateTime
Library    Collections

*** Variables ***
${GREETING}    Hello, World!
${USER}        Robot User
${INVALID_USER}    Invalid User

*** Test Cases ***
Test Set Suite Documentation and metadata
    Set Suite Documentation  This suite contains smoke tests    #Sets documentation for the current test suite.
    Set Suite Metadata  version 1.0.0    test   #Sets metadata for the current test suite.

Test Set and Get Global Variable
    Set Global Variable  ${USER}  Robot Framework User       #Makes a variable available globally in all tests and suites.
    ${global_var}=  Get Variable Value  ${USER}              #Returns variable value or default if the variable does not exist.
    Log  Global variable is: ${global_var}                   #Logs the given message with the given level.
    Should Be Equal As Strings  ${global_var}  Robot Framework User    #Fails if objects are unequal after converting them to strings.

Test Set and Get Local Variable
    Set Variable  ${GREETING}  Hello, ${USER}        #Makes a variable available everywhere within the local scope.
    Log  Local variable is: ${GREETING}
    Should Be Equal As Strings  ${GREETING}  Hello, Robot Framework User

Test Set Log Level and Reset
    Set Test Documentation  This test sets documentation for the test case
    Set Test Message  Test case message set using Set Test Message
    Log  Test documentation and message set
    Set Log Level  DEBUG            #Sets the log threshold to the specified level.
    Log  This is a debug message
    #Messages below the level will not logged.
    #The default logging level is INFO, but it can be overridden with the --loglevel command line option.
    #The available levels are TRACE, DEBUG, INFO (default), WARN, ERROR and NONE (no logging).
    Set Log Level  NONE
    Log  This is an None message
    Set Log Level      INFO       #Resets the log level to the original value.
    Log  Log level reset to default

Test Run Keyword And Return status
    ${result}=  Run Keyword And Return status  Evaluate    5<1    #After running the keyword, returns from the enclosing user keyword and passes possible return value from the executed keyword further
    Log    ${result}

Test for Catenate keyword
    ${result}=  Catenate  Hello  World   #Catenates the given items together and returns the resulted string
    Log  Catenated string: ${result}
    Should Be Equal As Strings  ${result}  Hello World    # #default separator is one space
    ${result1}=  Catenate  SEPARATOR=--    Hello  World
    Log  Catenated string: ${result1}
    Should Be Equal As Strings  ${result1}  Hello--World
    ${str}=    Catenate    hello    world    123    Testing
    Should Be Equal    ${str}    hello world 123 Testing

Test Get Length
    ${length}=  Get Length  Robot Framework    #Returns and logs the length of the given item as an integer
    Log  Length of string: ${length}
    Should Be Equal As Numbers  ${length}  15    #Fails if objects are unequal after converting them to real numbers

Test Get Count
    ${str}=    Set Variable    The quick brown fox jumps over the lazy dog.
    ${count}=  Get Count    ${str}    quick   #Returns and logs how many times item is found from container
    Log  Count of occurrences of 'quick': ${count}
    Should Be Equal As Numbers  ${count}  1
    ${str}=    Set Variable    This test
    ${count}=    Get Count    ${str}    t    #it will return value 2 - excludes the Upper case T
    ${count}=    Get Count    ${str}    st    # does not consider Thi's t'est  as there is whitespece between them

Test Replace Variables
    ${str}=    Set Variable    Hello World
    Log    --${str}--
    ${str}=  Replace Variables    Hello India    #Replaces variables in the given text with their current values.
    Log  Replaced string: ${str}
    Should Be Equal As Strings  ${str}  Hello India   #Fails if objects are unequal after converting them to strings.

Test Should Contain
    Should Contain  The quick brown fox jumps over the lazy dog.  quick    #Fails if container does not contain item one or more times.
    Log  The string contains 'quick'

Test Convert To Integer
    ${int_value}=  Convert To Integer  123    #Converts the given item to an integer number in default base 10
    Log  Converted to integer: ${int_value}
    Should Be Equal As Numbers  ${int_value}  123
    ${type}=    Evaluate    type($int_value)
    Should Be Equal As Strings    ${type}    <class 'int'>
    ${int_value2}=  Convert To Integer  123    base=32    #converts to integer base 2
    log    converted to integer with base 32 : ${int_value2}

Test Convert To Number
    ${number_value}=  Convert To Number  3.14   # Converts the given item to a floating point number with default precision of None
    Log  Converted to number: ${number_value}
    Should Be Equal As Numbers  ${number_value}  3.14
    ${type}=    Evaluate    type($number_value)
    Should Be Equal As Strings    ${type}    <class 'float'>
    ${number_value}=  Convert To Number  12.6752    2
    Should Be Equal As Numbers  ${number_value}  12.68        #rounds of the number
    ${number_value}=  Convert To Number  2.62712    4
    Should Be Equal As Numbers  ${number_value}  2.6271        #rounds of the number

Test Convert Integer To String
    ${int}=    Convert To Integer    88
    ${type}=    Evaluate    type($int)
    ${str_value}=  Convert To String  ${int}    #Converts the given item to a Unicode string
    Log  Converted to string: ${str_value}
    ${type_str}=    Evaluate    type($str_value)
    Should Be Equal As Strings         ${type_str}  	<class 'str'>

Test Convert Float To String
    ${flo}=    Convert To Number    3.2637
    ${type}=    Evaluate    type($flo)
    ${str_value}=  Convert To String  ${flo}    #Converts the given item to a Unicode string
    Log  Converted to string: ${str_value}
    ${type_str}=    Evaluate    type($str_value)
    Should Be Equal As Strings         ${type_str}  	<class 'str'>

Test Convert List To String
    ${list}=    Create List    1    2     3     4
    Log list      ${list}
    ${type}=    Evaluate    type($list)
    ${str_value}=  Convert To String  ${list}
    ${type_str}=    Evaluate    type($str_value)
    Should Be Equal As Strings       ${str_value}    ['1', '2', '3', '4']
    Should Be Equal As Strings         ${type_str}  	<class 'str'>

Test Convert Dictionary To String
    ${dict}=    Create Dictionary        key1=1    key2=2     key3=3
    Log Dictionary    ${dict}
    ${type}=    Evaluate    type($dict)
    ${str_value}=  Convert To String  ${dict}
    ${type_str}=    Evaluate    type($str_value)
    Should Be Equal As Strings       ${str_value}    {'key1': '1', 'key2': '2', 'key3': '3'}
    Should Be Equal As Strings         ${type_str}  	<class 'str'>

Test Convert boolean and NONE value To String
    ${bool}=    Set Variable    ${TRUE}
    ${type}=    Evaluate    type(bool)
    ${str_value}=  Convert To String  ${bool}
    ${type_str}=    Evaluate    type($str_value)
    Should Be Equal As Strings       ${str_value}    True
    Should Be Equal As Strings         ${type_str}  	<class 'str'>
### for FALSE
    ${bool}=    Set Variable    ${FALSE}
    ${str_value}=  Convert To String  ${bool}
    Should Be Equal As Strings       ${str_value}    False
### for NONE
    ${none}=    Set Variable    ${NONE}
    ${type}=    Evaluate    type($none)
    ${str_value}=  Convert To String  ${none}
    Should Be Equal As Strings       ${str_value}    None

Test Convert To Binary
    ${int}=    Convert To Integer    88
    ${binary_value}=  Convert To Binary  ${int}    #first converts to integer internally then Converts the given item to a binary string of base 2
    Log  Converted to binary: ${binary_value}
    Should Be Equal As Strings  ${binary_value}  1011000
    ${type}=    Evaluate    type($binary_value)
    Should Be Equal As Strings       ${type}    <class 'str'>

Test Regexp Escape
    ${escaped_string}=  Regexp Escape  S^a^m^p^l^e    #Returns each argument string escaped for use as a regular expression
    #Escaping is done with Python's re.escape() function.
    Log  Escaped string: ${escaped_string}

Test Evaluate
    ${eval_result}=  Evaluate  5 * 10    #Evaluates the given expression in Python and returns the result
    Log  Evaluated result: ${eval_result}
    Should Be Equal As Numbers  ${eval_result}  50

Test Should Not Match Regexp
    Should Not Match  The quick brown fox jumps over the lazy dog.  ^dog$    #Fails if the given string matches the given pattern
    #If ignore_case is given a true value, the comparison is case-insensitive.
    Log  The string does not match the regex ^dog$

Test Convert To Hex
    ${hex_value}=  Convert To Hex  123
    #Converts the given item to a hexadecimal string
    Log  Converted to hex: ${hex_value}
    Should Be Equal As Strings  ${hex_value}  7B