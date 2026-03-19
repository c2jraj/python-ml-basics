# Prompt Engineering Examples

---

## Good Prompts

### Prompt 1 — Clear and Specific

**Prompt:**
> write a python function that calculates the factorial of a number

**Why it works:**
- Specifies the **language** (Python)
- Specifies the **output format** (a function)
- Specifies the **task** clearly (calculate factorial)

**Response:**
```python
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

---

### Prompt 2 — Clear with Extra Instructions

**Prompt:**
> write a python function to reverse a string, include comments explaining each steps

**Why it works:**
- Specifies the **language** (Python)
- Specifies the **output format** (a function)
- Specifies the **task** (reverse a string)
- Adds a **style requirement** (include comments explaining each step)

**Response:**
```python
def reverse_string(s):
    # Convert the string to a list of characters
    chars = list(s)

    # Set two pointers: one at the start, one at the end
    left, right = 0, len(chars) - 1

    # Swap characters moving inward until the pointers meet
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    # Join the list back into a string and return it
    return ''.join(chars)
```

---

## Bad Prompt

### Prompt 3 — Vague and Missing Context

**Prompt:**
> summarize this text in 3 bullet points

**Why it fails:**
- **No input provided** — the prompt says "this text" but doesn't include any text to summarize.
- **Assumes context** — the AI has no way to know what "this text" refers to.
- The task itself (summarize in 3 bullet points) is clear, but without the actual content, the prompt is **incomplete and unanswerable**.

**Response:**
> No text was provided. Please share the text you'd like me to summarize.

**How to fix it:**
> Summarize the following text in 3 bullet points:
>
> *[paste the actual text here]*

---

## Key Takeaways

| Trait | Good Prompt | Bad Prompt |
|---|---|---|
| **Clarity** | States the task explicitly | Task is clear but incomplete |
| **Context** | Self-contained, no external info needed | References missing content ("this text") |
| **Specificity** | Defines language, format, and style | Leaves out critical input |
| **Actionable** | AI can respond immediately | AI must ask for clarification |
