"""
Tests for Lesson 3: Data Types

Covers:
- Numeric types (int, float, complex)
- String type and operations
- Boolean type
- Type conversion
- Numeric operations
- String methods
"""

import pytest
from src.learn_python_with_claude.lesson_03_data_types import (
    explain_integers,
    explain_floats,
    explain_complex_numbers,
    explain_strings,
    explain_string_indexing,
    explain_booleans,
    explain_type_conversion,
    explain_numeric_operations,
    explain_string_methods,
    exercise_1,
    exercise_2,
    exercise_3,
    exercise_4,
    exercise_5,
)


class TestIntegerType:
    """Test integer type and operations."""

    def test_positive_integer(self):
        """Positive integers work correctly."""
        x = 42
        assert x == 42
        assert type(x) == int

    def test_negative_integer(self):
        """Negative integers work correctly."""
        x = -10
        assert x == -10
        assert type(x) == int

    def test_zero(self):
        """Zero is an integer."""
        x = 0
        assert x == 0
        assert type(x) == int

    def test_large_integer(self):
        """Python handles arbitrarily large integers."""
        large = 10**100
        assert isinstance(large, int)
        assert large > 0

    def test_binary_notation(self):
        """Binary literals work."""
        binary = 0b1010
        assert binary == 10

    def test_octal_notation(self):
        """Octal literals work."""
        octal = 0o77
        assert octal == 63

    def test_hexadecimal_notation(self):
        """Hexadecimal literals work."""
        hexadecimal = 0xFF
        assert hexadecimal == 255

    def test_explain_integers(self):
        """Complete integer explanation."""
        p, n, z, b, bi, o, h = explain_integers()
        assert p > 0
        assert n < 0
        assert z == 0
        assert bi == 10


class TestFloatType:
    """Test float type and operations."""

    def test_basic_float(self):
        """Basic float values."""
        x = 3.14
        assert x == 3.14
        assert type(x) == float

    def test_negative_float(self):
        """Negative floats work."""
        x = -2.5
        assert x == -2.5

    def test_scientific_notation(self):
        """Scientific notation works."""
        scientific = 1.23e-4
        assert abs(scientific - 0.000123) < 1e-10

    def test_large_float(self):
        """Large floats work."""
        large = 1e10
        assert large == 10000000000.0

    def test_small_float(self):
        """Small floats work."""
        small = 1e-10
        assert small < 1e-9

    def test_float_precision(self):
        """Floats have limited precision."""
        result = 0.1 + 0.2
        # Should be approximately 0.3
        assert abs(result - 0.3) < 1e-10

    def test_explain_floats(self):
        """Complete float explanation."""
        pi, nf, zf, sci, large, small, result = explain_floats()
        assert isinstance(pi, float)
        assert isinstance(large, float)


class TestComplexType:
    """Test complex number type."""

    def test_basic_complex(self):
        """Basic complex numbers."""
        c = 3 + 4j
        assert c.real == 3.0
        assert c.imag == 4.0

    def test_purely_imaginary(self):
        """Purely imaginary numbers."""
        c = 2j
        assert c.real == 0.0
        assert c.imag == 2.0

    def test_complex_function(self):
        """complex() function."""
        c = complex(5, 6)
        assert c.real == 5.0
        assert c.imag == 6.0

    def test_complex_addition(self):
        """Complex number addition."""
        c1 = 3 + 4j
        c2 = 2 + 1j
        result = c1 + c2
        assert result == 5 + 5j

    def test_explain_complex(self):
        """Complete complex number explanation."""
        c1, c2, c3, real, imag, addition = explain_complex_numbers()
        assert c1.real == 3.0
        assert c1.imag == 4.0


