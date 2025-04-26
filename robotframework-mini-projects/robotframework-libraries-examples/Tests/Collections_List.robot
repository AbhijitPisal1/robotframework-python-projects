*** Settings ***
Documentation    This test deals with common keywords used from Collections library
...            A library providing keywords for handling lists and dictionaries.
...            official documentation : https://robotframework.org/robotframework/latest/libraries/Collections.html
Suite Setup    Log    This Suite deals with test cases for List objects.
Library    Collections
Library    OperatingSystem

*** Test Cases ***
Test for creating a list
    ${list_1}=    Create List    Apple    Banana
    Log List    ${list_1}    #['Apple', 'Banana']

    @{list_2}=    Create List    Mango    Orange
    Log List    ${list_2}    #[ Mango | Orange ]

Test for Append To List keyword
    # Append to list will directly add item at end of list
    ${list1}=    Create List    Apple    Banana
    Log List    ${list1}    #['Apple', 'Banana']
    Append To List    ${list1}    Mango
    Log List    ${list1}    # ['Apple', 'Banana', 'Mango']

Test for Insert Into List keyword
    # Insert Into List will add item at specified index
    ${items}=    Create List    test1    test3    test4    test2
    Log List    ${items}    #['test1', 'test3', 'test4', 'test2']
    Insert Into List    ${items}    0    test0        ##add item as 0 index item
    Log List    ${items}    #['test0', 'test1', 'test3', 'test4', 'test2']
    Insert Into List    ${items}    -1    test6        #add items as second last index item
    Log List    ${items}    #['test0', 'test1', 'test3', 'test4', 'test6', 'test2']

Test for Set List Value keyword
    # Set list value will be replacing the value present in list
    ${table}=    Create List    a     b     c     d     e     f
    Log List    ${table}    #['a', 'b', 'c', 'd', 'e', 'f']
    Set List Value   ${table}    0    1    # replaces value 'a' present at 0 index with new value '1'
    Log List    ${table}    #['1', 'b', 'c', 'd', 'e', 'f']
    Set List Value    ${table}    -1    100    # replaces values 'f' present at end of list with new value '100'
    Log List    ${table}    # ['1', 'b', 'c', 'd', 'e', '100']
Test for Combine Lists keyword
    # combines lists one after other in sequence
    # Combine Lists    ${list_1}    ${list_2} !==    Combine Lists    ${list_2}    ${list_1}
    ${list_1}=    Create List    1     2     3     4     5
    Log List    ${list_1}    #['1', '2', '3', '4', '5']
    ${list_2}=    Create List    a     b     c     d     e
    Log List    ${list_2}    #['a', 'b', 'c', 'd', 'e']
    ${combined_list}=    Combine Lists    ${list_1}    ${list_2}
    Log List    ${combined_list}    #['1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e']
    ${combined_list2}=    Combine Lists    ${list_2}    ${list_1}
    Log List    ${combined_list2}    #['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']

Test for Sort list keyword
    # sorts list in alphabetical order
    ${list_1}=    Create List    4     2     1     2     3     5
    Sort List    ${list_1}
    Log List    ${list_1}    # output ['1', '2', '2', '3, '4', '5']
    ${list_2}=    Create List    z     a     b    d     b     ca     cd    ce     cat     car
    Sort List     ${list_2}    # output ['a', 'b, 'b', 'ca', 'car', 'cat', 'cd', 'ce', 'd', 'z']
    Log List    ${list_2}
    ${list_3}=    Create List    7     a    2    z     p
    sort List    ${list_3}    #output    ['2', '7', 'a', 'p', 'z']
   Log List    ${list_3}    #numbers are first sorted then characters

Test for Reverse List keyword
    ${items}=    Create List    test1    test5    test3    test4    test2
    Log List    ${items}    # output    #['test1', 'test5', 'test3', 'test4', 'test2']
  # #reverses list directly by index so last item in original list will be first item in new list
    Reverse List    ${items}
    Log List    ${items}    #output ['test2', 'test4', 'test3', 'test5', 'test1']
Test for Extracting from List

    ${alphabets}=    Create List     a     a    d     b     c     a     c     d

    ${a_count}=    Count Values In List    ${alphabets}    a     #count 3
    ${z_count}=    Count Values In List    ${alphabets}    z     # no such values - 0
    ${A_count}=    Count Values In List    ${alphabets}    A    #case sensitive keyword - count 0

    #gives value present at index
    ${character}=    Get From List    ${alphabets}    1    # index 1 i.e second value   #a
    ${character}=    Get From List    ${alphabets}    3    # index 3 i.e fourth value #b
    ${character}=    Get From List    ${alphabets}    -1    # last index    #d

    ##gives index of character
    ${index}=    Get Index From List    ${alphabets}    b     #3
    ${index}=    Get Index From List    ${alphabets}    a    #first instance is returned in this case index 0
    ${index}=    Get Index From List    ${alphabets}    d    #first instance is returned in this case index 2

    # Get Slice From List gives part of list
    # it includes stat index given but ignores end index
    ${slice1}=    Get Slice From List    ${alphabets}    1     3     #start index =1    end index=    3
    Log List        ${slice1}    #output    ['a', 'd']
    ${slice2}=    Get Slice From List    ${alphabets}    3         #start index =3    end index= not given so last index considered
    Log List        ${slice2}    #output    ['b', 'c', 'a', 'c', 'd']
    ${slice3}=    Get Slice From List    ${alphabets}    end=3     #start index =1    end index=3 start not given so 0 index taken
    Log List        ${slice3}    #output    ['a', 'a', 'd']

