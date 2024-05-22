'''
Exercise 7: The Server's Graceful Exit

In server applications, unexpected exceptions can occur, and it's crucial to handle these gracefully to prevent data loss and ensure necessary cleanup is performed.
Your task is to simulate a server's main operation loop and implement a mechanism that guarantees a graceful shutdown, even if an error occurs.

**Instructions**:

1. Simulate a server's main loop with a placeholder comment.
2. Use a 'try-except-finally' block to handle any potential exceptions during the server's runtime.
3. In the 'except' block, catch a general exception and print an error message.
4. In the 'finally' block, perform cleanup operations and print a shutdown message.

**Hints**:

- The 'finally' block is executed after 'try' and 'except' blocks, regardless of whether an exception was raised or not.
- Use the 'finally' block to include any code that you want to execute regardless of exceptions, such as closing files or releasing resources.
'''

try:
    print("Server is running...")
    # simulate an error
    raise Exception("Unexpected error!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Performing cleanup operations...")
    print("Shutting down server gracefully")