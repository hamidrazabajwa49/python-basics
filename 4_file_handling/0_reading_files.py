from pathlib import Path
current_dir = Path(__file__).parent
file_path = current_dir / "sample_data" / "sample.txt"


print("Reading Entire File\n")

# Using with statement (recommended - automatically closes file)
with open(file_path, "r") as file:
    content = file.read()
    print(content)




print("\nReading Line by Line\n")
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters





print("\nReading Lines into List\n")
with open(file_path, "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")





print("\nError Handling\n")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
