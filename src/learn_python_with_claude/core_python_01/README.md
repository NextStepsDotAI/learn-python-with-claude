# Core Python: Language Constructs & Syntax

A roadmap of basic Python topics, ordered from simple to complex. It covers the
language itself only (syntax and constructs), not the standard library or
third-party packages.

## Level 1: First Steps

1. **Running Python**: the interpreter, REPL, running a `.py` file
2. **Comments**: `#` single-line comments, docstrings (`"""..."""`)
3. **Indentation & statements**: whitespace as block structure, line continuation (`\`, brackets)
4. **`print()` and `input()`**: basic output and input
5. **Variables & assignment**: naming rules, `=`, multiple assignment (`a, b = 1, 2`)
6. **Keywords & identifiers**: reserved words, naming conventions (PEP 8)

## Level 2: Data Types & Operators

7. **Numbers**: `int`, `float`, `complex`
8. **Booleans**: `True`, `False`, truthiness
9. **`None`**: the absence of a value
10. **Strings**: literals, quotes, escape sequences, raw strings, multi-line strings
11. **Arithmetic operators**: `+ - * / // % **`
12. **Comparison operators**: `== != < > <= >=`, chained comparisons
13. **Logical operators**: `and`, `or`, `not`, short-circuiting
14. **Assignment operators**: `+= -= *=` and friends
15. **Identity & membership**: `is`, `is not`, `in`, `not in`
16. **Bitwise operators**: `& | ^ ~ << >>`
17. **Operator precedence**
18. **Type conversion**: `int()`, `float()`, `str()`, `bool()`, `type()`, `isinstance()`

## Level 3: Strings in Depth

19. **Indexing & slicing**: `s[0]`, `s[-1]`, `s[1:4:2]`
20. **String methods**: `.upper()`, `.split()`, `.join()`, `.strip()`, `.replace()`, `.find()`
21. **String formatting**: f-strings, `.format()`, `%` formatting
22. **Immutability** of strings

## Level 4: Control Flow

23. **`if` / `elif` / `else`**
24. **Conditional expression**: `x if cond else y`
25. **`while` loops**
26. **`for` loops** and `range()`
27. **`break`, `continue`, `pass`**
28. **`else` on loops**
29. **`match` / `case`**: structural pattern matching (Python 3.10+)

## Level 5: Collections

30. **Lists**: creation, indexing, slicing, mutation, methods (`append`, `extend`, `pop`, `sort`)
31. **Tuples**: immutability, packing & unpacking
32. **Sets**: uniqueness, set operations (`| & - ^`)
33. **Dictionaries**: keys & values, access, `.get()`, `.items()`, iteration
34. **Nested collections**
35. **Mutable vs immutable types** and hashability
36. **Iterating helpers**: `enumerate()`, `zip()`, `len()`, `sorted()`, `reversed()`
37. **Unpacking**: extended unpacking with `*` (`first, *rest = items`)

## Level 6: Functions

38. **Defining & calling functions**: `def`, `return`
39. **Parameters**: positional, keyword, default values
40. **`*args` and `**kwargs`**
41. **Keyword-only & positional-only parameters**: `*`, `/`
42. **Scope**: local, enclosing, global, built-in (LEGB), `global`, `nonlocal`
43. **Docstrings & type hints**: `def f(x: int) -> str:`
44. **Lambda expressions**
45. **Functions as first-class objects**: passing and returning functions
46. **Recursion**

## Level 7: Comprehensions & Iteration

47. **List comprehensions**
48. **Dict & set comprehensions**
49. **Generator expressions**
50. **Iterables vs iterators**: `iter()`, `next()`
51. **Generators**: `yield`, `yield from`

## Level 8: Errors & Exceptions

52. **Common exceptions**: `SyntaxError`, `TypeError`, `ValueError`, `KeyError`, `IndexError`
53. **`try` / `except` / `else` / `finally`**
54. **`raise`** and re-raising
55. **Custom exceptions**
56. **`assert`**

## Level 9: Modules & Packages

57. **`import`**, `from ... import ...`, `as` aliases
58. **Writing your own modules**
59. **Packages**: `__init__.py`, relative imports
60. **`if __name__ == "__main__":`**

## Level 10: Object-Oriented Programming

61. **Classes & objects**: `class`, `__init__`, `self`
62. **Instance vs class attributes**
63. **Methods**: instance, `@classmethod`, `@staticmethod`
64. **Inheritance** and `super()`
65. **Multiple inheritance & MRO**
66. **Encapsulation conventions**: `_protected`, `__private` (name mangling)
67. **Properties**: `@property`, setters
68. **Dunder (magic) methods**: `__str__`, `__repr__`, `__eq__`, `__len__`, `__add__`
69. **Polymorphism & duck typing**

## Level 11: Advanced Constructs

70. **Closures**
71. **Decorators**: function decorators, decorators with arguments
72. **Context managers**: `with` statement, `__enter__` / `__exit__`
73. **The walrus operator**: `:=`
74. **Dataclasses**: `@dataclass`
75. **Abstract base classes**: `abc.ABC`, `@abstractmethod`
76. **Iterator protocol**: implementing `__iter__` / `__next__`
77. **Descriptors**: `__get__` / `__set__`
78. **Metaclasses**: `type` as a class factory
79. **Async syntax**: `async def`, `await`, `async for`, `async with`
