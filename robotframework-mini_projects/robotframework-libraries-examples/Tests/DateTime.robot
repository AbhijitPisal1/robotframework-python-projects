*** Settings ***
Documentation    This test deals with common keywords used from DateTime library
...            library for handling date and time values
...            official documentation : https://robotframework.org/robotframework/latest/libraries/DateTime.html
Library    DateTime
Variables    ../Library/DateTimeResource.py

*** Variables ***
${Date_1}    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    #here format is ${datetime(year, month, date, hour(24h format), min, seconds, milliseconds)}
${Date_2}    ${datetime(2025, 4, 15, 22, 45, 12, 123000)}
${Date_3}    ${datetime(2025, 4, 18, 21, 45, 12, 123000)}
${Date_4}    ${datetime(2025, 4, 15, 21, 45, 12)}

# result_format=verbose --> verb format
# result_format=number --> integer
# result_format=timer --> %H:%M:%S-- 12:23:32.000
# result_format=datetime --> year-month-date hour:min:seconds.milliseconds
# result_format=epoch    --> milliseconds

*** Test Cases ***
Add Time to Date Test
    Log    input time: ${Date_1}

    # add time by giving hour argument
    ${new_date_time1}    Add Time To Date    ${Date_1}    1 hour    result_format=datetime
    Log     New time after adding 1 hour : ${new_date_time1}
    Should Be Equal    ${new_date_time1}    ${Date_2}

    # add time by giving days argument
    ${new_date_time2}    Add Time To Date    ${Date_1}    3 days    result_format=datetime
    Log     New time after adding 3 days : ${new_date_time2}
    Should Be Equal    ${new_date_time2}    ${Date_3}

    #add time by giving hour argument and check for result format
    ${new_date_time3}    Add Time To Date    ${Date_1}    1h    result_format=%H:%M:%S %Y.%m.%d
    Log     New time after adding 1 hour : ${new_date_time3}
    Should Be Equal    ${new_date_time3}    22:45:12 2025.04.15

    # hardcoding date values needs date_format to be specified
    ${new_date_time4}    Add Time To Date    22:45:12 2025.04.15    01:02:03    result_format=%H:%M:%S %Y.%m.%d    date_format=%H:%M:%S %Y.%m.%d
    Log     New time after adding given time : ${new_date_time4}
    Should Be Equal    ${new_date_time4}    23:47:15 2025.04.15
#    22:45:12 2025.04.15
#    01:02:03
#    -------------------
#    23:47:15 2025.04.15

    #using python datetime and timedelta time can be added to date
    ${new_date_time5}    Add Time To Date    ${datetime(2025, 4, 15)}    ${timedelta(1)}    result_format=datetime
    Log     New time after adding 1 day using timedelta : ${new_date_time5}
    Should Be Equal    ${new_date_time5}    ${datetime(2025, 4, 16)}

Add Time to Time test

    # use of verbose to format result
    ${new_time}=    Add Time To Time    01:00:00.000    1 hour    result_format=verbose
    Log    new time : ${new_time}
    #verbose result format will show result in the format of given argument
    Should Be Equal    ${new_time}    2 hours

    # use of timer to format result
    ${new_time}=    Add Time To Time    5 hours 3 minutes    15 minutes 30 seconds   result_format=timer
    #add ${70.0} as 70 seconds i.e., 1 minute 10 seconds
    Should Be Equal    ${new_time}    05:18:30.000

    ${new_time}=    Add Time To Time    5 hours 3 minutes    ${70.0}    result_format=timer
    #add ${70.0} as 70 seconds i.e., 1 minute 10 seconds
    Should Be Equal    ${new_time}    05:04:10.000

Subtract Time from Time Test

    ${new_time}=    Subtract Time From Time    04:00:00.000    1 hour    result_format=verbose
    Should Be Equal    ${new_time}    3 hours
    ${new_time}=    Subtract Time From Time    02:00:00.000    1 hour    result_format=verbose
    Should Be Equal    ${new_time}    1 hour    #singular for single hour

    ${new_time}=    Subtract Time From Time    5 hours 3 minutes    4 minutes    result_format=timer
    Should Be Equal    ${new_time}    04:59:00.000

    ${new_time}=    Subtract Time From Time    5 hours 3 minutes    ${90.0}    result_format=timer
    #${90.0} is 90 seconds i.e 1 minute 30 seconds
    Should Be Equal    ${new_time}    05:01:30.000

