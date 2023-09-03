# Creating an empty dictionary to store contact information
contacts = {}

while True:
    print("\n ----- MENU ----- \n")
    print("1. Add a contact")
    print("2. Update a contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. List all contacts")
    print("6. Exit \n")
    
    choice = input("What you want to do?\nEnter Your Choice: ")
    
    if choice == "1":
        name = input("Enter the name of the contact: ")
        phone = input("Enter the phone number: ")
        if len(phone) != 11:
            print("Invalid phone number. Please enter exactly 11 digits.")
        else:
            contacts[name] = phone
            print(f"{name} has been added to your contacts.")
    elif choice == "2":
        name = input("Enter the name of the contact to update: ")
        if name in contacts:
            phone = input("Enter the new phone number: ")
            if len(phone) != 11:
                print("Invalid phone number. Please enter exactly 11 digits.")
            else:
                contacts[name] = phone
                print(f"{name}'s phone number has been updated.")
        else:
            print(f"{name} is not in your contacts.")
    elif choice == "3":
        name = input("Enter the name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} has been deleted from your contacts.")
        else:
            print(f"{name} is not in your contacts.")
    elif choice == "4":
        name = input("Enter the name of the contact to search for: ")
        if name in contacts:
            phone = contacts[name]
            print(f"{name}'s phone number is {phone}")
        else:
            print(f"{name} is not in your contacts.")
    elif choice == "5":
        if not contacts:
            print("Your contacts list is empty.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "6":
        print("Goodbye!\nCreated By Qavi Shaikh")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")
