"""
Tests for Lesson 2: Variables

Covers:
- Variable creation and assignment
- Variable naming rules
- Type introspection
- Scope (local and global)
- Immutability and mutability
- Variable operations
"""

import pytest
from src.learn_python_with_claude.lesson_02_variables import (
    explain_variables,
    explain_naming_rules,
    explain_assignment,
    explain_type_and_id,
    explain_local_scope,
    access_global,
    explain_immutability,
    demonstrate_variable_operations,
    exercise_1,
    exercise_2,
    exercise_3,
    exercise_4,
    exercise_5,
)


class TestVariableCreation:
    """Test basic variable creation and assignment."""

    def test_variable_assignment(self):
        """Variables can hold values."""
        x = 42
        assert x == 42

    def test_variable_reassignment(self):
        """Variables can be reassigned."""
        x = 10
        x = 20
        assert x == 20

    def test_multiple_variables(self):
        """Multiple variables can be created."""
        x = 1
        y = 2
        z = 3
        assert x + y + z == 6

    def test_chained_assignment(self):
        """Multiple variables can share the same initial value."""
        a = b = c = 5
        assert a == 5 and b == 5 and c == 5

    def test_multiple_assignment_unpacking(self):
        """Values can be unpacked to multiple variables."""
        x, y, z = 1, 2, 3
        assert x == 1 and y == 2 and z == 3


class TestVariableNaming:
    """Test variable naming rules and conventions."""

    def test_lowercase_snake_case(self):
        """Snake case is the Python convention."""
        user_name = "Alice"
        user_age = 30
        assert user_name == "Alice"
        assert user_age == 30

    def test_variable_naming_with_underscore(self):
        """Underscores are valid in variable names."""
        _private_var = "internal"
        public_var = "external"
        assert _private_var == "internal"
        assert public_var == "external"

    def test_variable_names_are_case_sensitive(self):
        """Variable names are case-sensitive."""
        age = 25
        Age = 30
        AGE = 35
        assert age == 25 and Age == 30 and AGE == 35

    def test_constant_naming_convention(self):
        """Constants use UPPERCASE."""
        MAX_SIZE = 100
        DEFAULT_TIMEOUT = 30
        assert MAX_SIZE == 100
        assert DEFAULT_TIMEOUT == 30

    def test_variable_names_starting_with_letter(self):
        """Variable names must start with letter or underscore."""
        valid_name = "value"
        _also_valid = "value"
        assert valid_name == "value"
        assert _also_valid == "value"


class TestVariableTypes:
    """Test variable type introspection."""

    def test_integer_type(self):
        """Integer variables have type int."""
        x = 42
        assert type(x) == int

    def test_string_type(self):
        """String variables have type str."""
        s = "hello"
        assert type(s) == str

    def test_float_type(self):
        """Float variables have type float."""
        f = 3.14
        assert type(f) == float

    def test_boolean_type(self):
        """Boolean variables have type bool."""
        flag = True
        assert type(flag) == bool
        assert isinstance(flag, bool)

    def test_list_type(self):
        """List variables have type list."""
        lst = [1, 2, 3]
        assert type(lst) == list

    def test_type_names(self):
        """Type names can be accessed as strings."""
        x = 42
        assert type(x).__name__ == 'int'

        s = "hello"
        assert type(s).__name__ == 'str'

    def test_same_value_different_types(self):
        """Same value can have different types."""
        x = 42  # int
        y = 42.0  # float
        z = "42"  # str

        assert type(x) != type(y)
        assert type(y) != type(z)
        assert x == float(y)  # Values can be equal
        assert type(x) != type(z)  # But types are different


class TestVariableScope:
    """Test variable scope (local and global)."""

    def test_local_variable(self):
        """Variables in functions are local."""
        def create_local():
            local_var = "local"
            return local_var

        result = create_local()
        assert result == "local"

    def test_global_variable_access(self):
        """Global variables can be accessed from functions."""
        from src.learn_python_with_claude.lesson_02_variables import global_var
        assert global_var == "I'm global"

    def test_local_shadows_global(self):
        """Local variables shadow global variables."""
        local, shadowed = explain_local_scope()
        assert local == "I'm local"
        assert shadowed == "I'm local (shadows global)"

    def test_modify_global_with_global_keyword(self):
        """Global keyword allows modification of global variables."""
        # Save original
        from src.learn_python_with_claude import lesson_02_variables as mod
        original = mod.global_var

        try:
            access_global()
            assert mod.global_var == "Modified globally"
        finally:
            # Restore
            mod.global_var = original


