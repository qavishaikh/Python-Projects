# Grocery List Application

# Initialize an empty list to store grocery items
grocery_list = []

# Function to add an item to the grocery list
def add_item(item):
    grocery_list.append(item)
    print(f"Added '{item}' to your grocery list.")

# Function to view the grocery list
def view_list():
    if not grocery_list:
        print("Your grocery list is empty.")
    else:
        print("Grocery List:")
        for i, item in enumerate(grocery_list, 1):
            print(f"{i}. {item}")

# Function to remove an item from the grocery list
def remove_item(item_index):
    if 1 <= item_index <= len(grocery_list):
        removed_item = grocery_list.pop(item_index - 1)
        print(f"Removed '{removed_item}' from your grocery list.")
    else:
        print("Invalid item index!")

# Main program loop
while True:
    print("\nGrocery List Application")
    print("1. Add Item")
    print("2. View Grocery List")
    print("3. Remove Item")
    print("4. Quit")

    choice = input("\n Enter your choice: ")

    if choice == "1":
        item = input("Enter the item to add to your grocery list: ")
        add_item(item)
    elif choice == "2":
        view_list()
    elif choice == "3":
        item_index = int(input("Enter the item number to remove from your grocery list: "))
        remove_item(item_index)
    elif choice == "4":
        print("Good Bye.\n Created By Qavi Shaikh")
        break
    else:
        print("Invalid choice. Please select a valid option.")
