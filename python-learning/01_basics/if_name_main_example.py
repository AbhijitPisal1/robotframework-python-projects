"""
================================================================================
Understanding: if __name__ == "__main__"
================================================================================

1️. Introduction
----------------
- Every Python file (.py) has a special variable called __name__.
- When a file is run directly (python myfile.py), Python sets:
      __name__ = "__main__"
- When the file is imported, Python sets:
      __name__ = "filename"
- This allows Python to determine how the file is being used.

--------------------------------------------------------------------------------

2️. Purpose
-----------
- The check:
      if __name__ == "__main__":
  ensures that certain code runs only when the file is executed directly, not when imported.
- This is useful for testing, printing, or setup code.

--------------------------------------------------------------------------------

3️. Example Without __main__
----------------------------
# tools.py
print("Running tools.py")

def add(a, b):
    return a + b

# Importing this file elsewhere will still print "Running tools.py"

--------------------------------------------------------------------------------

4️. Example With __main__
-------------------------
# tools.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Running tools.py directly")
    print(add(2, 3))

# Running the file directly prints output.
# Importing it elsewhere does not execute the code automatically.

--------------------------------------------------------------------------------

5️. When to Use
---------------
| Situation                       | Use __main__? | Reason                        |
|---------------------------------|---------------|-------------------------------|
| Small personal script            | ❌ No         | Only run directly             |
| Module/library                   | ✅ Yes        | Prevents unwanted execution   |
| Script usable both directly & imported | ✅ Yes  | Best practice                 |
| Jupyter notebook / interactive  | ❌ No         | Not imported anyway           |

--------------------------------------------------------------------------------

6️. Explanation in Simple Terms
-------------------------------
- “Run this code only if this file is executed directly.”
- Helps separate test/demo code from reusable functions.

--------------------------------------------------------------------------------

7️. Prevalence
--------------
- Common in reusable files, libraries, and command-line tools.
- Not necessary for one-off scripts.

--------------------------------------------------------------------------------

8️. Summary
-----------
- Without __main__: all code runs automatically.
- With __main__: only selected code runs when executed directly.
- Use in reusable or importable files.
- Skip for quick or one-time scripts.

================================================================================
"""
# File: calculator.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print("Testing calculator functions...")
    print(add(2, 3))
    print(sub(5, 2))

# ➤ Running `python calculator.py`  --> prints tests
# ➤ Importing `calculator` elsewhere  --> no auto print
