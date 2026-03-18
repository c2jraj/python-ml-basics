# dictionaries.py
# Demonstrates Python dictionary creation, access, update, iteration,
# nested dicts, and dict comprehensions.

# --- Creation ---
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "courses": ["Math", "Physics", "Computer Science"],
}
print("Student dict:", student)

# --- Access ---
print(f"\nName:  {student['name']}")
print(f"Grade: {student.get('grade', 'N/A')}")
print(f"GPA:   {student.get('gpa', 'Not available')}")  # missing key with default

# --- Update ---
student["age"] = 22
student["gpa"] = 3.9
print(f"\nUpdated student: {student}")

# --- Delete ---
student_copy = dict(student)
del student_copy["grade"]
removed = student_copy.pop("gpa", None)
print(f"After deletions (removed gpa={removed}): {student_copy}")

# --- Iteration ---
print("\nIterating over key-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\nKeys:  ", list(student.keys()))
print("Values:", list(student.values()))

# --- Nested dictionary ---
school = {
    "Alice": {"age": 22, "grade": "A"},
    "Bob": {"age": 20, "grade": "B"},
    "Carol": {"age": 23, "grade": "A+"},
}
print("\nNested school dict:")
for name, info in school.items():
    print(f"  {name}: age={info['age']}, grade={info['grade']}")

# --- Dict comprehension ---
squared = {x: x ** 2 for x in range(1, 6)}
print("\nSquares (dict comprehension):", squared)

# --- Merge dicts (Python 3.9+) ---
defaults = {"color": "blue", "font": "Arial", "size": 12}
overrides = {"color": "red", "size": 14}
merged = {**defaults, **overrides}
print("\nMerged dict:", merged)

# --- Counting with dict ---
sentence = "the quick brown fox jumps over the lazy dog"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"\nWord counts (partial): { {k: v for k, v in word_count.items() if v > 1} }")
