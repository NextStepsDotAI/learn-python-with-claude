"""
Lesson 2: Variables

Topics covered:
- What are variables
- Variable naming rules and conventions
- Assignment and reassignment
- Variable scope (local and global)
- Multiple assignment
- Variable introspection (type, id)

A variable is a named container that holds a value in memory.
Python manages memory automatically, so you can create and use variables
without worrying about allocation and deallocation.
"""


# ============================================================================
# SECTION 1: WHAT ARE VARIABLES
# ============================================================================

def explain_variables():
    """
    Variables are named references to objects in Python.

    When you create a variable, you're binding a name to an object.
    Multiple variables can point to the same object.
    """
    # Create variables
    name = "Alice"  # String object
    age = 30  # Integer object
    height = 5.7  # Float object

    # Variables are references to objects
    x = 42
    y = x  # y now refers to the same object as x

    return name, age, height, x, y


# ============================================================================
# SECTION 2: VARIABLE NAMING RULES
# ============================================================================

def explain_naming_rules():
    """
    Python variable naming rules:

    Rules (mandatory):
    1. Must start with letter (a-z, A-Z) or underscore (_)
    2. Can contain letters, digits (0-9), and underscores
    3. Case-sensitive (age, Age, AGE are different variables)
    4. Cannot be a reserved keyword

    Conventions (recommended):
    1. Use lowercase with underscores (snake_case): my_variable
    2. Use meaningful names: user_age not ua or a
    3. Class names use PascalCase: MyClass
    4. Constants use UPPERCASE: MAX_SIZE
    5. Private/internal use leading underscore: _private_var
    """

    # Valid variable names
    name = "Bob"
    user_age = 25
    _internal = "private"
    User_ID = 123  # Valid but not conventional
    age2 = 30

    # Class name convention
    class UserProfile:
        pass

    # Constant convention
    MAX_RETRIES = 3
    DEFAULT_TIMEOUT = 30

    return name, user_age, _internal, MAX_RETRIES


# ============================================================================
# SECTION 3: ASSIGNMENT AND REASSIGNMENT
# ============================================================================

def explain_assignment():
    """
    Variables can be assigned and reassigned.
    Assignment uses the = operator (right-to-left).

    The right side is evaluated first, then bound to the left-side name.
    """
    # Single assignment
    x = 10

    # Reassignment (x now refers to a different object)
    x = 20

    # Assignment with expression
    y = 5 + 3  # Right side evaluated first (8), then assigned to y

    # Chained assignment (all refer to same object)
    a = b = c = 0

    # Multiple assignment (unpacking)
    x, y, z = 1, 2, 3  # x=1, y=2, z=3

    # Swap using multiple assignment (no temp variable needed)
    x, y = y, x  # x and y are swapped

    return x, y, z


# ============================================================================
# SECTION 4: VARIABLE TYPES AND INTROSPECTION
# ============================================================================

def explain_type_and_id():
    """
    Every variable has:
    - Type: the class of the object (int, str, list, etc.)
    - ID: unique identifier in memory
    - Value: the actual data

    Use type() and id() to introspect variables.
    """

    # Different types
    integer_var = 42
    string_var = "hello"
    float_var = 3.14
    list_var = [1, 2, 3]

    # Type introspection
    type_int = type(integer_var)  # <class 'int'>
    type_str = type(string_var)  # <class 'str'>
    type_list = type(list_var)  # <class 'list'>

    # ID introspection (memory address)
    id_int = id(integer_var)
    id_str = id(string_var)

    # Same value, different types
    x = 42
    y = 42.0
    z = "42"

    # x and y have same value but different types
    # z is a string, different from x and y

    return type_int, type_str, type_list, id_int, id_str


# ============================================================================
# SECTION 5: SCOPE
# ============================================================================

# Global variable
global_var = "I'm global"


def explain_local_scope():
    """
    Variable scope determines where a variable is accessible.

    - Local scope: variables defined in a function
    - Global scope: variables defined at module level
    - Variables in local scope shadow global variables with same name
    """

    # Local variable (only exists inside this function)
    local_var = "I'm local"

    # This is a local variable, not the global one
    global_var = "I'm local (shadows global)"

    return local_var, global_var


