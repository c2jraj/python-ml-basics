# file_operations.py
# Demonstrates reading and writing plain text files, working with file paths,
# and handling common file-related exceptions.

import os

SAMPLE_FILE = "sample.txt"


def write_file(path, lines):
    """Write a list of strings to a text file (one per line)."""
    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(line + "\n" for line in lines)
    print(f"Written {len(lines)} lines to '{path}'.")


def read_file(path):
    """Read and return all lines from a text file."""
    with open(path, "r", encoding="utf-8") as fh:
        return fh.readlines()


def append_to_file(path, text):
    """Append a single line to an existing file."""
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"Appended line to '{path}'.")


def read_specific_lines(path, start, end):
    """Return lines [start, end) from a file (0-indexed)."""
    result = []
    with open(path, "r", encoding="utf-8") as fh:
        for i, line in enumerate(fh):
            if i >= end:
                break
            if i >= start:
                result.append(line)
    return result


if __name__ == "__main__":
    # ── Write ──────────────────────────────────────────────────────────────
    data = [
        "Line 1: Hello, World!",
        "Line 2: Python file handling is straightforward.",
        "Line 3: Always use context managers (with statement).",
        "Line 4: Specify encoding to avoid platform issues.",
    ]
    write_file(SAMPLE_FILE, data)

    # ── Read all ───────────────────────────────────────────────────────────
    print("\nAll lines:")
    for line in read_file(SAMPLE_FILE):
        print(" ", line.rstrip())

    # ── Append ─────────────────────────────────────────────────────────────
    append_to_file(SAMPLE_FILE, "Line 5: Appended after initial write.")

    # ── Read specific lines ────────────────────────────────────────────────
    print("\nLines 2-4 (0-indexed):")
    for line in read_specific_lines(SAMPLE_FILE, 1, 4):
        print(" ", line.rstrip())

    # ── File metadata ──────────────────────────────────────────────────────
    size = os.path.getsize(SAMPLE_FILE)
    print(f"\nFile size: {size} bytes")
    print(f"Absolute path: {os.path.abspath(SAMPLE_FILE)}")

    # ── Exception handling ─────────────────────────────────────────────────
    try:
        with open("nonexistent.txt", "r", encoding="utf-8") as fh:
            fh.read()
    except FileNotFoundError as e:
        print(f"\nExpected error caught: {e}")

    # ── Cleanup ────────────────────────────────────────────────────────────
    os.remove(SAMPLE_FILE)
    print(f"\n'{SAMPLE_FILE}' removed.")
