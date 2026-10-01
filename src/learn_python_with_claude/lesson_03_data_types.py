"""
Lesson 3: Data Types

Topics covered:
- Numeric types (int, float, complex)
- String type (str) and string operations
- Boolean type (bool)
- Type conversion
- Numeric operations and methods
- String methods and formatting

Python has several fundamental data types that represent different kinds of data.
Understanding these types is essential for writing correct programs.
"""


# ============================================================================
# SECTION 1: NUMERIC TYPES - INTEGERS
# ============================================================================

def explain_integers():
    """
    Integers are whole numbers without decimal points.
    In Python 3, there's only one integer type: int

    Integers can be:
    - Positive: 42
    - Negative: -10
    - Zero: 0
    - Large: 999999999999999999 (Python handles arbitrarily large integers)
    - Different bases: 0b (binary), 0o (octal), 0x (hexadecimal)
    """

    # Basic integers
    positive = 42
    negative = -10
    zero = 0

    # Large integers
    big_number = 10**100  # Python handles this easily

    # Different bases
    binary = 0b1010  # 10 in decimal
    octal = 0o77  # 63 in decimal
    hexadecimal = 0xFF  # 255 in decimal

    return positive, negative, zero, big_number, binary, octal, hexadecimal


# ============================================================================
# SECTION 2: NUMERIC TYPES - FLOATS
# ============================================================================

def explain_floats():
    """
    Floats are numbers with decimal points.
    They represent floating-point numbers (approximately).

    Floats can be:
    - Decimal: 3.14
    - Scientific notation: 1.23e-4
    - Negative: -2.5
    - Very large/small: 1e100, 1e-100

    Note: Floats have limited precision and can have rounding errors.
    """

    # Basic floats
    pi = 3.14
    negative_float = -2.5
    zero_float = 0.0

    # Scientific notation
    scientific = 1.23e-4  # 0.000123
    large = 1e10  # 10,000,000,000
    small = 1e-10  # 0.0000000001

    # Float precision
    result = 0.1 + 0.2  # Approximately 0.30000000000000004

    return pi, negative_float, zero_float, scientific, large, small, result


# ============================================================================
# SECTION 3: NUMERIC TYPES - COMPLEX
# ============================================================================

def explain_complex_numbers():
    """
    Complex numbers have real and imaginary parts.
    Format: a + bj (where a is real, b is imaginary)

    Complex numbers are used in:
    - Engineering
    - Physics
    - Signal processing
    - Mathematics
    """

    # Complex numbers
    c1 = 3 + 4j  # 3 real, 4 imaginary
    c2 = 2j  # Purely imaginary
    c3 = complex(5, 6)  # Using complex() function

    # Access real and imaginary parts
    real_part = c1.real  # 3.0
    imag_part = c1.imag  # 4.0

    # Operations
    addition = c1 + c2  # (3 + 6j)

    return c1, c2, c3, real_part, imag_part, addition


# ============================================================================
# SECTION 4: STRING TYPE
# ============================================================================

def explain_strings():
    """
    Strings are sequences of characters.
    Created with single quotes, double quotes, or triple quotes.

    Strings are immutable - once created, they cannot be changed.
    """

    # Different ways to create strings
    single_quote = 'Hello'
    double_quote = "World"
    triple_quote = '''This is a
    multi-line string'''

    # Empty string
    empty = ""

    # String with special characters
    with_newline = "Hello\nWorld"  # \n is newline
    with_tab = "Name\tAge"  # \t is tab
    with_quote = "He said \"Hi\""  # Escaped quotes

    # Raw strings (backslashes not escaped)
    raw_string = r"C:\Users\Name"

    # String concatenation
    concat = "Hello" + " " + "World"

    # String repetition
    repeated = "Ha" * 3  # "HaHaHa"

    return (single_quote, double_quote, triple_quote, empty,
            with_newline, with_tab, with_quote, raw_string, concat, repeated)


# ============================================================================
# SECTION 5: STRING INDEXING AND SLICING
# ============================================================================

