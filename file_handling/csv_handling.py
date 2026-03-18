# csv_handling.py
# Demonstrates reading and writing CSV files using Python's csv module.

import csv
import os

CSV_FILE = "students.csv"

FIELDNAMES = ["name", "age", "grade", "score"]

STUDENTS = [
    {"name": "Alice", "age": 21, "grade": "A", "score": 95.5},
    {"name": "Bob", "age": 22, "grade": "B", "score": 82.0},
    {"name": "Carol", "age": 20, "grade": "A+", "score": 98.3},
    {"name": "Dave", "age": 23, "grade": "C", "score": 70.1},
    {"name": "Eve", "age": 21, "grade": "B+", "score": 87.4},
]


def write_csv(path, fieldnames, rows):
    """Write a list of dicts to a CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to '{path}'.")


def read_csv(path):
    """Read a CSV file and return a list of dicts."""
    with open(path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def filter_students(rows, min_score):
    """Return students whose score is >= min_score."""
    return [r for r in rows if float(r["score"]) >= min_score]


def average_score(rows):
    """Return the average score across all rows."""
    scores = [float(r["score"]) for r in rows]
    return sum(scores) / len(scores) if scores else 0.0


if __name__ == "__main__":
    # ── Write ──────────────────────────────────────────────────────────────
    write_csv(CSV_FILE, FIELDNAMES, STUDENTS)

    # ── Read ───────────────────────────────────────────────────────────────
    records = read_csv(CSV_FILE)
    print("\nAll students from CSV:")
    for rec in records:
        print(f"  {rec['name']:6} | age {rec['age']} | grade {rec['grade']:3} | score {rec['score']}")

    # ── Filter ─────────────────────────────────────────────────────────────
    top_students = filter_students(records, 85.0)
    print(f"\nStudents scoring >= 85.0 ({len(top_students)}):")
    for rec in top_students:
        print(f"  {rec['name']} ({rec['score']})")

    # ── Statistics ─────────────────────────────────────────────────────────
    avg = average_score(records)
    print(f"\nClass average score: {avg:.2f}")

    # ── Cleanup ────────────────────────────────────────────────────────────
    os.remove(CSV_FILE)
    print(f"\n'{CSV_FILE}' removed.")
