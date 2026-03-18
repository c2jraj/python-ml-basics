# tuples_and_sets.py
# Demonstrates Python tuples (immutable sequences) and sets (unique collections).

from collections import namedtuple

# ── TUPLES ──────────────────────────────────────────────────────────────────

# Creation
coordinates = (40.7128, -74.0060)
rgb = (255, 128, 0)
single = (42,)           # single-element tuple requires trailing comma
empty = ()

print("coordinates:", coordinates)
print("rgb:", rgb)
print("single:", single)
print("empty:", empty)

# Access and slicing
print(f"\nLatitude:  {coordinates[0]}")
print(f"Longitude: {coordinates[1]}")
print(f"First two RGB: {rgb[:2]}")

# Unpacking
lat, lon = coordinates
r, g, b = rgb
print(f"\nUnpacked: lat={lat}, lon={lon}")
print(f"Unpacked: r={r}, g={g}, b={b}")

# Tuples are immutable
try:
    coordinates[0] = 0
except TypeError as e:
    print(f"\nImmutability check: {e}")

# Named tuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"\nNamedTuple Point: {p}, x={p.x}, y={p.y}")

# Tuple as dict key (hashable)
distances = {(0, 0): 0, (3, 4): 5, (6, 8): 10}
print("Tuple as dict keys:", distances)

# ── SETS ─────────────────────────────────────────────────────────────────────

# Creation
primes = {2, 3, 5, 7, 11}
evens = {2, 4, 6, 8, 10}
print("\n--- Sets ---")
print("Primes:", primes)
print("Evens:", evens)

# Add and remove
primes.add(13)
primes.discard(100)   # no error if missing
print("After add(13) & discard(100):", primes)

# Set operations
print(f"\nUnion:        {primes | evens}")
print(f"Intersection: {primes & evens}")
print(f"Difference:   {primes - evens}")
print(f"Symmetric diff: {primes ^ evens}")

# Membership
print(f"\n7 in primes: {7 in primes}")
print(f"9 in primes: {9 in primes}")

# Deduplication
duplicates = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(duplicates))
print(f"\nDeduplicated {duplicates} -> {sorted(unique)}")

# Frozenset (immutable set)
frozen = frozenset([1, 2, 3, 2, 1])
print(f"\nFrozenset: {frozen}")
