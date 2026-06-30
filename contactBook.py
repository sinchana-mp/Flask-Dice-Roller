contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")
        contacts[name] = number
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for name, number in contacts.items():
                print(name, ":", number)

    elif choice == "3":
        name = input("Enter Name to Search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")