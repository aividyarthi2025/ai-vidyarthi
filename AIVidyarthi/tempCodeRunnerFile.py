"""
=============================================================================
PYTHON FUNDAMENTALS - COMPREHENSIVE REFERENCE GUIDE
=============================================================================

Python is a high-level, interpreted, general-purpose programming language.
It emphasizes readability, simplicity, and expressiveness.

Key characteristics:
    - Dynamically typed: variable types are determined at runtime
    - Interpreted: code is executed line by line
    - Object-oriented: everything in Python is an object
    - Garbage-collected: memory is managed automatically
    - Multi-paradigm: supports OOP, functional, and procedural styles

Author: Python Fundamentals Guide
Python version: 3.x
=============================================================================
"""

# =============================================================================
# SECTION 1: VARIABLES AND DATA TYPES
# =============================================================================
"""
Variables are containers for storing data values.
Python uses dynamic typing — no need to declare types explicitly.

Naming rules:
    - Must start with a letter or underscore (_)
    - Cannot start with a digit
    - Can contain letters, digits, and underscores
    - Case-sensitive (age, Age, AGE are different variables)
    - Cannot use Python reserved keywords (if, for, class, etc.)
"""

# --- Integers ---
# Whole numbers, positive or negative, without decimals.
age = 25
negative_number = -10
big_number = 1_000_000      # underscores improve readability
hex_number = 0xFF           # hexadecimal literal (255)
octal_number = 0o17         # octal literal (15)
binary_number = 0b1010      # binary literal (10)

# --- Floats ---
# Numbers with a decimal point. Stored as 64-bit IEEE 754 double precision.
temperature = 98.6
scientific = 1.5e3          # 1500.0 (scientific notation)
small = 2.5e-4              # 0.00025

# --- Strings ---
# Immutable sequences of Unicode characters.
name = "Alice"
greeting = 'Hello, World!'
multiline = """This string
spans multiple
lines."""
raw_string = r"C:\Users\name"   # raw string: backslashes are literal
byte_string = b"bytes"          # bytes literal, not a str

# --- Booleans ---
# Subclass of int. True == 1, False == 0.
is_active = True
is_deleted = False

# --- NoneType ---
# Represents the absence of a value. Similar to null in other languages.
result = None

# --- Type inspection ---
print(type(age))            # <class 'int'>
print(type(temperature))    # <class 'float'>
print(type(name))           # <class 'str'>
print(type(is_active))      # <class 'bool'>
print(type(result))         # <class 'NoneType'>