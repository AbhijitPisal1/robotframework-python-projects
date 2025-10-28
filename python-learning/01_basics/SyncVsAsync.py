"""
This script demonstrates the difference between synchronous (blocking) 
and asynchronous (non-blocking) execution in Python.
"""
import time
def timestamp():
    """Return current time in HH:MM:SS format."""
    return time.strftime("%H:%M:%S", time.localtime())

# ---------- Synchronous Example ----------

def task_sync(name):
    """
    Perform a simple synchronous task.
    
    Each call to 'task_sync' blocks the program using time.sleep(),
    meaning the next task starts only after the previous one finishes.
    """
    print(f"[{timestamp()}] Starting {name}")
    time.sleep(2)  # Blocking: the program waits here for 2 seconds
    print(f"[{timestamp()}] Finished {name}")


print("Synchronous Execution:\n")
task_sync("book 1")
task_sync("book 2")


# Expected Output (executed one after another):
# [19:49:51] Starting book 1
# [19:49:53] Finished book 1
# [19:49:53] Starting book 2
# [19:49:55] Finished book 2

# ---------- Asynchronous Example ----------
import asyncio

async def task_async(name):
    """
    Perform an asynchronous task using asyncio.
    
    'await asyncio.sleep(2)' is non-blocking — it suspends the coroutine,
    allowing other tasks to run concurrently during the wait period.
    """
    print(f"[{timestamp()}] Started Downloading {name}")
    await asyncio.sleep(2)  # Non-blocking: allows other tasks to run
    print(f"[{timestamp()}] Finished Downloading {name}")


async def main():
    """
    Main coroutine that runs multiple asynchronous tasks concurrently.
    
    'asyncio.gather()' schedules and runs both tasks at the same time,
    demonstrating concurrent execution within a single thread.
    """
    await asyncio.gather(task_async("file 1"), task_async("file 2"))


print("\nAsynchronous Execution:\n")
asyncio.run(main())

# Expected Output (executed concurrently):
# [19:49:55] Started Downloading file 1
# [19:49:55] Started Downloading file 2
# [19:49:57] Finished Downloading file 1
# [19:49:57] Finished Downloading file 2