class TestStringType:
    """Test string type and basic operations."""

    def test_single_quote_string(self):
        """Strings with single quotes."""
        s = 'Hello'
        assert s == 'Hello'
        assert type(s) == str

    def test_double_quote_string(self):
        """Strings with double quotes."""
        s = "World"
        assert s == "World"

    def test_triple_quote_string(self):
        """Triple-quoted strings."""
        s = '''Multi
        line
        string'''
        assert '\n' in s

    def test_empty_string(self):
        """Empty string."""
        s = ""
        assert s == ""
        assert len(s) == 0

    def test_string_with_newline(self):
        """Strings with escape sequences."""
        s = "Hello\nWorld"
        assert '\n' in s
        assert s.count('\n') == 1

    def test_string_concatenation(self):
        """String concatenation."""
        s = "Hello" + " " + "World"
        assert s == "Hello World"

    def test_string_repetition(self):
        """String repetition."""
        s = "Ha" * 3
        assert s == "HaHaHa"

    def test_raw_string(self):
        """Raw strings don't escape backslashes."""
        s = r"C:\Users\Name"
        assert s == "C:\\Users\\Name"


class TestStringIndexingSlicing:
    """Test string indexing and slicing."""

    def test_string_indexing_positive(self):
        """Positive indexing."""
        s = "Python"
        assert s[0] == 'P'
        assert s[1] == 'y'
        assert s[2] == 't'

    def test_string_indexing_negative(self):
        """Negative indexing."""
        s = "Python"
        assert s[-1] == 'n'
        assert s[-2] == 'o'
        assert s[-6] == 'P'

    def test_string_slicing_basic(self):
        """Basic string slicing."""
        s = "Python"
        assert s[0:3] == "Pyt"
        assert s[2:] == "thon"
        assert s[:3] == "Pyt"

    def test_string_slicing_step(self):
        """String slicing with step."""
        s = "Python"
        assert s[::2] == "Pto"
        assert s[1::2] == "yhn"

    def test_string_reversal(self):
        """Reversing strings with slicing."""
        s = "Python"
        assert s[::-1] == "nohtyP"

    def test_string_length(self):
        """String length."""
        s = "Python"
        assert len(s) == 6
        assert len("") == 0

    def test_explain_string_indexing(self):
        """Complete indexing explanation."""
        f, s, l, sl2, s1, s2, s3, s4, s5, ln = explain_string_indexing()
        assert f == 'P'
        assert l == 'n'
        assert ln == 6


class TestBooleanType:
    """Test boolean type."""

    def test_true_value(self):
        """True boolean."""
        b = True
        assert b is True
        assert type(b) == bool

    def test_false_value(self):
        """False boolean."""
        b = False
        assert b is False
        assert type(b) == bool

    def test_comparison_true(self):
        """Comparisons return True."""
        assert 5 > 3
        assert "Hello" == "Hello"
        assert 10 >= 10

    def test_comparison_false(self):
        """Comparisons return False."""
        assert not (5 < 3)
        assert not ("Hello" == "World")
        assert not (10 < 10)

    def test_and_operation(self):
        """AND operation."""
        assert (True and True) == True
        assert (True and False) == False
        assert (False and False) == False

    def test_or_operation(self):
        """OR operation."""
        assert True or True == True
        assert True or False == True
        assert False or False == False

    def test_not_operation(self):
        """NOT operation."""
        assert not True == False
        assert not False == True

    def test_truthy_values(self):
        """Truthy values."""
        assert bool(42)
        assert bool("Hello")
        assert bool([1, 2, 3])

    def test_falsy_values(self):
        """Falsy values."""
        assert not bool(0)
        assert not bool("")
        assert not bool([])
        assert not bool(None)


