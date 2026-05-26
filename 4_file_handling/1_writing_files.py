from pathlib import Path
current_dir = Path(__file__).parent
file_path = current_dir / "sample_data" / "sample.txt"


print("Writing to Files\n")

# 'w' mode - creates new file or overwrites existing
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")
    file.write("Writing multiple lines.\n")
print("File written successfully!")





print("\nAppending to Files\n")
# 'a' mode - adds to end of file without deleting existing content
with open(file_path, "a") as file:
    file.write("This line was appended.\n")
    file.write("Another appended line.\n")
print("Content appended!")





print("\nWriting Lists\n")
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]
with open(file_path, "w") as file:
    file.writelines(lines)
print("List written to file!")


# Practical Examples


# Creating Logs
print("\nCreating Log File\n")
from datetime import datetime
def log_message(message):
    """Append timestamped message to log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("User logged in")
log_message("Data processed successfully")

print("Log entries added!")
