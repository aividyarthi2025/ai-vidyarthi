"""
=============================================================================
AI Vidyarthi USA - www.aividyarthi.us - @AIVidyarthiOfficial
=============================================================================
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

# --- Type conversion (casting) ---
int_from_str = int("42")        # 42
float_from_int = float(10)      # 10.0
str_from_int = str(100)         # "100"
bool_from_int = bool(0)         # False (0 is falsy)
bool_from_str = bool("hello")   # True (non-empty string is truthy)
list_from_str = list("abc")     # ['a', 'b', 'c']

# --- Falsy values in Python ---
# The following evaluate to False in boolean contexts:
#   False, None, 0, 0.0, 0j, "", [], (), {}, set()
# Everything else is truthy.


# =============================================================================
# SECTION 2: OPERATORS
# =============================================================================
"""
Python supports a rich set of operators for arithmetic, comparison,
logical operations, identity, membership, and bitwise operations.
"""

# --- Arithmetic operators ---
a, b = 10, 3
print(a + b)    # 13   — addition
print(a - b)    # 7    — subtraction
print(a * b)    # 30   — multiplication
print(a / b)    # 3.333 — true division (always returns float)
print(a // b)   # 3    — floor division (integer result)
print(a % b)    # 1    — modulo (remainder)
print(a ** b)   # 1000 — exponentiation

# --- Comparison operators (return bool) ---
print(a == b)   # False — equal
print(a != b)   # True  — not equal
print(a > b)    # True  — greater than
print(a < b)    # False — less than
print(a >= b)   # True  — greater than or equal
print(a <= b)   # False — less than or equal

# Python supports chained comparisons:
x = 5
print(1 < x < 10)   # True — equivalent to (1 < x) and (x < 10)

# --- Logical operators ---
print(True and False)   # False — both must be True
print(True or False)    # True  — at least one must be True
print(not True)         # False — inverts the boolean

# Short-circuit evaluation:
#   `and` stops at first False value and returns it
#   `or` stops at first True value and returns it
print(0 and 5)      # 0   (short-circuits, returns 0)
print(0 or 5)       # 5   (returns first truthy value)
print(None or "default")  # "default"

# --- Assignment operators ---
c = 10
c += 5      # c = c + 5   → 15
c -= 3      # c = c - 3   → 12
c *= 2      # c = c * 2   → 24
c //= 5     # c = c // 5  → 4
c **= 3     # c = c ** 3  → 64
c %= 10     # c = c % 10  → 4

# --- Identity operators ---
# `is` checks if two variables point to the same object in memory.
# `==` checks if values are equal.
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)   # True  — same values
print(x is y)   # False — different objects in memory
print(x is z)   # True  — same object

# --- Membership operators ---
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)    # True
print("grape" not in fruits) # True

# --- Bitwise operators ---
print(5 & 3)    # 1  — AND
print(5 | 3)    # 7  — OR
print(5 ^ 3)    # 6  — XOR
print(~5)       # -6 — NOT
print(5 << 1)   # 10 — left shift
print(5 >> 1)   # 2  — right shift


# =============================================================================
# SECTION 3: STRINGS IN DEPTH
# =============================================================================
"""
Strings are immutable sequences of Unicode characters.
They support indexing, slicing, and many built-in methods.
"""

s = "Hello, Python!"

# --- Indexing ---
# Positive index starts at 0 from the left.
# Negative index starts at -1 from the right.
print(s[0])     # 'H'
print(s[-1])    # '!'
print(s[7])     # 'P'

# --- Slicing: s[start:stop:step] ---
# start is inclusive, stop is exclusive.
print(s[0:5])       # 'Hello'
print(s[7:])        # 'Python!'
print(s[:5])        # 'Hello'
print(s[::2])       # 'Hlo yhn'  — every 2nd character
print(s[::-1])      # '!nohtyP ,olleH' — reversed

# --- String methods ---
print(s.upper())            # 'HELLO, PYTHON!'
print(s.lower())            # 'hello, python!'
print(s.title())            # 'Hello, Python!'
print(s.strip())            # removes leading/trailing whitespace
print(s.lstrip())           # strips left whitespace only
print(s.rstrip())           # strips right whitespace only
print(s.replace("Hello", "Hi"))  # 'Hi, Python!'
print(s.split(", "))        # ['Hello', 'Python!']
print(s.startswith("Hello")) # True
print(s.endswith("!"))       # True
print(s.find("Python"))      # 7 (index of first occurrence, -1 if not found)
print(s.count("l"))          # 3
print(s.isdigit())           # False
print(s.isalpha())           # False (contains spaces and punctuation)
print("  hello  ".strip())   # 'hello'
print(",".join(["a", "b", "c"]))  # 'a,b,c'

# --- String formatting ---
name = "Alice"
score = 95.678

# f-strings (Python 3.6+) — preferred, most readable
print(f"Name: {name}, Score: {score:.2f}")  # Score rounded to 2 decimals

# format() method
print("Name: {}, Score: {:.2f}".format(name, score))

# % formatting (older style)
print("Name: %s, Score: %.2f" % (name, score))

# String alignment and padding
print(f"{'left':<10}|")     # left-aligned in 10 chars
print(f"{'right':>10}|")    # right-aligned in 10 chars
print(f"{'center':^10}|")   # centered in 10 chars
print(f"{42:05d}")           # zero-padded integer: 00042


# =============================================================================
# SECTION 4: COLLECTIONS — LIST, TUPLE, SET, DICT
# =============================================================================

# --- LIST ---
"""
Lists are ordered, mutable (changeable) sequences.
They allow duplicate elements and can hold mixed types.
"""

fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]   # mixed types allowed

# Accessing elements
print(fruits[0])        # 'apple'
print(fruits[-1])       # 'cherry'

# Modifying
fruits.append("date")           # add to end
fruits.insert(1, "avocado")     # insert at index
fruits.extend(["elderberry"])   # add multiple items
removed = fruits.pop()          # removes and returns last item
fruits.pop(0)                   # removes item at index 0
fruits.remove("banana")         # removes first occurrence of value
fruits.sort()                   # sort in place (ascending)
fruits.sort(reverse=True)       # sort descending
fruits.reverse()                # reverse in place
fruits_copy = fruits.copy()     # shallow copy

# List information
print(len(fruits))          # number of elements
print(fruits.index("cherry"))   # index of value
print(fruits.count("cherry"))   # occurrences of value

# List slicing (same as strings)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])     # [2, 3, 4, 5, 6]
print(numbers[::2])     # [0, 2, 4, 6, 8]
print(numbers[::-1])    # reversed list

# List comprehension (covered in detail later)
squares = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]

# Nested lists (2D list / matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])     # 6 — row 1, column 2

# --- TUPLE ---
"""
Tuples are ordered, IMMUTABLE sequences.
Use tuples for data that should not change (coordinates, RGB values, etc.).
Slightly faster than lists for iteration.
"""

coords = (10, 20)
rgb = (255, 128, 0)
single = (42,)          # single-element tuple MUST have trailing comma
empty = ()

# Unpacking tuples
x, y = coords           # x=10, y=20
r, g, b = rgb

# Swapping variables using tuple packing/unpacking
a, b = 5, 10
a, b = b, a     # a=10, b=5

# Named tuple (structured, self-documenting)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)     # 3 4

# --- SET ---
"""
Sets are unordered collections of UNIQUE elements.
Great for membership testing, deduplication, and set operations.
Sets are mutable; frozenset is the immutable version.
"""

colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("green")    # remove if present (no error if missing)
colors.remove("red")       # remove (raises KeyError if missing)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # {1,2,3,4,5,6} — union
print(a & b)    # {3,4}         — intersection
print(a - b)    # {1,2}         — difference (in a, not in b)
print(a ^ b)    # {1,2,5,6}     — symmetric difference

# Membership (O(1) average, much faster than list)
print(3 in a)       # True

# Deduplicate a list
dupes = [1, 2, 2, 3, 3, 3]
unique = list(set(dupes))   # [1, 2, 3] (order not guaranteed)

# --- DICTIONARY ---
"""
Dictionaries are ordered (Python 3.7+) collections of key-value pairs.
Keys must be unique and hashable (str, int, tuple, etc.).
Values can be any type.
"""

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])               # 'Alice'
print(person.get("age"))            # 30
print(person.get("email", "N/A"))   # 'N/A' — default if key missing

# Modifying
person["age"] = 31              # update existing key
person["email"] = "alice@example.com"  # add new key
del person["city"]              # delete a key
popped = person.pop("email")    # remove and return value

# Iterating
for key in person:                      # iterate over keys
    print(key, person[key])

for key, value in person.items():       # iterate over key-value pairs
    print(f"{key}: {value}")

for key in person.keys():              # keys view
    pass
for value in person.values():          # values view
    pass

# Dictionary comprehension
squared = {x: x**2 for x in range(1, 6)}  # {1:1, 2:4, 3:9, 4:16, 5:25}

# Merging dictionaries (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2        # {"a":1, "b":3, "c":4} — d2 values win on conflict

# Nested dictionary
employee = {
    "id": 101,
    "name": "Bob",
    "address": {
        "street": "123 Main St",
        "city": "Chicago"
    }
}
print(employee["address"]["city"])  # 'Chicago'

# --- COLLECTIONS MODULE EXTRAS ---
from collections import Counter, defaultdict, OrderedDict, deque

# Counter: counts occurrences
word_count = Counter("mississippi")
print(word_count)   # Counter({'i':4,'s':4,'p':2,'m':1})
print(word_count.most_common(2))  # [('i', 4), ('s', 4)]

# defaultdict: returns a default value for missing keys
dd = defaultdict(list)
dd["fruits"].append("apple")    # no KeyError even though key is new
dd["fruits"].append("banana")

# deque: double-ended queue, efficient insert/remove from both ends
dq = deque([1, 2, 3])
dq.appendleft(0)    # [0, 1, 2, 3]
dq.append(4)        # [0, 1, 2, 3, 4]
dq.popleft()        # removes 0
dq.pop()            # removes 4
dq.rotate(1)        # rotate right by 1


# =============================================================================
# SECTION 5: CONTROL FLOW
# =============================================================================

# --- if / elif / else ---
"""
Conditional execution. Python uses indentation (4 spaces) to define blocks.
No braces {} or semicolons required.
"""

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")

# Ternary / conditional expression (one-liner if/else)
status = "pass" if score >= 60 else "fail"

# match statement (Python 3.10+ — structural pattern matching)
command = "quit"
match command:
    case "quit":
        print("Quitting...")
    case "help":
        print("Showing help...")
    case _:         # wildcard — matches anything
        print("Unknown command")

# --- for loop ---
"""
Iterates over any iterable (list, tuple, string, range, dict, file, etc.).
"""

# Basic for loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 10, 2):  # start=1, stop=10, step=2 → 1,3,5,7,9
    print(i)

# Iterating over collections
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for char in "Python":
    print(char)

# enumerate — get index and value together
for index, value in enumerate(["a", "b", "c"], start=1):
    print(f"{index}: {value}")   # 1: a, 2: b, 3: c

# zip — iterate over multiple iterables in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip produces tuples and stops at the shortest iterable
# zip_longest (from itertools) pads with a fill value

# --- while loop ---
"""
Repeats as long as condition is True. Be careful of infinite loops!
"""

count = 0
while count < 5:
    print(count)
    count += 1      # always update the condition variable!

# while with else (else runs when condition becomes False, not on break)
n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("Done!")  # prints "Done!" after loop finishes normally

# --- break, continue, pass ---
"""
break   — exits the loop immediately
continue — skips to the next iteration
pass    — does nothing (placeholder for empty block)
"""

for i in range(10):
    if i == 5:
        break           # stop loop when i is 5
    if i % 2 == 0:
        continue        # skip even numbers
    print(i)            # prints 1, 3 (odd numbers before 5)

# pass as placeholder
def not_implemented_yet():
    pass    # function body cannot be empty; pass satisfies this

# for/else — else runs only if loop was NOT broken
for num in [2, 4, 6, 8]:
    if num % 2 != 0:
        print("Found odd!")
        break
else:
    print("All even!")  # prints because no break occurred


# =============================================================================
# SECTION 6: FUNCTIONS
# =============================================================================
"""
Functions are reusable blocks of code defined with the `def` keyword.
They promote DRY (Don't Repeat Yourself) principles.
"""

# --- Basic function ---
def greet(name):
    """Return a greeting message. (This is a docstring)"""
    return f"Hello, {name}!"

message = greet("Alice")

# --- Default parameter values ---
def power(base, exponent=2):
    """Calculate base raised to exponent. Default exponent is 2."""
    return base ** exponent

print(power(3))         # 9  (uses default exponent=2)
print(power(3, 3))      # 27 (overrides default)

# --- Keyword arguments ---
# Arguments can be passed by name in any order.
def create_profile(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

profile = create_profile(age=25, name="Bob", city="NYC")

# --- *args — variable positional arguments ---
# Collects extra positional arguments into a tuple.
def sum_all(*numbers):
    """Sum any number of arguments."""
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))   # 15

# --- **kwargs — variable keyword arguments ---
# Collects extra keyword arguments into a dictionary.
def print_info(**details):
    """Print arbitrary key-value pairs."""
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=30, role="Engineer")

# --- Combining all parameter types ---
# Order: regular, *args, keyword-only, **kwargs
def full_example(required, *args, keyword_only=True, **kwargs):
    print(required, args, keyword_only, kwargs)

full_example("hello", 1, 2, 3, keyword_only=False, extra="yes")

# --- Return multiple values (returns a tuple) ---
def min_max(numbers):
    """Return the minimum and maximum of a list."""
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")   # Min: 1, Max: 9

# --- Lambda functions (anonymous functions) ---
"""
Short, one-expression functions. Useful as arguments to higher-order functions.
Syntax: lambda parameters: expression
"""
square = lambda x: x ** 2
add = lambda x, y: x + y

# Common use with sorted, map, filter
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
students.sort(key=lambda s: s[1], reverse=True)   # sort by score descending

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))    # [2, 4, 6]
doubled = list(map(lambda x: x * 2, numbers))           # [2, 4, 6, 8, 10, 12]

# --- Higher-order functions ---
# Functions that take or return other functions.
def apply_twice(func, value):
    """Apply a function to a value twice."""
    return func(func(value))

result = apply_twice(lambda x: x + 3, 10)  # 16 (10+3=13, 13+3=16)

# --- Closures ---
"""
A closure is a function that remembers values from its enclosing scope,
even after that scope has finished executing.
"""
def make_multiplier(factor):
    def multiply(number):
        return number * factor      # `factor` is captured from outer scope
    return multiply

triple = make_multiplier(3)
print(triple(5))    # 15
print(triple(7))    # 21

# --- Decorators ---
"""
Decorators wrap a function to add behavior before/after it runs.
They use the @syntax_sugar notation.
"""
import functools
import time

def timer(func):
    """Decorator that measures execution time of a function."""
    @functools.wraps(func)  # preserves original function's metadata
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

def logger(func):
    """Decorator that logs function calls."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timer
@logger     # decorators are applied bottom-up (logger first, then timer)
def add_numbers(x, y):
    """Add two numbers."""
    return x + y

add_numbers(3, 4)

# Decorator with arguments
def repeat(n):
    """Decorator factory: repeats the function n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()     # prints "Hello!" three times

# --- Generators ---
"""
Generators produce values lazily (one at a time), saving memory.
They use `yield` instead of `return`.
A generator function returns a generator object (an iterator).
"""
def count_up(start, end):
    """Generator that yields numbers from start to end."""
    current = start
    while current <= end:
        yield current       # pause and send value to caller
        current += 1

gen = count_up(1, 5)
print(next(gen))    # 1
print(next(gen))    # 2
for val in count_up(3, 6):
    print(val)      # 3, 4, 5, 6

# Generator expression (like list comprehension but lazy)
gen_expr = (x**2 for x in range(100_000))  # no memory allocated yet
first_square = next(gen_expr)   # compute only first value

# Infinite generator
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))    # 0, 1, 2, 3, 4


# =============================================================================
# SECTION 7: COMPREHENSIONS
# =============================================================================
"""
Comprehensions provide a concise way to create collections from iterables.
They are more Pythonic and typically faster than equivalent for loops.
"""

# --- List comprehension ---
# [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(20) if x % 2 == 0]
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]

# Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1,2,3],[2,4,6],[3,6,9]]

# Flatten a 2D list
flat = [num for row in matrix for num in row]

# --- Dict comprehension ---
# {key_expr: value_expr for item in iterable if condition}
squared_dict = {x: x**2 for x in range(1, 6)}
inverted = {v: k for k, v in {"a": 1, "b": 2, "c": 3}.items()}

# --- Set comprehension ---
unique_lengths = {len(w) for w in ["apple", "banana", "kiwi", "fig"]}
# {3, 4, 5, 6}

# --- Generator expression ---
total = sum(x**2 for x in range(100))   # memory-efficient sum of squares


# =============================================================================
# SECTION 8: OBJECT-ORIENTED PROGRAMMING (OOP)
# =============================================================================
"""
OOP organizes code around objects that bundle data (attributes) and
behavior (methods). Core pillars: Encapsulation, Inheritance,
Polymorphism, Abstraction.
"""

# --- Basic class ---
class Animal:
    """Represents a generic animal."""

    species = "Unknown"     # class variable: shared by all instances

    def __init__(self, name, age):
        """
        __init__ is the constructor — called when creating an instance.
        `self` refers to the instance being created.
        """
        self.name = name        # instance variable: unique to each instance
        self.age = age
        self._health = 100      # convention: _ prefix = "protected" (not enforced)
        self.__secret = "hidden" # __prefix = name-mangled (harder to access externally)

    def speak(self):
        """Method that all animals should implement."""
        return f"{self.name} makes a sound."

    def __str__(self):
        """Called by str() and print(). Human-readable representation."""
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self):
        """Called by repr(). Unambiguous representation for developers."""
        return f"Animal('{self.name}', {self.age})"

    def __len__(self):
        """Called by len()."""
        return self.age

    @classmethod
    def from_dict(cls, data):
        """
        Class method — receives class (cls) instead of instance (self).
        Often used as an alternative constructor.
        """
        return cls(data["name"], data["age"])

    @staticmethod
    def is_adult(age, adulthood=2):
        """
        Static method — no access to class or instance.
        Logically belongs to the class but doesn't need class/instance state.
        """
        return age >= adulthood

    @property
    def health(self):
        """Property — access like an attribute, but it's a method."""
        return self._health

    @health.setter
    def health(self, value):
        """Setter — validates/processes values on assignment."""
        if not 0 <= value <= 100:
            raise ValueError("Health must be between 0 and 100")
        self._health = value


# --- Inheritance ---
class Dog(Animal):
    """Dog inherits from Animal and adds its own behavior."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)     # call parent __init__
        self.breed = breed

    def speak(self):
        """Overrides the parent's speak method (polymorphism)."""
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


# --- Polymorphism ---
animals = [Dog("Rex", 3, "Labrador"), Cat("Whiskers", 5), Dog("Buddy", 2, "Poodle")]
for animal in animals:
    print(animal.speak())   # each object uses its own speak() implementation


# --- Multiple inheritance ---
class Flyable:
    """Mixin: adds flying capability."""
    def fly(self):
        return "I can fly!"

class Swimmable:
    """Mixin: adds swimming capability."""
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable, Animal):
    """Duck can fly, swim, and is an Animal."""
    def speak(self):
        return f"{self.name} says: Quack!"