def explain_string_indexing():
    """
    Strings are sequences - you can access individual characters.

    Indexing: Get character at position (0-based)
    Slicing: Get substring using [start:end:step]
    Negative indices: Count from the end (-1 is last character)
    """

    s = "Python"

    # Indexing (0-based)
    first = s[0]  # 'P'
    second = s[1]  # 'y'
    last = s[-1]  # 'n'
    second_last = s[-2]  # 'o'

    # Slicing [start:end:step]
    slice1 = s[0:3]  # "Pyt" (index 0, 1, 2)
    slice2 = s[2:]  # "thon" (from index 2 to end)
    slice3 = s[:3]  # "Pyt" (from start to index 2)
    slice4 = s[::2]  # "Pto" (every 2nd character)
    slice5 = s[::-1]  # "nohtyP" (reversed)

    # String length
    length = len(s)  # 6

    return first, second, last, second_last, slice1, slice2, slice3, slice4, slice5, length


# ============================================================================
# SECTION 6: BOOLEAN TYPE
# ============================================================================

def explain_booleans():
    """
    Boolean type represents True or False.

    Booleans are used in:
    - Conditional statements (if/elif/else)
    - Logical operations (and, or, not)
    - Comparisons

    Everything in Python has a "truthiness":
    - Falsy: False, 0, "", [], {}, None
    - Truthy: Everything else
    """

    # Boolean values
    true_value = True
    false_value = False

    # Boolean from comparisons
    comparison1 = 5 > 3  # True
    comparison2 = 10 == 5  # False
    comparison3 = "Hello" == "Hello"  # True

    # Logical operations
    and_result = True and True  # True
    or_result = True or False  # True
    not_result = not True  # False

    # Truthiness
    truthy_number = bool(42)  # True
    falsy_number = bool(0)  # False
    truthy_string = bool("Hello")  # True
    falsy_string = bool("")  # False

    return (true_value, false_value, comparison1, comparison2, comparison3,
            and_result, or_result, not_result, truthy_number, falsy_number,
            truthy_string, falsy_string)


# ============================================================================
# SECTION 7: TYPE CONVERSION
# ============================================================================

def explain_type_conversion():
    """
    Convert between different types using conversion functions:
    - int() - convert to integer
    - float() - convert to float
    - str() - convert to string
    - bool() - convert to boolean
    """

    # String to integer
    str_to_int = int("42")  # 42

    # String to float
    str_to_float = float("3.14")  # 3.14

    # Integer to float
    int_to_float = float(42)  # 42.0

    # Float to integer (truncates)
    float_to_int = int(3.99)  # 3 (truncated, not rounded)

    # Any type to string
    int_to_str = str(42)  # "42"
    float_to_str = str(3.14)  # "3.14"
    bool_to_str = str(True)  # "True"

    # Any type to boolean
    to_bool_1 = bool(42)  # True
    to_bool_2 = bool(0)  # False
    to_bool_3 = bool("hello")  # True
    to_bool_4 = bool("")  # False

    return (str_to_int, str_to_float, int_to_float, float_to_int,
            int_to_str, float_to_str, bool_to_str, to_bool_1, to_bool_2,
            to_bool_3, to_bool_4)


# ============================================================================
# SECTION 8: NUMERIC OPERATIONS
# ============================================================================

def explain_numeric_operations():
    """
    Common operations on numbers:
    - Arithmetic: +, -, *, /, //, %, **
    - Comparison: ==, !=, <, >, <=, >=
    - Assignment: +=, -=, *=, /=, etc.
    """

    # Arithmetic operations
    addition = 10 + 3  # 13
    subtraction = 10 - 3  # 7
    multiplication = 10 * 3  # 30
    division = 10 / 3  # 3.333...
    floor_division = 10 // 3  # 3 (integer division)
    modulo = 10 % 3  # 1 (remainder)
    power = 2 ** 3  # 8 (exponentiation)

    # Order of operations (PEMDAS)
    result = 2 + 3 * 4  # 14 (not 20)

    # Comparisons return booleans
    equal = 5 == 5  # True
    not_equal = 5 != 3  # True
    less_than = 5 < 10  # True
    greater_than = 10 > 5  # True
    less_equal = 5 <= 5  # True
    greater_equal = 10 >= 10  # True

    # Chained comparisons
    chained = 5 < 10 < 15  # True (10 is between 5 and 15)

    return (addition, subtraction, multiplication, division, floor_division,
            modulo, power, result, equal, not_equal, less_than, greater_than,
            less_equal, greater_equal, chained)


# ============================================================================
# SECTION 9: STRING METHODS
# ============================================================================