class TestMutabilityAndImmutability:
    """Test mutable vs immutable types."""

    def test_immutable_string(self):
        """Strings are immutable."""
        s = "hello"
        # s[0] = 'H' would raise TypeError
        s_new = s.upper()
        assert s_new == "HELLO"
        assert s == "hello"  # Original unchanged

    def test_immutable_tuple(self):
        """Tuples are immutable."""
        t = (1, 2, 3)
        # t[0] = 10 would raise TypeError
        assert t == (1, 2, 3)

    def test_mutable_list(self):
        """Lists are mutable."""
        lst = [1, 2, 3]
        lst[0] = 10
        assert lst == [10, 2, 3]

    def test_mutable_list_append(self):
        """List modifications change the object."""
        lst = [1, 2, 3]
        lst.append(4)
        assert lst == [1, 2, 3, 4]

    def test_mutable_list_shared_reference(self):
        """Multiple names can refer to same mutable object."""
        lst1 = [1, 2, 3]
        lst2 = lst1  # Both refer to same object
        lst1.append(4)
        assert lst2 == [1, 2, 3, 4]  # lst2 also changed

    def test_immutable_shared_reference(self):
        """Reassigning immutable creates new reference."""
        x = 42
        y = x
        x = 43  # Creates new object, x refers to it
        assert y == 42  # y still refers to original


class TestVariableOperations:
    """Test working with variables."""

    def test_variable_in_expression(self):
        """Variables can be used in expressions."""
        x = 10
        y = 20
        result = x + y
        assert result == 30

    def test_variable_increment(self):
        """Variables can be incremented."""
        x = 0
        x = x + 1
        assert x == 1
        x += 1
        assert x == 2

    def test_variable_in_string(self):
        """Variables can be used in strings."""
        name = "Alice"
        age = 30
        message = f"My name is {name} and I'm {age}"
        assert message == "My name is Alice and I'm 30"

    def test_swap_variables(self):
        """Variables can be swapped elegantly."""
        x = 5
        y = 10
        x, y = y, x
        assert x == 10 and y == 5


class TestExercises:
    """Test lesson exercises."""

    def test_exercise_1_personal_info(self):
        """Exercise 1: Personal information."""
        first_name, last_name, age, city = exercise_1()
        assert first_name == "John"
        assert last_name == "Doe"
        assert age == 25
        assert city == "New York"

    def test_exercise_2_swap_variables(self):
        """Exercise 2: Swap without temporary."""
        a, b = exercise_2()
        assert a == 10
        assert b == 5

    def test_exercise_3_types(self):
        """Exercise 3: Different types."""
        result = exercise_3()
        assert result['number'] == 'int'
        assert result['text'] == 'str'
        assert result['decimal'] == 'float'
        assert result['flag'] == 'bool'
        assert result['items'] == 'list'

    def test_exercise_4_string_immutability(self):
        """Exercise 4: String immutability."""
        word = exercise_4()
        assert word == "Hello"

    def test_exercise_5_rotation(self):
        """Exercise 5: Variable rotation."""
        x, y, z = exercise_5()
        assert x == 30  # z value
        assert y == 10  # x value
        assert z == 20  # y value


class TestIntegration:
    """Integration tests combining multiple concepts."""

    def test_complete_flow_explain_variables(self):
        """Complete flow of variable creation."""
        name, age, height, x, y = explain_variables()
        assert isinstance(name, str)
        assert isinstance(age, int)
        assert isinstance(height, float)
        assert x == y  # Both refer to same value

    def test_complete_flow_naming_rules(self):
        """Complete flow with naming rules."""
        name, age, internal, max_r = explain_naming_rules()
        assert isinstance(name, str)
        assert isinstance(age, int)
        assert isinstance(max_r, int)

    def test_complete_flow_assignment(self):
        """Complete assignment flow."""
        x, y, z = explain_assignment()
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(z, int)

    def test_complete_flow_types(self):
        """Complete type introspection flow."""
        t1, t2, t3, id1, id2 = explain_type_and_id()
        assert t1 == int
        assert t2 == str
        assert t3 == list
        assert isinstance(id1, int)
        assert isinstance(id2, int)

    def test_complete_flow_immutability(self):
        """Complete immutability flow."""
        x, y, lst, lst2, lst2_ref = explain_immutability()
        assert isinstance(x, str)
        assert isinstance(y, int)
        assert isinstance(lst, list)
        assert lst2 == lst2_ref  # Same object


class TestLessonStructure:
    """Test that lesson follows expected structure."""

    def test_lesson_module_exists(self):
        """Lesson module can be imported."""
        from src.learn_python_with_claude import lesson_02_variables
        assert lesson_02_variables is not None

    def test_lesson_has_docstring(self):
        """Lesson module has a docstring."""
        from src.learn_python_with_claude import lesson_02_variables
        assert lesson_02_variables.__doc__ is not None
        assert "Lesson 2" in lesson_02_variables.__doc__

    def test_all_exercise_functions_exist(self):
        """All exercise functions are defined."""
        assert callable(exercise_1)
        assert callable(exercise_2)
        assert callable(exercise_3)
        assert callable(exercise_4)
        assert callable(exercise_5)

    def test_all_explain_functions_exist(self):
        """All explain functions are defined."""
        assert callable(explain_variables)
        assert callable(explain_naming_rules)
        assert callable(explain_assignment)
        assert callable(explain_type_and_id)
        assert callable(explain_local_scope)
