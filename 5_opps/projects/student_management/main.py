# Define the Student Class
class Student:
    def __init__(self, name, roll_no, grades):
        # Initialize student name, roll number, and grades (dict)
        self.name = name
        self.roll_no = roll_no
        self.grades = grades  # already a dictionary from input

    def display_info(self):
        # Display student's full information
        print(f'Student Details:')
        print(f'Name: {self.name}')
        print(f'Roll No: {self.roll_no}')
        for subject, grade in self.grades.items():
            print(f'Subject: {subject} | Grade: {grade}')

    def calculate_average(self):
        if self.grades:
            total = sum(self.grades.values())
            average = total / len(self.grades)
            return average
        else:
            return 0.0


# Define the StudentManager Class (Core Logic)
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print(f"Student '{student.name}' removed.")
                return
        print(f"No student with roll no {roll_no} found.")

    def update_grades(self, roll_no, subject, grade):
        for student in self.students:
            if student.roll_no == roll_no:
                student.grades[subject] = grade
                print(f"Grade updated for subject '{subject}'.")
                return
        print(f"No student with roll no {roll_no} found.")

    def display_all_students(self):
        if not self.students:
            print("No students to display.")
            return
        print("All Student Details:")
        for student in self.students:
            student.display_info()
            print('-' * 30)

    def search_by_roll(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display_info()
                return
        print(f"No student with roll no {roll_no} found.")

    # File Handling – Save/Load data to JSON
    def save_data(self, filename='students.json'):
        try:
            data = []
            for student in self.students:
                student_dict = {
                    "name": student.name,
                    "roll_no": student.roll_no,
                    "grades": student.grades
                }
                data.append(student_dict)
            with open(filename, 'w') as f:
                import json
                json.dump(data, f, indent=4)
            print("Data saved to students.json.")
        except Exception as e:
            print("Failed to save:", e)

    def load_data(self, filename='students.json'):
        try:
            import json
            with open(filename, 'r') as f:
                data = json.load(f)
                for std_dict in data:
                    student = Student(
                        std_dict['name'],
                        std_dict['roll_no'],
                        std_dict['grades']
                    )
                    self.students.append(student)
            print("Data loaded from students.json.")
        except FileNotFoundError:
            print("No saved file found. Starting fresh.")
        except Exception as e:
            print("Failed to load:", e)


# Command Line Interface (CLI)
def main():
    manager = StudentManager()
    manager.load_data()

    while True:
        print('''\n
        ===== Student Management System =====
        1. Add student
        2. Display all students
        3. Search by roll number
        4. Update grade
        5. Remove student
        6. Save and Exit
        ''')

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter Student Name: ")
            roll_no = int(input("Enter Roll Number: "))
            print("Enter Grades (e.g., Math:90,English:85): ")
            raw_grades = input(">> ")
            grades = {}
            try:
                for pair in raw_grades.split(','):
                    subject, mark = pair.split(':')
                    grades[subject.strip()] = int(mark.strip())
            except Exception:
                print("Invalid grade format. Try again.")
                continue
            manager.add_student(Student(name, roll_no, grades))

        elif choice == '2':
            manager.display_all_students()

        elif choice == '3':
            roll_no = int(input("Enter Roll Number: "))
            manager.search_by_roll(roll_no)

        elif choice == '4':
            roll_no = int(input("Enter Roll Number: "))
            subject = input("Enter Subject: ")
            grade = int(input("Enter Grade: "))
            manager.update_grades(roll_no, subject, grade)

        elif choice == '5':
            roll_no = int(input("Enter Roll Number to Remove: "))
            manager.remove_student(roll_no)

        elif choice == '6':
            manager.save_data()
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Entry Point
if __name__ == "__main__":
    main()
