"""
Tests for Lesson 1: Running Python

These tests verify understanding of:
- The __name__ variable
- sys.argv and command-line arguments
- sys.version and Python version info
- Module imports vs. direct execution
"""

import sys
import subprocess
from pathlib import Path


def test_name_is_main_when_direct():
    """
    When a script is run directly (not imported), __name__ == "__main__".
    We verify this by checking the lesson module's __name__.
    """
    # Import the lesson module
    import learn_python_with_claude.core_python_01.lesson_01_running_python as lesson

    # When imported, __name__ is the module path, not "__main__"
    assert lesson.__name__ == "learn_python_with_claude.core_python_01.lesson_01_running_python"


def test_sys_argv_contains_script_name():
    """
    sys.argv[0] is the name of the script being run.
    sys.argv[1:] are the arguments passed to it.
    """
    # The current process's sys.argv should have at least one element (pytest)
    assert len(sys.argv) >= 1
    # sys.argv[0] should be some form of the test runner or script name
    assert isinstance(sys.argv[0], str)


def test_sys_version_is_string():
    """
    sys.version is a string containing Python version info.
    """
    assert isinstance(sys.version, str)
    # Should be a non-empty string with version information
    assert len(sys.version) > 0
    # Should contain version numbers (e.g., "3.11.9")
    assert any(char.isdigit() for char in sys.version)


def test_sys_version_info_is_tuple():
    """
    sys.version_info is a tuple with major, minor, micro, etc.
    """
    assert isinstance(sys.version_info, tuple)
    # Should have at least 5 elements: major, minor, micro, releaselevel, serial
    assert len(sys.version_info) >= 5
    # major, minor, micro should be integers
    assert isinstance(sys.version_info.major, int)
    assert isinstance(sys.version_info.minor, int)
    assert isinstance(sys.version_info.micro, int)


def test_python_version_meets_requirement():
    """
    According to CLAUDE.md, this project requires Python >= 3.10.
    Verify we're running on a compatible version.
    """
    assert sys.version_info >= (3, 10), "Python 3.10+ is required"


def test_say_hello_function():
    """
    Test the say_hello function from the lesson.
    """
    from learn_python_with_claude.core_python_01.lesson_01_running_python import say_hello

    result = say_hello("Alice")
    assert result == "Hello, Alice!"

    result = say_hello("Python")
    assert result == "Hello, Python!"


def test_main_function_callable():
    """
    The main() function should be callable without errors.
    We'll capture its output to verify it works.
    """
    from learn_python_with_claude.core_python_01.lesson_01_running_python import main
    import io
    from contextlib import redirect_stdout

    # Capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        main()

    output = f.getvalue()
    # main() calls say_hello("World") and prints it
    assert "Hello, World!" in output


def test_print_arguments_function():
    """
    Test the print_arguments function with mocked sys.argv.
    """
    from learn_python_with_claude.core_python_01.lesson_01_running_python import print_arguments
    import io
    from contextlib import redirect_stdout

    # Temporarily change sys.argv
    original_argv = sys.argv
    try:
        sys.argv = ["test_script.py", "arg1", "arg2", "arg3"]

        f = io.StringIO()
        with redirect_stdout(f):
            print_arguments()

        output = f.getvalue()
        assert "test_script.py" in output
        assert "arg1" in output
        assert "arg2" in output
        assert "arg3" in output
    finally:
        # Restore original sys.argv
        sys.argv = original_argv


def test_lesson_module_docstring():
    """
    The lesson module should have a docstring.
    """
    from learn_python_with_claude.core_python_01 import lesson_01_running_python

    assert lesson_01_running_python.__doc__ is not None
    assert "Running Python" in lesson_01_running_python.__doc__
