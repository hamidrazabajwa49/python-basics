# 📁 6 — Problem Solving

This is where everything comes together. Each file in this module takes a real programming problem, solves it cleanly using functions, and verifies the solution with written test cases. This is how professional developers think — write the solution, then prove it works.

---

## 📂 Files in This Module

| # | File | Problem |
|---|---|---|
| 0 | `0_common_characters.py` | Find characters common to two strings |
| 1 | `1_most_frequent_char.py` | Find the most frequently occurring character |
| 2 | `2_string_to_tuple_list.py` | Convert a string into a list of tuples |
| 3 | `3_swap_tuple_elements.py` | Swap elements inside tuples |
| 4 | `4_anagram_pairs.py` | Detect whether two strings are anagrams |

---

## 📄 Problem Breakdown

### `0_common_characters.py` — Common Characters

**Problem:** Given two strings, find all characters that appear in both — the intersection of their character sets.

**Approach:**
- Convert both strings into sets to eliminate duplicates
- Use set intersection to find shared characters
- Return the result as a sorted list for consistent, readable output

**Example:**
```
Input:  "hello"  ,  "world"
Output: ['l', 'o']
```

**What the test cases cover:**
- Two strings with multiple common characters
- Two strings with only one character in common
- Strings with no common characters at all (empty result)
- Strings with repeated characters — confirms duplicates are handled correctly
- Case sensitivity — `'A'` and `'a'` treated as different characters

---

### `1_most_frequent_char.py` — Most Frequent Character

**Problem:** Given a string, find the character that appears the most number of times.

**Approach:**
- Build a frequency dictionary by iterating through the string
- Find the key with the highest value using `max()` with a `key=` argument
- Handle ties — define clearly which character wins (first encountered)

**Example:**
```
Input:  "programming"
Output: 'g'  (appears 2 times)
```

**What the test cases cover:**
- A string with one clear most-frequent character
- A string where multiple characters tie for frequency
- A single-character string
- A string with all unique characters
- Spaces and special characters included in the count

---

### `2_string_to_tuple_list.py` — String to Tuple List

**Problem:** Convert a string into a list of tuples, where each tuple pairs a character with its index position.

**Approach:**
- Use `enumerate()` to iterate with index and character together
- Build the list of `(index, character)` tuples using a list comprehension
- Return the complete list

**Example:**
```
Input:  "python"
Output: [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
```

**What the test cases cover:**
- A regular word — verifies index-character pairing is correct
- An empty string — confirms an empty list is returned
- A string with spaces — spaces are included as characters with their own index
- A single-character string — output is a list with one tuple
- A string with repeated characters — each occurrence gets its own tuple with a unique index

---

### `3_swap_tuple_elements.py` — Swap Tuple Elements

**Problem:** Given a list of two-element tuples, swap the elements inside each tuple — first becomes second, second becomes first.

**Approach:**
- Iterate over the list of tuples
- Unpack each tuple and repack in reverse order
- Return a new list of swapped tuples using a list comprehension

**Example:**
```
Input:  [(1, 'a'), (2, 'b'), (3, 'c')]
Output: [('a', 1), ('b', 2), ('c', 3)]
```

**What the test cases cover:**
- A standard list of `(int, str)` tuples — the typical case
- Tuples containing two integers
- Tuples where both elements are already the same type
- A list with a single tuple
- An empty list — confirms an empty list is returned without errors

---

### `4_anagram_pairs.py` — Anagram Pairs

**Problem:** Given two strings, determine whether they are anagrams of each other — meaning they contain exactly the same characters in the same frequencies, just in a different order.

**Approach:**
- Normalise both strings (strip whitespace, convert to lowercase)
- Sort both strings and compare — two anagrams will always sort to the same sequence
- Return `True` if they match, `False` otherwise

**Example:**
```
Input:  "listen"  ,  "silent"
Output: True

Input:  "hello"   ,  "world"
Output: False
```

**What the test cases cover:**
- A classic anagram pair (`"listen"` / `"silent"`)
- Two strings that are not anagrams
- Same string compared to itself — always `True`
- Mixed case — `"Listen"` and `"Silent"` should still return `True`
- Strings with spaces — normalisation handles them before comparison
- Different length strings — immediately `False`
- Single character strings, both matching and non-matching

---

## 🧪 Test Case Structure

Every file follows the same pattern — the function is defined first, then a block of test cases runs at the bottom:

```python
def solve(input):
    # clean solution here
    pass


# ── Test Cases ──────────────────────────────────────────
if __name__ == "__main__":
    print(solve("hello"))          # Expected: ...
    print(solve(""))               # Expected: ...
    print(solve("programming"))    # Expected: ...
```

Running the file directly executes all test cases and prints the results so you can verify the output at a glance. No testing framework needed — just run the file.

---

## 🚀 How to Run

```bash
cd 6_problem_solving

python 0_common_characters.py
python 1_most_frequent_char.py
python 2_string_to_tuple_list.py
python 3_swap_tuple_elements.py
python 4_anagram_pairs.py
```

Each file prints its test case results to the terminal immediately.

---

## 💡 Key Takeaways from This Module

- **Functions make solutions reusable and testable** — wrapping logic in a function means you can verify it against many inputs without rewriting anything
- **Test cases are not optional** — they're what separate a solution that *seems* to work from one that *actually* works
- **Sets are perfect for membership problems** — common characters, unique elements, and presence checks are all faster and cleaner with sets than loops
- **`enumerate()` is the clean way to track index and value together** — no need for a manual counter variable
- **Sorting is a reliable anagram check** — `sorted(s1) == sorted(s2)` is simple, readable, and correct
- **Always normalise input before comparing strings** — lowercase and strip before doing any character-level work

---

## 🏁 You've Reached the End

This is the final module of `python-basics`. By this point you've covered:

| Module | What You Learned |
|---|---|
| `0_basics` | Variables, types, input, arithmetic |
| `1_flow_control` | Conditionals and loops |
| `2_data_structures` | Lists, tuples, dicts, strings |
| `3_functions` | Functions, parameters, lambdas |
| `5_file_handling` | Reading, writing, JSON |
| `5_oops` | Classes, inheritance, encapsulation, polymorphism |
| `6_problem_solving` | Algorithmic thinking with functions and tests |

The next step is building bigger projects, exploring Python's standard library deeper, or picking up a domain — web development with Django/Flask, data science with Pandas, or automation with scripts. The foundation is solid. Keep building.
