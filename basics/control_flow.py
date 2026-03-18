# control_flow.py
# Demonstrates if/elif/else, for loops, while loops, and comprehensions.

# --- if / elif / else ---
temperature = 22

if temperature > 30:
    weather = "hot"
elif temperature > 20:
    weather = "warm"
elif temperature > 10:
    weather = "cool"
else:
    weather = "cold"

print(f"Temperature {temperature}°C is {weather}.")

# --- for loop ---
fruits = ["apple", "banana", "cherry"]
print("\nFruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# --- range-based for loop ---
print("\nSquares of 1-5:")
for i in range(1, 6):
    print(f"  {i}^2 = {i ** 2}")

# --- while loop ---
count = 0
total = 0
while count < 5:
    count += 1
    total += count
print(f"\nSum of 1 to 5 = {total}")

# --- break and continue ---
print("\nEven numbers up to 10 (skip multiples of 6):")
for n in range(2, 11, 2):
    if n % 6 == 0:
        continue
    print(f"  {n}")

# --- list comprehension ---
squares = [x ** 2 for x in range(1, 6)]
print("\nList comprehension — squares:", squares)

# --- conditional comprehension ---
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)