# --- Abstract Base Classes ---
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class — cannot be instantiated directly."""

    @abstractmethod
    def area(self):
        """Subclasses MUST implement this method."""
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        """Concrete method available to all subclasses."""
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    import math
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

rect = Rectangle(5, 3)
print(rect.describe())  # Area: 15.00, Perimeter: 16.00

# --- Dataclasses (Python 3.7+) ---
"""
Dataclasses auto-generate __init__, __repr__, __eq__, and optionally more.
Ideal for simple data containers.
"""
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0          # default value
    tags: list = field(default_factory=list)  # mutable default must use field()

    def distance_to_origin(self):
        import math
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

p = Point(1.0, 2.0)
print(p)            # Point(x=1.0, y=2.0, z=0.0, tags=[])
print(p == Point(1.0, 2.0))  # True (auto-generated __eq__)


# =============================================================================
# SECTION 9: EXCEPTION HANDLING
# =============================================================================
"""
Exceptions are runtime errors. Python's exception handling follows the
EAFP (Easier to Ask Forgiveness than Permission) philosophy.

Exception hierarchy (partial):
    BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    └── Exception
        ├── ValueError
        ├── TypeError
        ├── NameError
        ├── IndexError
        ├── KeyError
        ├── AttributeError
        ├── FileNotFoundError
        ├── ZeroDivisionError
        ├── StopIteration
        ├── RuntimeError
        └── ... (many more)
