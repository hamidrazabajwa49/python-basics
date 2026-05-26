import json
from getpass import getpass


# Class to store individual credentials
class Credential:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'site': self.site,
            'username': self.username,
            'password': self.password
        }

# Main class to manage credentials
class PasswordManager:
    def __init__(self):
        self.credentials = []

    def add_credential(self):
        site = input("Enter site: ")
        username = input("Enter username: ")
        password = getpass("Enter password: ")
        self.credentials.append(Credential(site, username, password))
        print("Credential added.")

    def get_credential(self):
        site = input("Enter site to retrieve: ")
        for credit in self.credentials:
            if credit.site.lower() == site.lower():
                print(f"\nSite: {credit.site}")
                print(f"Username: {credit.username}")
                print(f"Password: {credit.password}")
                return
        print("Credential not found.")

    def update_credential(self):
        username = input("Enter username to update: ")
        for credit in self.credentials:
            if credit.username.lower() == username.lower():
                print("Updating credentials.......")
                credit.site = input("Enter new site: ")
                credit.username = input("Enter new username: ")
                credit.password = getpass("Enter new password: ")
                print("Credential updated.")
                return
        print("Credential not found.")

    def delete_credential(self):
        site = input("Enter site to delete: ")
        for credit in self.credentials:
            if credit.site.lower() == site.lower():
                self.credentials.remove(credit)
                print("Credential deleted.")
                return
        print("Credential not found.")

    def save_to_file(self, filename='credentials.json'):
        data = [cred.to_dict() for cred in self.credentials]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to file.")

    def load_from_file(self, filename='credentials.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.credentials = [Credential(**cred) for cred in data]
            print("Data loaded from file.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")

# Main program loop
def main():
    manager = PasswordManager()
    manager.load_from_file()

    while True:
        print("\n ---- Password Manager ----")
        print("1. Add New Credential")
        print("2. View Credential")
        print("3. Update Credential")
        print("4. Delete Credential")
        print("5. Save & Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            manager.add_credential()
        elif choice == '2':
            manager.get_credential()
        elif choice == '3':
            manager.update_credential()
        elif choice == '4':
            manager.delete_credential()
        elif choice == '5':
            manager.save_to_file()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
