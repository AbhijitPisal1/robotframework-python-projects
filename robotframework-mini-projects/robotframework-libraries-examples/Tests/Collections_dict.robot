*** Settings ***
Documentation    This test deals with common keywords used from Collections library
...            A library providing keywords for handling lists and dictionaries.
...            official documentation : https://robotframework.org/robotframework/latest/libraries/Collections.html
Suite Setup    Log    This Suite deals with test cases for dictionary objects.
Library    Collections

*** Test Cases ***
Test for creating a Dictionary
    #key=value approach
    ${dict_1}=    Create Dictionary    a=1    b=2
    Log Dictionary    ${dict_1}        #output    {'a': '1', 'b': '2'}

    #separate key and value argument
    ${dict_2}=    Create Dictionary    c     3     d     4
    Log Dictionary    ${dict_2}        #output    {'c': '3', 'd': '4'}

    #using variables
    ${dict_3}=    Create Dictionary    e=${5}
    Log Dictionary    ${dict_3}        #output     {'e': 5}

    #combining one dictionary into another
    ${dict_4}=    Create Dictionary    f=${7}   &{dict_1}    g=8
    Log Dictionary    ${dict_4}        #output    {'f': 7, 'a': '1', 'b': '2', 'g': '8'}

    # value itself is a dictionary
    ${d1}=    Create Dictionary    2     1
    ${dict_5}=    Create Dictionary    3     ${d1}
    Log Dictionary    ${dict_5}        #output    {'3': {'2': '1'}}

    # empty dictionary
    ${dict_6}=    Create Dictionary
    Log Dictionary    ${dict_6}        #output    {}    dictionary is empty

    # empty value in dictionary
    ${dict_7}=    Create Dictionary    a=2    b=4    c=
    Log Dictionary    ${dict_7}        # output {'a': '2', 'b': '4', 'c': ''}

    # duplicate key with different values in dictionary
    ${dict_8}=    Create Dictionary    a=1    a=2
    Log Dictionary    ${dict_8}        # output {'a': '2'}

    # for different keys same value
    ${dict_9}=    Create Dictionary    a=1    b=1
    Log Dictionary    ${dict_9}        # output {'a': '1', 'b': '1'}

Test for Update dictionary using Keep In Dictionary keyword
    ${dict_1}=    Create Dictionary        a=1    b=2    c=3    d=4    e=5
    Keep In Dictionary    ${dict_1}    b     i     d     g      #provide key names
    #it will keep only those pairs matching with key name argument given
    #for any argument given, if it not present in dict, it will be ignored
    Log Dictionary     ${dict_1}     #output    {'b': '2', 'd': '4'}

Test for Update dictionary using Set To Dictionary keyword
    ${dict_1}=    Create Dictionary        a=apple    b=banana
    Log Dictionary    ${dict_1}        #Output    {'a': 'apple','b': 'banana'}
    #set using key=value approach
    Set To Dictionary    ${dict_1}    c=cat    d=dog
    Log Dictionary     ${dict_1}     #output    {'a': 'apple','b': 'banana', 'c': 'cat', 'd': 'dog'}
    #set providing key and values separately
    Set To Dictionary    ${dict_1}    e     elephant    f     fox
    Log Dictionary    ${dict_1}    #output    {'a': 'apple','b': 'banana', 'c': 'cat', 'd': 'dog', 'e': 'elephant', 'f': 'fox'}

Test for Convert To Dictionary keyword
    [Documentation]    by default the returned dictionary is robot framework's own DotDict Instance
    ...                if there is need, it can be converted into a regular python dict instance
    ...                by using the Convert To Dictionary keyword
    ${dict_1}=    Create Dictionary    a=apple    b=banana
    ${type_dict_1}=    Evaluate    type($dict_1)    #type is <class 'robot.utils.dotdict.DotDict'>
    Should Be True    type($dict_1)    is not dict
    ${dict_2}=    Convert To Dictionary    ${dict_1}
    ${type_dict_2}=    Evaluate    type($dict_2)    #type is <class 'dict'>
    Should Be True    type($dict_2)    is dict
    Should Be Equal    ${dict_1}    ${dict_2}        #type is different but values will be same

Test for Copying Dictionary
    ${dict_1}=    Create Dictionary    a=apple    b=ball    c=cat    d=dog    #output {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
    ${dict_2}=    Copy Dictionary    ${dict_1}    #output    {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
    Set To Dictionary    ${dict_1}    a=ant
    Set To Dictionary    ${dict_2}    b=baseball
    Log Dictionary    ${dict_1}    #output    {'a': 'ant', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
    Log Dictionary    ${dict_2}    #output    {'a': 'apple', 'b': 'baseball', 'c': 'cat', 'd': 'dog'}