"""

# --- Basic try/except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# --- Multiple exceptions ---
def safe_parse(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer")
        return None
    except TypeError:
        print("Input must be a string or number")
        return None

# --- Catch multiple in one except ---
try:
    data = {}
    x = data["key"]
except (KeyError, IndexError) as e:
    print(f"Key or index error: {e}")

# --- else and finally ---
"""
else   — runs only if NO exception was raised in try
finally — ALWAYS runs, exception or not (used for cleanup)
"""
def read_number(s):
    try:
        num = int(s)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    else:
        print(f"Successfully parsed: {num}")   # only if no exception
        return num
    finally:
        print("Attempted to parse:", s)    # always runs

# --- Raising exceptions ---
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of realistic range (0–150)")
    return True

# Re-raising exceptions
def process():
    try:
        validate_age(-5)
    except ValueError:
        print("Logging the error...")
        raise   # re-raise the same exception up the call stack

# --- Custom exceptions ---
class AppError(Exception):
    """Base exception for this application."""
    pass

class DatabaseError(AppError):
    """Raised when a database operation fails."""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class NotFoundError(AppError):
    """Raised when a resource is not found."""
    pass

try:
    raise DatabaseError("Connection failed", error_code=500)
except DatabaseError as e:
    print(f"DB Error (code {e.error_code}): {e}")

# --- Context managers with exception handling ---
# with statement ensures __enter__ and __exit__ are called
# __exit__ is called even if an exception occurs
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found — handled gracefully")


# =============================================================================
# SECTION 10: FILE I/O
# =============================================================================
"""
Python's built-in `open()` function handles file operations.
Always use `with` to ensure files are properly closed.