def access_global():
    """
    To modify a global variable inside a function, use 'global' keyword.
    """
    global global_var
    global_var = "Modified globally"


# ============================================================================
# SECTION 6: IMMUTABILITY AND MUTABILITY
# ============================================================================

def explain_immutability():
    """
    Python has mutable and immutable types:

    Immutable (cannot be changed):
    - int, float, str, bool, tuple
    - When you "change" them, you create a new object

    Mutable (can be changed):
    - list, dict, set
    - When you modify them, the object itself changes
    """

    # Immutable: creating new object
    x = "hello"
    x = x + " world"  # Creates new string, x refers to it

    # Immutable: reassignment looks like change, but isn't
    y = 42
    y = y + 1  # Creates new int, y refers to it

    # Mutable: modifying the object itself
    lst = [1, 2, 3]
    lst.append(4)  # Modifies the list object (no reassignment needed)

    # Mutable: reassignment is different from modification
    lst2 = [1, 2, 3]
    lst2_ref = lst2  # Two names point to same object
    lst2.append(4)  # Modifies the object
    # Now both lst2 and lst2_ref show [1, 2, 3, 4]

    return x, y, lst, lst2, lst2_ref


# ============================================================================
# SECTION 7: WORKING WITH VARIABLES
# ============================================================================

def demonstrate_variable_operations():
    """
    Common operations with variables.
    """

    # Create and modify variables
    count = 0
    count = count + 1  # Increment
    count += 1  # Shorthand increment

    # Variable in expressions
    x = 10
    y = 20
    result = x + y * 2  # 50 (order of operations)

    # Variable names can be built dynamically (advanced)
    variables = {}
    variables['name'] = "Alice"
    variables['age'] = 30

    return count, result, variables


# ============================================================================
# EXERCISES
# ============================================================================

def exercise_1():
    """
    Create variables for personal information and return them.
    Variables: first_name, last_name, age, city
    """
    first_name = "John"
    last_name = "Doe"
    age = 25
    city = "New York"
    return first_name, last_name, age, city


def exercise_2():
    """
    Swap two variables without using a temporary variable.
    """
    a = 5
    b = 10
    a, b = b, a  # Python swap
    return a, b


def exercise_3():
    """
    Create variables with different types and check their types.
    """
    num = 42
    text = "Python"
    decimal = 3.14
    flag = True
    items = [1, 2, 3]

    return {
        'number': type(num).__name__,
        'text': type(text).__name__,
        'decimal': type(decimal).__name__,
        'flag': type(flag).__name__,
        'items': type(items).__name__,
    }


def exercise_4():
    """
    Demonstrate immutability: strings cannot be changed in place.
    """
    word = "hello"
    # word[0] = 'H'  # This would raise TypeError

    # Instead, create a new string
    word = word.capitalize()  # "Hello"

    return word


def exercise_5():
    """
    Multiple assignment with three variables.
    """
    x, y, z = 10, 20, 30

    # Rotate: x -> y, y -> z, z -> x
    x, y, z = z, x, y

    return x, y, z


if __name__ == "__main__":
    print("Lesson 2: Variables")
    print("=" * 60)

    print("\n1. What are variables:")
    name, age, height, x, y = explain_variables()
    print(f"   name={name}, age={age}, height={height}")

    print("\n2. Naming rules:")
    name, age, internal, max_r = explain_naming_rules()
    print(f"   snake_case names used throughout")

    print("\n3. Assignment:")
    x, y, z = explain_assignment()
    print(f"   After swap: x={x}, y={y}, z={z}")

    print("\n4. Type and ID:")
    t1, t2, t3, id1, id2 = explain_type_and_id()
    print(f"   Types: int={t1}, str={t2}, list={t3}")

    print("\n5. Scope:")
    local, shadowed = explain_local_scope()
    print(f"   Local: {local}, Shadowed: {shadowed}")

    print("\n6. Immutability:")
    x, y, lst, lst2, lst2_ref = explain_immutability()
    print(f"   Immutable strings/ints vs mutable lists")

    print("\n✓ All lessons completed")