Test for Get From Dictionary keywords
    ${dict_1}=    Create Dictionary    2=TWO    1=ONE    4=FOUR    3=THREE

    Log    test Get From Dictionary
    ${value}=    Get From Dictionary    ${dict_1}    3    #provide key
    Should Be Equal    ${value}   THREE
    ${value}=    Get From Dictionary    ${dict_1}    7     #default=NONE
    Should Be Equal    ${value}   NONE    #sine given key is not present it will return default value set
    Log    success

    Log    test Get Dictionary Items
    ${sorted_dict}=    Get Dictionary Items    ${dict_1}
    #it will sort the dictionary based on keys and then return entire dictionary as list
    Log     ${sorted_dict}    #output ['1', 'ONE', '2', 'TWO', '3', 'THREE', '4', 'FOUR']

    ${unsorted_dict}=    Get Dictionary Items    ${dict_1}    sort_keys=False
    log     ${unsorted_dict}    #output    ['2', 'TWO', '1', 'ONE', '4', 'FOUR', '3', 'THREE']
    Log    success

    Log    test Get Dictionary Keys
    ${key_sorted}=    Get Dictionary Keys    ${dict_1}
    #it will return keys only - in sorted order
    Log    ${key_sorted}    #output    ['1', '2', '3', '4']

    ${key_unsorted}=    Get Dictionary Keys    ${dict_1}    sort_keys=False
    Log    ${key_unsorted}    #output    	['2', '1', '4', '3']
    Log    success

    Log    test Get Dictionary Values
    ${value_sorted}=    Get Dictionary Values    ${dict_1}
    #it will return values only - in sorted order
    Log    ${key_sorted}    #output    	['ONE', 'TWO', 'THREE', 'FOUR']
    ${Value_unsorted}=     Get Dictionary Values    ${dict_1}    sort_keys=False
    Log    ${key_unsorted}    #output    	['TWO', 'ONE', 'FOUR', 'THREE']
    Log    success

Test for Dictionary assertions
    ${dict}=    Create Dictionary    DL=Delhi    PN=Punjab    KL=Kerala    UP=Uttar Pradesh    MH=Maharashtra

    Dictionary Should Contain Item    ${dict}    DL    Delhi
    #format is Dictionary Should Contain Item    ${dict}    key    value
    #cannot query like key=value.... it will be considered single key item
    Dictionary Should Contain Item    ${dict}    PN    punjab    ignore_case=True
#    # If value provided does not match with key then Error :    Value of dictionary key '' does not match
#    Dictionary Should Contain Item    ${dict}    KL    Karnataka    msg=Item is not present
#    # If key provided is not present in dictionary then Error : Dictionary does not contain key 'GJ'.
#    Dictionary Should Contain Item    ${dict}    GJ    Gujrat

    Dictionary Should Contain Key    ${dict}    UP
    Dictionary Should Contain Key    ${dict}    MH    ignore_case=True
#    # If key is not present then Error : Dictionary does not contain key 'CG'.
#    Dictionary Should Contain Key    ${dict}    CG

    Dictionary Should Not Contain Key    ${dict}    CG
    Dictionary Should Not Contain Key     ${dict}    jk    ignore_case=True
#    # If key is present then Error : Dictionary contains key ''.
#    Dictionary Should Not Contain Key     ${dict}    UP

    Dictionary Should Contain Value    ${dict}    Maharashtra
    Dictionary Should Contain Value    ${dict}    MAHARASHTRA    ignore_case=True

    Dictionary Should Not Contain Value   ${dict}    MAHARASHTRA    #case does not match and hence value will not macth
#    Dictionary Should Not Contain Value    ${dict}    MAHARASHTRA    ignore_case=True    #this will fail as value after ignore case TRUE exist

Test for SubDictionary
    ${dict}=    Create Dictionary    DL=Delhi    PN=Punjab    KL=Kerala    UP=Uttar Pradesh    MH=Maharashtra
    ${sub_dict1}=    Create Dictionary      DL=Delhi
    ${sub_dict2}=    Create Dictionary      mh=Maharashtra
    ${sub_dict3}=    Create Dictionary      MH=Maharashtra    GJ=Gujrat

    Dictionary Should Contain Sub Dictionary    ${dict}     ${sub_dict1}
    Dictionary Should Contain Sub Dictionary    ${dict}     ${sub_dict2}    ignore_case=True    #it passes as ignore case removes case insensitive issue
#   #  In case any key value pair is missing in first dict then error: Following keys missing from first dictionary: 'GJ'
#    Dictionary Should Contain Sub Dictionary    ${dict}     ${sub_dict3}

Test For Deleting or removing from dictionary
    ${dict}=    Create Dictionary    1=One    3=Three    2=Two    4=Four
    ${popped_item}=    Pop From Dictionary    ${dict}    3
    Log    ${popped_item}    #output    Three --- only value is shown
    Log    ${dict}    #output    {'1': 'One', '2': 'Two', '4': 'Four'}
    
    Remove From Dictionary    ${dict}    4    2     5    8
    Log Dictionary    ${dict}        #output    {'1': 'One'}
    # If key is present --> Removed item with key '2' and value 'Two'.
    # Ignores if key not present --> Key '8' not found.

    ## difference between pop and remove
    ## Pop From Dictionary - removes item and returns the specified element value from  dictionary
    ##  Remove From Dictionary - removes item and does not return the specified element value