Modes:
    'r'   — read (default)
    'w'   — write (creates or overwrites)
    'a'   — append
    'x'   — exclusive creation (fails if file exists)
    'b'   — binary mode (combined: 'rb', 'wb')
    't'   — text mode (default, combined: 'rt', 'wt')
    '+'   — read and write (combined: 'r+', 'w+')
"""

import os

# --- Writing a file ---
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.writelines(["Line 3\n", "Line 4\n"])   # write multiple lines

# --- Reading a file ---
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()          # read entire file as string
    # f.read(100)               # read first 100 characters
    # lines = f.readlines()     # read all lines into a list
    # line = f.readline()       # read one line at a time

# Reading line by line (memory-efficient for large files)
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())     # strip removes the trailing newline

# --- Appending to a file ---
with open("sample.txt", "a") as f:
    f.write("Line 5\n")

# --- Working with paths ---
import pathlib

# pathlib.Path — object-oriented path manipulation (Python 3.4+)
path = pathlib.Path("sample.txt")
print(path.exists())        # True
print(path.name)            # 'sample.txt'
print(path.stem)            # 'sample'
print(path.suffix)          # '.txt'
print(path.parent)          # '.' (current directory)
print(path.absolute())      # full absolute path

# Create directories
pathlib.Path("new_dir/sub_dir").mkdir(parents=True, exist_ok=True)

# List directory contents
for item in pathlib.Path(".").iterdir():
    print(item)

# Glob patterns
for py_file in pathlib.Path(".").glob("*.py"):
    print(py_file)

# --- Working with JSON ---
import json

data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# Write JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)    # indent for pretty-printing

# Read JSON
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded["name"])   # 'Alice'

# Convert to/from JSON string
json_str = json.dumps(data)         # dict → JSON string
parsed = json.loads(json_str)       # JSON string → dict

# Cleanup sample files
for fname in ["sample.txt", "data.json"]:
    if os.path.exists(fname):
        os.remove(fname)


# =============================================================================
# SECTION 11: MODULES AND PACKAGES
# =============================================================================
"""
A module is a .py file. A package is a directory with an __init__.py file.
The standard library contains hundreds of built-in modules.