class TestTypeConversion:
    """Test type conversion functions."""

    def test_string_to_int(self):
        """Convert string to integer."""
        result = int("42")
        assert result == 42
        assert type(result) == int

    def test_string_to_float(self):
        """Convert string to float."""
        result = float("3.14")
        assert abs(result - 3.14) < 0.01
        assert type(result) == float

    def test_int_to_float(self):
        """Convert integer to float."""
        result = float(42)
        assert result == 42.0
        assert type(result) == float

    def test_float_to_int(self):
        """Convert float to integer (truncates)."""
        result = int(3.99)
        assert result == 3  # Truncated, not rounded
        assert type(result) == int

    def test_int_to_string(self):
        """Convert integer to string."""
        result = str(42)
        assert result == "42"
        assert type(result) == str

    def test_float_to_string(self):
        """Convert float to string."""
        result = str(3.14)
        assert "3.14" in result
        assert type(result) == str

    def test_bool_to_string(self):
        """Convert boolean to string."""
        assert str(True) == "True"
        assert str(False) == "False"

    def test_to_boolean_truthy(self):
        """Convert to boolean (truthy)."""
        assert bool(42)
        assert bool("hello")
        assert bool([1, 2])

    def test_to_boolean_falsy(self):
        """Convert to boolean (falsy)."""
        assert not bool(0)
        assert not bool("")
        assert not bool([])

    def test_explain_type_conversion(self):
        """Complete type conversion explanation."""
        results = explain_type_conversion()
        assert isinstance(results[0], int)  # str to int


class TestNumericOperations:
    """Test numeric operations."""

    def test_addition(self):
        """Addition operation."""
        assert 10 + 3 == 13
        assert 10.5 + 3.5 == 14.0

    def test_subtraction(self):
        """Subtraction operation."""
        assert 10 - 3 == 7
        assert 10.5 - 3.5 == 7.0

    def test_multiplication(self):
        """Multiplication operation."""
        assert 10 * 3 == 30
        assert 10.0 * 3.0 == 30.0

    def test_division(self):
        """Division operation."""
        result = 10 / 3
        assert abs(result - 3.333333) < 0.001

    def test_floor_division(self):
        """Floor division operation."""
        assert 10 // 3 == 3
        assert 10 // 4 == 2

    def test_modulo(self):
        """Modulo (remainder) operation."""
        assert 10 % 3 == 1
        assert 10 % 4 == 2

    def test_power(self):
        """Power (exponentiation) operation."""
        assert 2 ** 3 == 8
        assert 3 ** 2 == 9

    def test_order_of_operations(self):
        """PEMDAS order of operations."""
        assert 2 + 3 * 4 == 14  # Not 20
        assert (2 + 3) * 4 == 20

    def test_comparison_operations(self):
        """Comparison operations."""
        assert 5 == 5
        assert 5 != 3
        assert 5 < 10
        assert 10 > 5
        assert 5 <= 5
        assert 10 >= 10

    def test_chained_comparison(self):
        """Chained comparisons."""
        assert 5 < 10 < 15
        assert not (5 > 10 < 15)


class TestStringMethods:
    """Test string methods."""

    def test_upper(self):
        """upper() method."""
        assert "hello".upper() == "HELLO"
        assert "Hello World".upper() == "HELLO WORLD"

    def test_lower(self):
        """lower() method."""
        assert "HELLO".lower() == "hello"
        assert "Hello World".lower() == "hello world"

    def test_title(self):
        """title() method."""
        assert "hello world".title() == "Hello World"

    def test_capitalize(self):
        """capitalize() method."""
        assert "hello world".capitalize() == "Hello world"

    def test_find(self):
        """find() method."""
        s = "Hello World"
        assert s.find("World") == 6
        assert s.find("xyz") == -1

    def test_replace(self):
        """replace() method."""
        s = "Hello World"
        assert s.replace("World", "Python") == "Hello Python"

    def test_split(self):
        """split() method."""
        s = "Hello World Python"
        assert s.split() == ["Hello", "World", "Python"]
        assert "a,b,c".split(",") == ["a", "b", "c"]

    def test_join(self):
        """join() method."""
        words = ["Hello", "World"]
        assert " ".join(words) == "Hello World"
        assert "-".join(["a", "b", "c"]) == "a-b-c"

    def test_strip(self):
        """strip() method."""
        assert "  hello  ".strip() == "hello"
        assert "hello".strip() == "hello"

    def test_isdigit(self):
        """isdigit() method."""
        assert "123".isdigit()
        assert not "12a".isdigit()

    def test_isalpha(self):
        """isalpha() method."""
        assert "abc".isalpha()
        assert not "ab1".isalpha()

    def test_isalnum(self):
        """isalnum() method."""
        assert "abc123".isalnum()
        assert not "abc 123".isalnum()

    def test_format(self):
        """format() method."""
        assert "Hello {}".format("World") == "Hello World"
        assert "{} {}".format("Hello", "World") == "Hello World"

    def test_f_string(self):
        """F-strings."""
        name = "World"
        assert f"Hello {name}" == "Hello World"


