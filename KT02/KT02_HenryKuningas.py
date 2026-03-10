class PhoneBook:
    def __init__(self, filename='phonebook.txt'):
        self.filename = filename
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, number = line.strip().split(',')
                    self.contacts[name] = number
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for name, number in self.contacts.items():
                file.write(f"{name},{number}\n")

    def add_contact(self, name, phone_number):
        if name in self.contacts:
            print(f"Contact '{name}' already exists with the number: {self.contacts[name]}")
        else:
            self.contacts[name] = phone_number
            self.save_contacts()
            print(f"Contact '{name}' added with number: {phone_number}")

    def get_number_by_name(self, name):
        return self.contacts.get(name)

    def get_name_by_number(self, phone_number):
        for name, number in self.contacts.items():
            if number == phone_number:
                return name
        return None

    def display_contacts(self):
        if not self.contacts:
            print("Phone book is empty.")
        else:
            for name, number in self.contacts.items():
                print(f"{name}: {number}")


if __name__ == "__main__":
    phone_book = PhoneBook()

    # 1. Add a contact
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    phone_book.add_contact(name, phone_number)

    # 2. Find a number by name
    name_to_find = input("Enter name to find number: ")
    number = phone_book.get_number_by_name(name_to_find)
    if number:
        print(f"The number for '{name_to_find}' is: {number}")
    else:
        print(f"No contact found for '{name_to_find}'. Would you like to add it? (yes/no)")
        if input().lower() == 'yes':
            new_number = input("Enter the new phone number: ")
            phone_book.add_contact(name_to_find, new_number)

    # 3. Find a name by number
    number_to_find = input("Enter number to find name: ")
    name = phone_book.get_name_by_number(number_to_find)
    if name:
        print(f"The name for number '{number_to_find}' is: {name}")
    else:
        print(f"No contact found for number '{number_to_find}'. Would you like to add it? (yes/no)")
        if input().lower() == 'yes':
            new_name = input("Enter the new name: ")
            phone_book.add_contact(new_name, number_to_find)

    # 4. Display all contacts
    print("\nAll Contacts:")
    phone_book.display_contacts()
