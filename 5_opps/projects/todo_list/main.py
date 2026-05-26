# Task Class
class Task:
    def __init__(self, title, description, due_date):
        # Initialize task title, description, due date, and status (default: not completed)
        self.title=title
        self.description=description
        self.due_date=due_date
        self.is_completed=False

    def toggle_status(self):
        # Toggle between completed and not completed
        self.is_completed= not self.is_completed

    def display(self):
        # Print task details: title, description, due date, status
        print("Task Details:")
        print(f'Title:{self.title}')
        print(f'Description:{self.description}')
        print(f'Due Date:{self.due_date}')
        print(f'Status:{self.is_completed}')

# TaskManager Class
class TaskManager:
    def __init__(self):
        # Initialize a list to store tasks
        self.tasks=[]

    def add_task(self, task):
        # Add a Task object to the list
        self.tasks.append(task)

    def remove_task(self, title):
        # Remove a task based on title
        try:
            for task in self.tasks:
                if task.title.lower()==title.lower():
                    self.tasks.remove(task)
                    return
            print("Task not found.....")
        except ValueError:
            print("Invalid Title.")    

    def update_task(self, title, new_title=None, new_desc=None, new_date=None):
        # Update title, description, and/or due date of a task
        try:
            for task in self.tasks:
                if task.title.lower()==title.lower():
                    if new_title is not None:
                        task.title=new_title
                    if new_desc is not None:
                        task.description=new_desc
                    if new_date is not None:
                        task.due_date=new_date
                # What if I want to display changes?
                return
            print(f'{title} not found.')
        except ValueError:
            print("Invalid Input.")

    def toggle_task_status(self, title):
        # Toggle status of a specific task
        try:
            for task in self.tasks:
                if task.title.lower()==title.lower():
                    task.is_completed=not task.is_completed
                return
            print(f'{title} not found')
        except ValueError:
                print("Inavlid Input.")


    def view_all_tasks(self):
        # Display all tasks in the list
        for task in self.tasks:
            print("Task Detail:")
            print(f'Title:{task.title}')
            print(f'Description:{task.description}')
            print(f'Due Date:{task.due_date}')
            print(f"{task}'s Status:{task.status}")
            return
        print("No Tasks....")

    def search_task(self, title):
        # Search and display a task by title
        try:
            for task in self.tasks:
                if task.title.lower()==title.lower():
                    print("Task Detail:")
                    print(f'Title:{task.title}')
                    print(f'Description:{task.description}')
                    print(f'Due Date:{task.due_date}')
                    print(f"{task}'s Status:{task.status}")
                    return
            print(f'No task with title:{title} found.')
        except ValueError:
            print("Invalid Input.")


# JSON File Handling Functions
import json

def save_tasks_to_file(manager, filename):
    # Convert tasks to dicts and save to a JSON file
    pass


def load_tasks_from_file(manager, filename):
    # Load tasks from JSON file and recreate Task objects
    pass


# CLI (Command-Line Interface)
def main():
    # Create TaskManager instance
    tk=TaskManager()
    # Load tasks from JSON file
    tk.load_data()

    # While loop to show CLI menu and take user input:
    while True:
        print(''' 
    1. Add Task
    2. View All Tasks
    3. Search Task
    4. Update Task
    5. Remove Task
    6. Toggle Task Status
    7. Save and Exit\n
    ''')
    
    choice=input("Enter Operation: ")
    # task title, description, due date, and status (default: not completed)
    if choice=='1':
        title=input("Enter task's title: ")
        description=input(f"Enter description: ")
        due_date=input("Enter Date(DD/MM/YYYY): ")
        tk(Task(title,description,due_date))


# Entry Point
if __name__ == "__main__":
    # Call main() function
    pass
