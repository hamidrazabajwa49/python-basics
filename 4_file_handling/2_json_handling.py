import json
from pathlib import Path


CURRENT_DIR = Path(__file__).parent
DATA_DIR = CURRENT_DIR / "sample_data"

def ensure_data_dir() -> None:
    """Create sample_data directory if it does not exist."""
    DATA_DIR.mkdir(exist_ok=True)

def write_json(data, filename: str, indent: int = 2) -> None:
    """Write Python object to a JSON file inside sample_data."""
    ensure_data_dir()
    file_path = DATA_DIR / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
    print(f"Written to {file_path}")

def read_json(filename: str):
    """Read and return JSON data from a file inside sample_data."""
    file_path = DATA_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def json_string_examples() -> None:
    """Demonstrate dumps and loads."""
    person = {"name": "Sara", "age": 25}
    json_string = json.dumps(person, indent=2)
    print(f"JSON string:\n{json_string}")

    json_data = '{"name": "Ahmed", "age": 30}'
    python_dict = json.loads(json_data)
    print(f"Python dict: {python_dict}")

def demo_student() -> None:
    """Write and read a student record."""
    student = {
        "name": "Ali",
        "age": 22,
        "courses": ["Python", "Data Science", "Web Development"],
        "grades": {"Python": 95, "Data Science": 88}
    }
    write_json(student, "student.json")
    loaded = read_json("student.json")
    print(f"Loaded student: {loaded['name']}, age {loaded['age']}")

def demo_config() -> None:
    """Write and read application configuration."""
    config = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "settings": {
            "theme": "dark",
            "language": "en",
            "auto_save": True
        }
    }
    write_json(config, "config.json")
    loaded_config = read_json("config.json")
    print(f"App: {loaded_config['app_name']}, Theme: {loaded_config['settings']['theme']}")

def demo_user_db() -> None:
    """Write and read a list of users."""
    users = [
        {"id": 1, "name": "Ali", "email": "ali@example.com"},
        {"id": 2, "name": "Sara", "email": "sara@example.com"},
        {"id": 3, "name": "Ahmed", "email": "ahmed@example.com"}
    ]
    write_json(users, "users.json")
    loaded_users = read_json("users.json")
    for user in loaded_users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")

def main() -> None:
    """Run all demonstrations."""
    print("=== Writing JSON ===\n")
    demo_student()

    print("\n=== Reading JSON ===\n")
    # Already shown inside demo_student, but explicit:
    loaded = read_json("student.json")
    print(f"Name: {loaded['name']}, Age: {loaded['age']}, Courses: {loaded['courses']}")

    print("\n=== JSON String Conversion ===\n")
    json_string_examples()

    print("\n=== Configuration File ===\n")
    demo_config()

    print("\n=== User Database ===\n")
    demo_user_db()

if __name__ == "__main__":
    main()