Import styles:
    import module               — import whole module
    import module as alias      — import with alias
    from module import name     — import specific name
    from module import *        — import all public names (avoid in production)
"""

import math
import random
import datetime
import itertools
import functools
import os
import sys

# math module
print(math.pi)          # 3.14159...
print(math.e)           # 2.71828...
print(math.sqrt(16))    # 4.0
print(math.ceil(3.2))   # 4
print(math.floor(3.8))  # 3
print(math.log(100, 10)) # 2.0
print(math.factorial(5)) # 120

# random module
print(random.random())              # float in [0, 1)
print(random.randint(1, 10))        # int in [1, 10]
print(random.choice(["a", "b", "c"]))  # random element
sample = random.sample(range(100), 5)  # 5 unique random numbers
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)    # shuffle in place

# datetime module
now = datetime.datetime.now()
today = datetime.date.today()
delta = datetime.timedelta(days=30)
future = today + delta
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # format datetime as string
print(datetime.datetime.strptime("2024-01-15", "%Y-%m-%d"))  # parse string

# itertools module
from itertools import chain, combinations, permutations, product, islice

print(list(chain([1, 2], [3, 4], [5])))     # [1,2,3,4,5]
print(list(combinations("ABC", 2)))         # [('A','B'),('A','C'),('B','C')]
print(list(permutations("AB", 2)))          # [('A','B'),('B','A')]
print(list(product([0,1], repeat=2)))       # [(0,0),(0,1),(1,0),(1,1)]
print(list(islice(infinite_counter(), 5)))  # [0,1,2,3,4]

# functools module
from functools import reduce, partial, lru_cache

total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])    # 15

def multiply(x, y):
    return x * y

double = partial(multiply, 2)   # partial application
print(double(5))    # 10
print(double(7))    # 14

@lru_cache(maxsize=None)    # memoize function results
def fibonacci(n):
    """Recursive fibonacci with memoization via lru_cache."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))    # fast due to caching