class TestExercises:
    """Test lesson exercises."""

    def test_exercise_1_numeric_types(self):
        """Exercise 1: Different numeric types."""
        integer, floating, complex_num = exercise_1()
        assert isinstance(integer, int)
        assert isinstance(floating, float)
        assert isinstance(complex_num, complex)

    def test_exercise_2_string_manipulation(self):
        """Exercise 2: String manipulation."""
        message, upper, reversed_str, first_word = exercise_2()
        assert message == "Python Programming"
        assert upper == "PYTHON PROGRAMMING"
        assert reversed_str == "gnimmargorP nohtyP"
        assert first_word == "Python"

    def test_exercise_3_type_conversion(self):
        """Exercise 3: Type conversion."""
        to_int, to_float, back_to_str = exercise_3()
        assert to_int == 123
        assert to_float == 123.0
        assert "123" in back_to_str

    def test_exercise_4_string_indexing(self):
        """Exercise 4: String indexing and slicing."""
        first, last, middle, every_other = exercise_4()
        assert first == 'e'
        assert last == 'n'
        assert middle == 'cati'
        assert every_other == 'euain'

    def test_exercise_5_boolean_operations(self):
        """Exercise 5: Boolean operations."""
        a, b, c, d, e = exercise_5()
        assert a is False  # True and False
        assert b is True   # True or False
        assert c is False  # not True
        assert d is True   # bool(42)
        assert e is False  # bool(0)


class TestIntegration:
    """Integration tests combining multiple concepts."""

    def test_mixed_type_operations(self):
        """Operations with mixed types."""
        x = 42  # int
        y = 3.14  # float
        result = x + y
        assert isinstance(result, float)
        assert abs(result - 45.14) < 0.01

    def test_string_number_conversion(self):
        """String to number and back."""
        original = "42"
        as_int = int(original)
        back_to_string = str(as_int)
        assert original == back_to_string

    def test_boolean_in_operations(self):
        """Boolean values in operations."""
        assert True + True == 2  # True is 1
        assert True * 5 == 5
        assert False + 10 == 10


class TestLessonStructure:
    """Test that lesson follows expected structure."""

    def test_lesson_module_exists(self):
        """Lesson module can be imported."""
        from src.learn_python_with_claude import lesson_03_data_types
        assert lesson_03_data_types is not None

    def test_lesson_has_docstring(self):
        """Lesson module has a docstring."""
        from src.learn_python_with_claude import lesson_03_data_types
        assert lesson_03_data_types.__doc__ is not None
        assert "Lesson 3" in lesson_03_data_types.__doc__

    def test_all_sections_present(self):
        """All explain functions exist."""
        assert callable(explain_integers)
        assert callable(explain_floats)
        assert callable(explain_complex_numbers)
        assert callable(explain_strings)
        assert callable(explain_string_indexing)
        assert callable(explain_booleans)
        assert callable(explain_type_conversion)
        assert callable(explain_numeric_operations)
        assert callable(explain_string_methods)

    def test_all_exercises_exist(self):
        """All exercises exist."""
        assert callable(exercise_1)
        assert callable(exercise_2)
        assert callable(exercise_3)
        assert callable(exercise_4)
        assert callable(exercise_5)
