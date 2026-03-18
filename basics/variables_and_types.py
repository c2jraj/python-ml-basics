# variables_and_types.py
# Demonstrates Python variable assignment and built-in data types.

# Integer
age = 25
print("Age:", age, "| type:", type(age))

# Float
height = 5.9
print("Height:", height, "| type:", type(height))

# String
name = "Alice"
print("Name:", name, "| type:", type(name))

# Boolean
is_student = True
print("Is student:", is_student, "| type:", type(is_student))

# NoneType
score = None
print("Score:", score, "| type:", type(score))

# String formatting
print(f"\n{name} is {age} years old and {height} ft tall.")

# Type conversion
age_str = str(age)
height_int = int(height)
print(f"\nConverted age to string: '{age_str}' ({type(age_str).__name__})")
print(f"Converted height to int: {height_int} ({type(height_int).__name__})")

# Basic arithmetic
a, b = 10, 3
print(f"\nArithmetic with a={a}, b={b}:")
print(f"  Addition:       {a} + {b} = {a + b}")
print(f"  Subtraction:    {a} - {b} = {a - b}")
print(f"  Multiplication: {a} * {b} = {a * b}")
print(f"  Division:       {a} / {b} = {a / b:.4f}")
print(f"  Floor division: {a} // {b} = {a // b}")
print(f"  Modulus:        {a} % {b} = {a % b}")
print(f"  Exponentiation: {a} ** {b} = {a ** b}")
