# 📁 5 — File Handling

Real programs don't just run and forget — they save data, read configurations, log results, and exchange information with other systems. File handling is how your Python code interacts with the outside world beyond the terminal. This module covers reading from files, writing to them, and working with JSON — one of the most common data formats in modern software.

---

## 📂 Files in This Module

```
5_file_handling/
│
├── 0_reading_files.py
├── 1_writing_files.py
├── 2_json_handling.py
└── sample_data/          ← files created and modified by the code
```

---

## 📄 File Breakdown

### `0_reading_files.py` — Reading Files

Before you can process any file, you need to open and read it. This file covers every way Python lets you pull content out of a file — from reading it all at once to going line by line.

**Concepts covered:**
- Opening a file with `open()` and the importance of closing it
- Context managers — using `with open(...) as f:` (the right way)
- File modes: `"r"` for reading, `"rb"` for binary reading
- `read()` — reads the entire file as a single string
- `readline()` — reads one line at a time
- `readlines()` — reads all lines into a list
- Iterating over a file object directly with a `for` loop
- Handling the `FileNotFoundError` exception gracefully
- Reading from a specific path vs the current directory
- Stripping newline characters with `.strip()`

**Practical Examples:**
- **File content viewer** — opens a text file from `sample_data/` and prints its contents cleanly, stripping trailing whitespace from each line
- **Line counter** — reads a file and reports how many lines, words, and characters it contains — a mini version of the Unix `wc` command
- **Keyword scanner** — reads through a log file line by line and prints only the lines that contain a specific word (e.g., `"ERROR"` or `"WARNING"`)
- **CSV manual reader** — reads a `.csv` file without the `csv` module, splits each line on commas, and displays the data in a formatted table
- **Config file reader** — reads a simple key=value settings file from `sample_data/` and parses it into a dictionary for use in the program

---

### `1_writing_files.py` — Writing Files

Reading is half the story — writing is how your program leaves something behind. This file covers creating new files, overwriting existing ones, and appending without destroying what's already there.

**Concepts covered:**
- File modes: `"w"` (write/overwrite), `"a"` (append), `"x"` (create, fails if exists)
- Writing strings with `write()` — and why you need to add `\n` yourself
- Writing multiple lines at once with `writelines()`
- The difference between `"w"` and `"a"` — when each is appropriate
- Creating files that don't exist yet
- Writing to a specific path inside `sample_data/`
- Flushing and closing files properly with context managers

**Practical Examples:**
- **Note saver** — takes a string and writes it to a `.txt` file in `sample_data/`, creating the file if it doesn't exist and overwriting it if it does
- **Daily log appender** — appends a timestamped entry to a `log.txt` file in `sample_data/` each time it runs, without erasing previous entries
- **Student report writer** — takes a list of student names and scores, formats them, and writes a clean report to `sample_data/report.txt`
- **CSV file generator** — writes a list of dictionaries (e.g., product inventory) into a `.csv` file in `sample_data/` row by row
- **Backup creator** — reads an existing file from `sample_data/`, modifies its content, and writes the result to a new `_backup.txt` file alongside the original

---

### `2_json_handling.py` — JSON Handling

JSON (JavaScript Object Notation) is the universal language of data exchange — APIs, config files, databases, and web apps all speak it. Python's `json` module makes reading and writing it straightforward.

**Concepts covered:**
- What JSON is and how it maps to Python types (`dict` ↔ object, `list` ↔ array, `str`, `int`, `bool`, `None`)
- `json.dumps()` — converting a Python object to a JSON string
- `json.loads()` — parsing a JSON string back into a Python object
- `json.dump()` — writing JSON directly to a file
- `json.load()` — reading JSON directly from a file
- Pretty-printing with `indent=` parameter
- Sorting keys with `sort_keys=True`
- Handling `json.JSONDecodeError` when parsing invalid JSON

**Practical Examples:**
- **Contact book** — stores a list of contacts (name, phone, email) as a JSON file in `sample_data/contacts.json`; demonstrates saving a new contact and loading the full list back
- **Settings manager** — writes a program's configuration (theme, language, font size) to `sample_data/settings.json` and reads it back on the next run — simulating persistent app settings
- **API response simulator** — parses a hardcoded JSON string (mimicking a real API response) into a Python dictionary and extracts specific fields for display
- **Student data store** — reads `sample_data/students.json`, adds a new student entry, and writes the updated list back to the same file
- **JSON pretty printer** — takes a compact, hard-to-read JSON string and reformats it with proper indentation and sorted keys for human readability

---

## 📂 sample_data/

This folder holds all the files that the code in this module creates, reads from, or modifies. You don't need to create anything here manually — running the scripts generates the files automatically.

| File | Created by |
|---|---|
| `log.txt` | `1_writing_files.py` — appended to on each run |
| `report.txt` | `1_writing_files.py` — student report output |
| `contacts.json` | `2_json_handling.py` — contact book data |
| `settings.json` | `2_json_handling.py` — persistent app settings |
| `students.json` | `2_json_handling.py` — student records |

> **Note:** If `sample_data/` is empty when you clone the repo, just run the scripts — they will populate the folder automatically.

---

## 🚀 How to Run

```bash
cd 5_file_handling

python 0_reading_files.py
python 1_writing_files.py
python 2_json_handling.py
```

Run `1_writing_files.py` before `0_reading_files.py` if `sample_data/` is empty — the writer creates the files that the reader expects to find.

---

## 💡 Key Takeaways from This Module

- Always use `with open(...) as f:` — it closes the file automatically even if an error occurs
- `"w"` mode **erases** the existing file before writing — use `"a"` if you want to keep what's already there
- `json.dump()` writes to a **file**; `json.dumps()` returns a **string** — the `s` stands for string
- `json.load()` reads from a **file**; `json.loads()` parses a **string** — same rule
- Always wrap `json.loads()` in a `try/except json.JSONDecodeError` block when parsing data you didn't write yourself
- File paths are relative to where you run the script from — if something isn't found, check your working directory

---

## ➡️ What's Next

You can now read, write, and persist data. Next, learn how to model real-world problems using classes and objects:

**`6_oops/`** — Object-Oriented Programming in Python

```bash
cd ../6_oops
python 0_classes_objects.py
```
