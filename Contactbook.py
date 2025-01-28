def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contact(contacts):
    search_term = input("Enter name to search: ")
    if search_term in contacts:
        print(f"Found: {search_term}: {contacts[search_term]}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name_to_update = input("Enter the name of the contact to update: ")
    
    if name_to_update in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name_to_update] = new_phone
        print(f"Contact '{name_to_update}' updated successfully!")
    else:
        print(f"No contact found with the name '{name_to_update}'.")

def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ")
    
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"Contact '{name_to_delete}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name_to_delete}'.")

def main():
    contacts = {}

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option! Please choose a valid option.")

# Run the application
if __name__ == "__main__":
    main()
