*** Settings ***
Documentation    This test deals with common keywords used from Operating system library
...            	 library providing keywords for operating system related tasks
...              official documentation : https://robotframework.org/robotframework/latest/libraries/OperatingSystem.html
Library    OperatingSystem
Library    Process

*** Variables ***
${FILE_PATH}       C:\\filetest1\\test1.txt
${DIRECTORY}       C:/filetest
${NEW_FILE_COPY}   ${DIRECTORY}\\first_test\\newfile_copy.txt
${TEMP_FILE}       ${DIRECTORY}\\second_test\\tempfile.txt
${PERMISSIONS}     755

*** Test Cases ***
File Exists Check
    [Documentation]    This test case checks if a file exists.
    File Should Exist    ${FILE_PATH}

Create Directory
    [Documentation]    This test case creates and removes a directory.
    Create Directory    ${DIRECTORY}

Copy A File
    [Documentation]    This test case copies a file to a new location.
    Copy File    ${FILE_PATH}    ${NEW_FILE_COPY}
    File Should Exist    ${NEW_FILE_COPY}

Move A File
    [Documentation]    This test case moves a file to a new location.
    Move File    ${NEW_FILE_COPY}    ${TEMP_FILE}
    File Should Not Exist    ${NEW_FILE_COPY}
    File Should Exist    ${TEMP_FILE}

Check File Properties
    [Documentation]    This test case checks the properties of a file (size and permissions).
    ${size}=    Get File Size    ${TEMP_FILE}
    Log    File size: ${size}

Create And Remove Temporary File
    [Documentation]    This test case creates a temporary file and then removes it.
    Create File    ${TEMP_FILE}    Temporary test file.
    File Should Exist    ${TEMP_FILE}
    Remove File    ${TEMP_FILE}
    File Should Not Exist    ${TEMP_FILE}

Read File Content
    [Documentation]    This test case reads the content of a file.
    ${content}=    Get File    ${FILE_PATH}
    Log    File content: ${content}

Check Directory Exists
    [Documentation]    This test case checks if a directory exists.
    Directory Should Exist    ${DIRECTORY}

List Files In Directory
    [Documentation]    This test case lists all files in a directory.
    ${files}=    List Files In Directory    ${DIRECTORY}
    Log    Files in directory: ${files}

Remove Directory
    Directory Should Exist    ${DIRECTORY}
    Remove Directory    ${DIRECTORY}    recursive=True
    Directory Should Not Exist    ${DIRECTORY}