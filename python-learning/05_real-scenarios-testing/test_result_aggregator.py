"""
Problem Statement:
------------------
Given a list of test results, summarize how many passed, failed, and skipped.
Also return a list of failed test names.

What it tests:
--------------
- Dictionary and list operations
- Counting and conditional filtering
"""

def summarize_results(results):
    summary = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    failed = []

    for test in results:
        status = test.get("status")
        name = test.get("test_name")
        if status in summary:
            summary[status] += 1
        if status == "FAIL":
            failed.append(name)
    return summary, failed


# Example usage
if __name__ == "__main__":
    test_data = [
        {"test_name": "LoginTest", "status": "PASS"},
        {"test_name": "SignupTest", "status": "FAIL"},
        {"test_name": "CartTest", "status": "PASS"}
    ]
    print(summarize_results(test_data))
