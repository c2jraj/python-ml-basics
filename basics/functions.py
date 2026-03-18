# functions.py
# Demonstrates function definitions, default arguments, *args, **kwargs,
# lambda expressions, and recursion.


def greet(name, greeting="Hello"):
    """Return a greeting string."""
    return f"{greeting}, {name}!"


def add(*numbers):
    """Return the sum of any number of arguments."""
    return sum(numbers)


def describe_person(**attributes):
    """Print key-value pairs describing a person."""
    for key, value in attributes.items():
        print(f"  {key}: {value}")


def factorial(n):
    """Return n! using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# --- Lambda ---
square = lambda x: x ** 2  # noqa: E731

# --- Higher-order functions ---
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))


if __name__ == "__main__":
    print(greet("Alice"))
    print(greet("Bob", greeting="Hi"))

    print(f"\nadd(1, 2, 3) = {add(1, 2, 3)}")
    print(f"add(10, 20)  = {add(10, 20)}")

    print("\ndescribe_person:")
    describe_person(name="Carol", age=30, city="New York")

    print(f"\nfactorial(6) = {factorial(6)}")

    print(f"\nsquare(9) via lambda = {square(9)}")

    print(f"\nOriginal numbers: {numbers}")
    print(f"Even numbers:     {evens}")
    print(f"Doubled numbers:  {doubled}")