def explain_string_methods():
    """
    Strings have many useful methods.
    Methods are functions that belong to an object.
    Syntax: string.method()

    Remember: Strings are immutable, so methods return new strings.
    """

    s = "Hello World"

    # Case methods
    upper = s.upper()  # "HELLO WORLD"
    lower = s.lower()  # "hello world"
    title = s.title()  # "Hello World"
    capitalize = s.capitalize()  # "Hello world"

    # Search methods
    contains = "World" in s  # True
    index = s.find("World")  # 6

    # Replace and split
    replaced = s.replace("World", "Python")  # "Hello Python"
    words = s.split()  # ["Hello", "World"]

    # Strip whitespace
    padded = "  Hello  "
    stripped = padded.strip()  # "Hello"

    # Check type
    is_digit = "123".isdigit()  # True
    is_alpha = "abc".isalpha()  # True
    is_alpha_num = "abc123".isalnum()  # True

    # String formatting (joining)
    joined = "-".join(["a", "b", "c"])  # "a-b-c"

    # Formatting
    formatted = "Hello {}".format("World")  # "Hello World"
    f_string = f"Hello {'World'}"  # "Hello World"

    return (upper, lower, title, capitalize, contains, index, replaced,
            words, stripped, is_digit, is_alpha, is_alpha_num, joined,
            formatted, f_string)


# ============================================================================
# EXERCISES
# ============================================================================

def exercise_1():
    """
    Create variables for different numeric types.
    Return: integer, float, complex
    """
    integer = 42
    floating = 3.14
    complex_num = 3 + 4j
    return integer, floating, complex_num


def exercise_2():
    """
    Create and manipulate strings.
    """
    message = "Python Programming"
    upper = message.upper()
    reversed_str = message[::-1]
    first_word = message.split()[0]
    return message, upper, reversed_str, first_word


def exercise_3():
    """
    Type conversions.
    """
    str_num = "123"
    to_int = int(str_num)
    to_float = float(str_num)
    back_to_str = str(to_float)
    return to_int, to_float, back_to_str


def exercise_4():
    """
    String indexing and slicing.
    """
    word = "education"
    first_letter = word[0]  # 'e'
    last_letter = word[-1]  # 'n'
    middle = word[3:7]  # 'cati'
    every_other = word[::2]  # 'euain'
    return first_letter, last_letter, middle, every_other


def exercise_5():
    """
    Boolean operations and truthiness.
    """
    a = True and False  # False
    b = True or False  # True
    c = not True  # False
    d = bool(42)  # True
    e = bool(0)  # False
    return a, b, c, d, e


if __name__ == "__main__":
    print("Lesson 3: Data Types")
    print("=" * 60)

    print("\n1. Integers:")
    p, n, z, b, bi, o, h = explain_integers()
    print(f"   Positive={p}, Negative={n}, Binary={bi}")

    print("\n2. Floats:")
    pi, nf, zf, sci, large, small, result = explain_floats()
    print(f"   Pi={pi}, Scientific={sci}, Large={large}")

    print("\n3. Complex numbers:")
    c1, c2, c3, r, i, add = explain_complex_numbers()
    print(f"   c1={c1}, Real part={r}, Imaginary part={i}")

    print("\n4. Strings:")
    sq, dq, tq, e, nl, t, q, r, conc, rep = explain_strings()
    print(f"   Single quote: {sq}, Concatenated: {conc}")

    print("\n5. String indexing:")
    f, s, l, sl2, s1, s2, s3, s4, s5, ln = explain_string_indexing()
    print(f"   First={f}, Last={l}, Slice={s1}")

    print("\n6. Booleans:")
    t, f, c1, c2, c3, ar, or_, nr, t1, f1, t2, f2 = explain_booleans()
    print(f"   True={t}, False={f}, Comparison={c1}")

    print("\n7. Type conversion:")
    si, sf, itf, fti, its, fts, bts, tb1, tb2, tb3, tb4 = explain_type_conversion()
    print(f"   str to int={si}, int to str={its}")

    print("\n8. Numeric operations:")
    (add, sub, mul, div, fdiv, mod, pw, res, eq, neq, lt, gt, le, ge, ch) = explain_numeric_operations()
    print(f"   10 + 3 = {add}, 10 // 3 = {fdiv}, 2**3 = {pw}")

    print("\n9. String methods:")
    (u, l, ti, c, cont, idx, repl, w, st, id, ia, ian, j, fmt, fs) = explain_string_methods()
    print(f"   Upper={u}, Lower={l}, Replaced={repl}")

    print("\n✓ All lessons completed")
