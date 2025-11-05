"""
Problem Statement:
------------------
You are given a log file containing lines like:
[2025-11-05 12:15:00] INFO User login successful
[2025-11-05 12:16:20] ERROR Invalid password attempt

Write a function that:
- Counts total number of ERROR and INFO entries.
- Prints timestamps of all ERROR events.

What it tests:
--------------
- File I/O
- String parsing
- Filtering and summarization
"""

def analyze_log(file_path: str):
    info_count = 0
    error_count = 0
    error_times = []

    with open(file_path, 'r') as file:
        for line in file:
            if "INFO" in line:
                info_count += 1
            elif "ERROR" in line:
                error_count += 1
                time = line.split(']')[0].strip('[')
                error_times.append(time)

    print(f"INFO count: {info_count}")
    print(f"ERROR count: {error_count}")
    print("Error timestamps:", error_times)
