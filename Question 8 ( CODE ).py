# Contact Book Using Lists and Dictionaries

contacts = []

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} | {contact['phone']} | {contact['email']}")

def search_contact():
    name = input("Enter the name to search: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            return
    print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting contact book.")
        break
    else:
        print("Invalid choice.")


# output
# --- Contact Book ---
# 1. Add contact
# 2. View contacts
# 3. Search contact
# 4. Exit
# Enter choice: 1
# Enter contact name: tejesh
# Enter phone number: 8754629997
# Enter email address: tejesh@123gmail.com
# Contact added successfully.

# --- Contact Book ---
# 1. Add contact
# 2. View contacts
# 3. Search contact
# 4. Exit
# Enter choice: 