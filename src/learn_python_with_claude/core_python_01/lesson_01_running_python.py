"""
Lesson 1: Running Python

The three main ways to run Python code:
1. The Python interpreter (interactive REPL)
2. Running a .py file directly
3. Importing modules and executing code in other contexts
"""

# ============================================================================
# Part 1: The Python Interpreter (REPL)
# ============================================================================
# REPL = Read, Evaluate, Print, Loop
#
# To start the interactive interpreter, run:
#   python
#   python3
#   py  (on Windows)
#
# The REPL waits for you to type Python code, executes it, prints the result,
# and waits for the next line.
#
# Example (in a terminal):
#   >>> 2 + 2
#   4
#   >>> name = "Python"
#   >>> print(f"Hello, {name}!")
#   Hello, Python!
#   >>> exit()  # or Ctrl+D on Unix, Ctrl+Z + Enter on Windows

# In the REPL, the underscore (_) holds the last printed expression:
#   >>> 5 + 5
#   10
#   >>> _ * 2
#   20


# ============================================================================
# Part 2: Running a .py File
# ============================================================================
# A .py file is a plain text file containing Python code.
# To run it:
#
#   python script.py
#   python3 script.py
#   py script.py  (on Windows)
#
# Python reads the file top to bottom and executes every statement.
#
# Example file structure:

def say_hello(name):
    """A simple function to greet someone."""
    return f"Hello, {name}!"


def main():
    """The entry point of the script."""
    result = say_hello("World")
    print(result)


# Only run this if the file is executed directly, not imported:
if __name__ == "__main__":
    main()


# ============================================================================
# Part 3: Key Concepts
# ============================================================================
#
# The __name__ variable:
#   - When you run a .py file directly: __name__ == "__main__"
#   - When you import a module: __name__ == "module_name"
#
# This lets you write code that behaves differently depending on context:
#
#   if __name__ == "__main__":
#       # This code runs only when the file is executed directly
#       main()


# ============================================================================
# Part 4: Running with Command-Line Arguments
# ============================================================================
# Scripts often need input. You can pass arguments from the command line:
#
#   python script.py arg1 arg2
#
# Inside the script, access them via sys.argv:

import sys


def print_arguments():
    """Print all command-line arguments."""
    print(f"Script name: {sys.argv[0]}")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")


# Example: if you run `python script.py hello world`
# Output:
#   Script name: script.py
#   Argument 1: hello
#   Argument 2: world


# ============================================================================
# Part 5: Python Version
# ============================================================================
# Check your Python version:
#
#   python --version
#   python3 --version
#   py --version  (on Windows)
#
# In a script, check it with sys.version or sys.version_info:

print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info}")


# ============================================================================
# Summary
# ============================================================================
# Three ways to run Python:
#
# 1. REPL (interactive)
#    - Good for: testing, learning, quick experiments
#    - Start with: python
#
# 2. .py file (script)
#    - Good for: repeatable tasks, larger programs
#    - Run with: python script.py
#
# 3. Importing modules
#    - Good for: reusing code across projects
#    - Use when: you want to share code as a library
#
# Always use if __name__ == "__main__": in scripts to separate
# code that runs when executed vs. when imported.
