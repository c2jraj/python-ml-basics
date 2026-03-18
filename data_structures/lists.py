# lists.py
# Demonstrates Python list operations, slicing, sorting, and common methods.

# --- Creation ---
fruits = ["banana", "apple", "cherry", "date", "elderberry"]
print("Original list:", fruits)

# --- Access and slicing ---
print(f"\nFirst element:  {fruits[0]}")
print(f"Last element:   {fruits[-1]}")
print(f"Slice [1:3]:    {fruits[1:3]}")
print(f"Every 2nd item: {fruits[::2]}")

# --- Modification ---
fruits.append("fig")
fruits.insert(2, "blueberry")
print(f"\nAfter append + insert: {fruits}")

fruits.remove("date")
popped = fruits.pop()
print(f"After remove + pop ('{popped}'): {fruits}")

# --- Sorting ---
fruits.sort()
print(f"\nSorted:         {fruits}")
fruits.sort(reverse=True)
print(f"Reverse sorted: {fruits}")

# --- Searching ---
print(f"\n'apple' in list: {'apple' in fruits}")
print(f"Index of 'apple': {fruits.index('apple')}")
print(f"Count of 'apple': {fruits.count('apple')}")

# --- List operations ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"\nNumbers: {numbers}")
print(f"Min: {min(numbers)}, Max: {max(numbers)}, Sum: {sum(numbers)}")
print(f"Sorted (unique): {sorted(set(numbers))}")

# --- Nested list (2-D) ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\n2-D matrix:")
for row in matrix:
    print(" ", row)
print(f"Element at [1][2]: {matrix[1][2]}")

# --- Flatten with comprehension ---
flat = [val for row in matrix for val in row]
print(f"Flattened: {flat}")