# os module
print(os.getcwd())              # current working directory
print(os.listdir("."))          # list directory contents
print(os.path.join("a", "b"))  # OS-appropriate path separator
print(os.environ.get("HOME"))   # environment variable
os.makedirs("temp_dir", exist_ok=True)
os.rmdir("temp_dir")

# sys module
print(sys.version)          # Python version string
print(sys.platform)         # 'linux', 'darwin', 'win32'
print(sys.path)             # list of directories Python searches for modules
# sys.exit(0)              # exit program with code 0


# =============================================================================
# SECTION 12: ADVANCED TOPICS
# =============================================================================

# --- Context Managers ---
"""
Objects that define __enter__ and __exit__ for use with `with` statement.
"""
class ManagedResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Acquiring {self.name}")
        return self     # returned as the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing {self.name}")
        # Return True to suppress exceptions, False (or None) to propagate
        return False

with ManagedResource("database connection") as resource:
    print(f"Using {resource.name}")

# contextlib.contextmanager — decorator-based context manager
from contextlib import contextmanager

@contextmanager
def temporary_file(filename):
    """Context manager that creates and cleans up a temp file."""
    try:
        with open(filename, "w") as f:
            yield f         # everything after yield is __exit__
    finally:
        if os.path.exists(filename):
            os.remove(filename)

