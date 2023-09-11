# Inventory Management System

# Initialize an empty list to store inventory items
inventory = []

# Function to add an item to the inventory
def add_item(item_name, quantity, price):
    item = {
        "name": item_name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(item)
    print(f"Added '{item_name}' to the inventory.")

# Function to view all inventory items
def view_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}")

# Function to update an item in the inventory
def update_item(item_index, new_quantity, new_price):
    if 1 <= item_index <= len(inventory):
        item = inventory[item_index - 1]
        item["quantity"] = new_quantity
        item["price"] = new_price
        print(f"Updated '{item['name']}' in the inventory.")
    else:
        print("Invalid item index!")

# Function to delete an item from the inventory
def delete_item(item_index):
    if 1 <= item_index <= len(inventory):
        deleted_item = inventory.pop(item_index - 1)
        print(f"Deleted '{deleted_item['name']}' from the inventory.")
    else:
        print("Invalid item index!")

# Main program loop
while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Quit")

    choice = input("Enter your choice : ")

    if choice == "1":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        add_item(item_name, quantity, price)
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        item_index = int(input("Enter the item number to update: "))
        new_quantity = int(input("Enter the new quantity: "))
        new_price = float(input("Enter the new price: "))
        update_item(item_index, new_quantity, new_price)
    elif choice == "4":
        item_index = int(input("Enter the item number to delete: "))
        delete_item(item_index)
    elif choice == "5":
        print("Exiting the inventory management system. \n Created by Qavi Shaikh")
        break
    else:
        print("Invalid choice. Please select a valid option.")