Subtract Time from Date Test
    ${new_date_time}=    Subtract Time From Date    ${Date_1}    1 hour    exclude_millis=Yes
    #exclude_millis=Yes will remove milliseconds from result
    Should Be Equal    ${new_date_time}    2025-04-15 20:45:12

    ${new_date_time}=    Subtract Time From Date   ${datetime(2025, 4, 15, 21, 45, 12)}    ${timedelta(hours=1)}    exclude_millis=Yes
    Should Be Equal    ${new_date_time}    2025-04-15 20:45:12

    ${new_date_time}=    Subtract Time From Date   ${datetime(2025, 4, 15, 21, 45, 12)}    ${timedelta(days=1)}    exclude_millis=Yes
    Should Be Equal    ${new_date_time}    2025-04-14 21:45:12


    ${new_date_time}=    Subtract Time From Date   21:47:13 2025.04.15   01:02:01.000    result_format=%H:%M:%S %Y.%m.%d    date_format=%H:%M:%S %Y.%m.%d
    Should Be Equal    ${new_date_time}    20:45:12 2025.04.15

Subtract Date from Date Test
    ${new_date_time}=    Subtract Date From Date    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    ${datetime(2025, 4, 15, 20, 45, 12, 123000)}    result_format=verbose
    Should Be Equal    ${new_date_time}    1 hour

    ${new_date_time}=    Subtract Date From Date    ${datetime(2025, 4, 15, 20, 45, 12, 123000)}    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    result_format=verbose
    Should Be Equal    ${new_date_time}    - 1 hour

    ${new_date_time}=    Subtract Date From Date    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    ${datetime(2025, 4, 15, 20, 45, 12, 123000)}    result_format=number
    # the result is 1 hr which is 3600 seconds
    ${type}=    Evaluate    type($new_date_time)    #<class 'float'>
    Should Be Equal    ${new_date_time}    ${3600.0}    # giving like "3600.0" will be considered as string

    ${new_date_time}=    Subtract Date From Date    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    ${datetime(2025, 4, 15, 20, 45, 12, 123000)}    result_format=timer
    Should Be Equal    ${new_date_time}    01:00:00.000

    ${new_date_time}=    Subtract Date From Date    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    ${datetime(2025, 4, 15, 20, 45, 12, 123000)}    result_format=compact
    Should Be Equal    ${new_date_time}    1h

     ${new_date_time}=    Subtract Date From Date    ${datetime(2025, 4, 15, 21, 45, 12, 123000)}    ${datetime(2025, 3, 10, 10, 15, 42, 100000)}    result_format=verbose
    Should Be Equal    ${new_date_time}    36 days 11 hours 29 minutes 30 seconds 23 milliseconds

    ${new_date_time}=    Subtract Date From Date    22:45:12 2025.04.15    2025-04-15 21:43:11   result_format=timer    date1_format=%H:%M:%S %Y.%m.%d    date2_format=%Y-%m-%d %H:%M:%S
    Should Be Equal    ${new_date_time}    01:02:01.000

Test for Get Current Date keyword
    ${date}=    Get Current Date        #default timestamp will be returned
    ${date}=    Get Current Date    UTC
    ${india_time1}=    Get Current Date    UTC    05:30:00
    ${india_time2}=    Get Current Date    UTC    5 hours 30 minutes
    ${date1}=    Get Current Date    UTC    result_format=datetime
    Should Be Equal    ${date1.year}    ${2025}
    ${india_time1}=    Get Current Date    result_format=%d.%m.%Y
    ${india_time1}=    Get Current Date    result_format=epoch

Test for Convert Date Keyword
    ${date}=    Convert Date    20250415 12:05:03.111
    Should Be Equal    ${date}    2025-04-15 12:05:03.111
    ${date}=    Convert Date    ${date}    epoch
    ${date}=    Convert Date    4.15.2025 12:05    exclude_millis=Yes    date_format=%m.%d.%Y %H:%M
    Should Be Equal    ${date}    2025-04-15 12:05:00

Test for Convert time Keyword
     ${time}=    Convert Time    10 seconds
     Should Be Equal    ${time}    ${10}
     
     ${time}=    Convert Time    1:00:01    result_format=verbose
     Should Be Equal    ${time}    1 hour 1 second

     ${time}=    Convert Time    2:15:11    result_format=verbose
     Should Be Equal    ${time}    2 hours 15 minutes 11 seconds
     
     ${time}=    Convert Time    ${3661.0}    timer    exclude_millis=Yes    #argument is in seconds
     Should Be Equal    ${time}    01:01:01

     ${time}=    Convert Time    ${75.5}    timer    exclude_millis=Yes    #if seconds value >.5 then it will rounded off
     Should Be Equal    ${time}    00:01:16
        