with temporary_file("temp.txt") as f:
    f.write("temporary data")

# --- Type Hints (Python 3.5+) ---
"""
Optional type annotations for better readability and IDE support.
Checked by tools like mypy, not enforced at runtime.
"""
from typing import List, Dict, Tuple, Optional, Union, Any, Callable

def process_items(items: List[int], multiplier: float = 1.0) -> List[float]:
    return [item * multiplier for item in items]

def find_user(user_id: int) -> Optional[Dict[str, Any]]:
    """Returns a user dict or None if not found."""
    users = {1: {"name": "Alice"}}
    return users.get(user_id)

def apply_operation(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Python 3.10+ simplified union type
def handle_input(value: int | str | None) -> str:
    return str(value)

# --- Walrus operator := (Python 3.8+) ---
"""
Assignment expression: assigns and returns a value in one step.
Useful to avoid computing a value twice.
"""
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Without walrus
filtered = []
for x in data:
    y = x ** 2
    if y > 25:
        filtered.append(y)

# With walrus
filtered = [y for x in data if (y := x ** 2) > 25]

# While loop with walrus — read until sentinel
import io
buffer = io.StringIO("line1\nline2\nline3")
while line := buffer.readline():
    print(line.strip())

# --- Unpacking and starred expressions ---
first, *rest = [1, 2, 3, 4, 5]    # first=1, rest=[2,3,4,5]
*init, last = [1, 2, 3, 4, 5]     # init=[1,2,3,4], last=5
a, *b, c = [1, 2, 3, 4, 5]        # a=1, b=[2,3,4], c=5

# Merge lists/dicts with unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]         # [1,2,3,4,5,6]

dict1 = {"a": 1}
dict2 = {"b": 2}
merged_dict = {**dict1, **dict2}   # {"a":1, "b":2}

# --- Slots ---
"""
__slots__ restricts instance attributes to a fixed set,
saving memory by avoiding per-instance __dict__.
"""
class Optimized:
    __slots__ = ["x", "y"]     # only x and y allowed as attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y


# =============================================================================
# SECTION 13: USEFUL BUILT-IN FUNCTIONS
# =============================================================================

# abs()
print(abs(-5))      # 5

# all() / any()
print(all([True, True, False]))     # False (all must be True)
print(any([False, False, True]))    # True (any must be True)

# dir() — list attributes of an object
print(dir([]))      # list of list methods and attributes

# enumerate()
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# filter() — returns iterator of items where func returns True
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# map() — apply function to each item
doubled = list(map(lambda x: x * 2, range(5)))

# zip() — pair up iterables
pairs = list(zip([1, 2, 3], ["a", "b", "c"]))   # [(1,'a'),(2,'b'),(3,'c')]

# sorted() — return sorted list (non-destructive)
sorted_data = sorted([3, 1, 4, 1, 5], reverse=True)
sorted_words = sorted(["banana", "apple", "cherry"], key=len)  # by length

# min() / max() — with key function
longest = max(["cat", "elephant", "dog"], key=len)  # 'elephant'

# sum() — with optional start value
total = sum([1, 2, 3, 4, 5], 100)  # 115 (starts from 100)

# range()
print(list(range(5)))           # [0,1,2,3,4]
print(list(range(2, 8, 2)))     # [2,4,6]

# isinstance() / issubclass()
print(isinstance(42, int))              # True
print(isinstance(42, (int, float)))     # True (checks against tuple of types)
print(issubclass(bool, int))            # True (bool is subclass of int)

# hasattr() / getattr() / setattr() / delattr()
class Demo:
    x = 10
d = Demo()
print(hasattr(d, "x"))          # True
print(getattr(d, "x", "N/A"))   # 10 (with default if missing)
setattr(d, "y", 20)             # d.y = 20
delattr(d, "y")                 # del d.y

# vars() — return __dict__ of object
print(vars(d))  # {'x': 10}

# id() — memory address of object
print(id(42))

# hash() — hash value (for use in dicts/sets)
print(hash("hello"))

# callable() — True if object is callable
print(callable(print))      # True
print(callable(42))         # False

# repr() / str()
print(repr("hello\n"))      # "'hello\\n'" — shows escape sequences
print(str("hello\n"))       # "hello\n" — evaluates escape sequences

# open() — already covered in File I/O section

# input() — get user input (not used here, but important)
# user_input = input("Enter a value: ")  # always returns a string

# print() — full signature
print("a", "b", "c", sep="-", end="!\n")  # "a-b-c!"


# =============================================================================
# SECTION 14: BEST PRACTICES AND PYTHONIC IDIOMS
# =============================================================================

# --- PEP 8 naming conventions ---
# module_name, package_name
# ClassName, ExceptionName
# function_name, method_name, variable_name
# CONSTANT_NAME
# _protected_var, __private_var

MAX_RETRIES = 3     # constant: UPPER_SNAKE_CASE

# --- Swap without temp variable ---
a, b = 1, 2
a, b = b, a

# --- Conditional import ---
try:
    import ujson as json_lib    # fast JSON library
except ImportError:
    import json as json_lib     # fall back to standard library

# --- Use enumerate instead of range(len(...)) ---
items = ["a", "b", "c"]
# Bad:
for i in range(len(items)):
    print(i, items[i])
# Good:
for i, item in enumerate(items):
    print(i, item)

# --- String joining ---
words_list = ["Hello", "World", "Python"]
# Bad: string concatenation in loop (creates many temp strings)
result = ""
for w in words_list:
    result += w + " "
# Good:
result = " ".join(words_list)

# --- Check for None explicitly ---
value = None
# Bad:
if value == None:
    pass
# Good:
if value is None:
    pass

# --- Use 'in' to check membership ---
if "apple" in ["apple", "banana"]:  # O(n) for list, O(1) for set/dict
    pass

# --- Dictionary .get() instead of KeyError ---
d = {"key": "value"}
# Bad:
if "key" in d:
    val = d["key"]
# Good:
val = d.get("key", "default")

# --- Unpack iterables ---
point = (10, 20)
# Bad:
x = point[0]
y = point[1]
# Good:
x, y = point

# --- Use list comprehensions over manual loops ---
# Bad:
squares = []
for n in range(10):
    squares.append(n ** 2)
# Good:
squares = [n ** 2 for n in range(10)]

print("\n=== Python Fundamentals Guide Complete ===")
print("This file covers: Variables, Types, Operators, Strings, Collections,")
print("Control Flow, Functions, Comprehensions, OOP, Exceptions, File I/O,")
print("Modules, and Advanced Topics.")