Test for convert tuple to list
    ${tuple_val}=    Evaluate    (1, 2, 3)
    Log    ${tuple_val}    #(1, 2, 3)
    ${type}=    Evaluate    type($tuple_val)
    Should Be Equal As Strings    ${type}    <class 'tuple'>
    ${list}=    Convert To List    ${tuple_val}
    Log List    ${list}    #[1, 2, 3]
    ${type}=    Evaluate    type($list)
    Should Be Equal As Strings    ${type}    <class 'list'>

Test for convert set to list
    ${set_val}=    Evaluate    ('apple', 'banana', 'mango')
    Log    ${set_val}    # ('apple', 'banana', 'mango')
    ${type}=    Evaluate    type($set_val)
    Should Be Equal As Strings    ${type}    <class 'tuple'>
    ${list}=    Convert To List    ${set_val}
    Log List    ${list}    # ['apple', 'banana', 'mango']
    ${type}=    Evaluate    type($list)
    Should Be Equal As Strings    ${type}    <class 'list'>

Test for convert string to list
    ${string}=    Set Variable    Good Morning
    Log    ${string}    # Good Morning
    ${type}=    Evaluate    type($string)
    Should Be Equal As Strings    ${type}    <class 'str'>
    ${list}=    Convert To List    ${string}
    Log List    ${list}    # ['G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g']
    ${type}=    Evaluate    type($list)
    Should Be Equal As Strings    ${type}    <class 'list'>

Test for Copy List keyword
    ${original_list}=    Create List    item1    item2    item3    item4
    ${copied_list}=    Copy List    ${original_list}
    # both lists are now same     ['item1', 'item2', 'item3', 'item4']
    # once list are copied, appending will have no impact
    Append To List    ${original_list}    item5    item6
    Log List    ${original_list}    #['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
    Append To List    ${copied_list}    item10
    Log List    ${copied_list}    # ['item1', 'item2', 'item3', 'item4', 'item10']

Test for Deleting from list
    ${items}=    Create List   item1    item2    item3    item4    item5
    Log List    ${items}    #['item1', 'item2', 'item3', 'item4', 'item5']

    # removes the item based on index provided
    ${removed_items}=    Remove From List    ${items}   2
    Log List    ${items}    #['item1', 'item2', 'item4', 'item5']

    ${removed_items}=    Remove From List    ${items}    -1
    Log List    ${items}    # ['item1', 'item2', 'item4']

    # removes value from list based on values provided
    ${removed_items}=    Remove Values From List    ${items}    item1    item4
    Log List    ${items}    # ['item2']

Test for List Should Contain Sub List assertion
    ${list1}=    Create List    item1    item2    item3    item4
    ${sub_list1}=    Create List    item1    item3
    ${sub_list2}=    Create List    ITEM2
    List Should Contain Sub List    ${list1}    ${sub_list1}
    List Should Contain Sub List    ${list1}    ${sub_list2}    ignore_case=True

#    #    ${sub_list3}=    Create List    item5
#    #    List Should Contain Sub List    ${list1}    ${sub_list3}    msg=This test case will fail and this message will be returned

Test for List Should Contain Value assertion
    ${list1}=    Create List    item1    item2    item3    item4
    List Should Contain Value    ${list1}    item3
    List Should Contain Value    ${list1}    ITEM2    ignore_case=True
#   # List Should Contain Value     ${list1}    item5    msg=This test case will fail and this message will be returned

Test for List Should Not Contain Value assertion
    ${list1}=    Create List    item1    item2    item3    item4
    List Should Not Contain Value    ${list1}    item5
    List Should Not Contain Value    ${list1}       ITEM2    #case sensitive item so it will pass
#     # List Should Not Contain Value     ${list1}    ITEM2        ignore_case=True    msg=This test case will fail and this message will be returned

Test for List Should Not Contain Duplicates assertion
    ${list1}=    Create List    item1    item2    item3    item4
    List Should Not Contain Duplicates    ${list1}
    ${list2}=    Create List    item1    item2    item3    ITEM2
    List Should Not Contain Duplicates    ${list2}    # case sensitive hence passes
#
#    ${list3}=    Create List    item1    item2    item3    ITEM2
#    List Should Not Contain Duplicates    ${list3}    ignore_case=True    # fails here as case insensitive now
#    ${list2}=    Create List    item1    item2    item1
#    List Should Not Contain Duplicates    ${list2}    #fails because of 'item1' found multiple times.

Test for Lists Should Be Equal assertions
    ${list1}=    Create List   item1     item2    item3
    ${list2}=    Create List   item1     item2    item3
   Lists Should Be Equal    ${list1}    ${list2}
   
   # case of items can be ignored by using ignore_case
   ${list3}=    Create List   item1     ITEM2    ITEM3
   Lists Should Be Equal    ${list1}    ${list3}    ignore_case=True

    # order of items can be ignored by using ignore_order
   ${list4}=    Create List   item2     item3    item1
    Lists Should Be Equal    ${list1}    ${list4}    ignore_order=True
    
    ${tuple}=    Evaluate    ('a', 'b', 'c')
    ${items}=    Create List    a     b     c 
    Lists Should Be Equal    ${tuple}    ${items}
    
Test for remove duplicates
    ${list1}=    Create List    1     2     3     4     2     1     2     
    # removes duplicate values and returns list without any duplicates
    ${removed_duplicates}=    Remove Duplicates    ${list1}
    Log List    ${removed_duplicates}    #output    ['1', '2', '3', '4']
    

