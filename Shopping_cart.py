# This is sets practical
# This is example of shopping cart for example you can not add Duplicate Item in the cart

shopping_cart = set()

def add_item(item):
    shopping_cart.add(item)
    print(f"Added {item} to your cart.")

def remove_item(item):
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(f"Removed {item} from your cart.")
    else:
        print(f"{item} is not in your cart.")

def display_cart():
    if not shopping_cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item in shopping_cart:
            print(item)

while True:
    print("\nOptions:")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Display cart")
    print("4. Quit"+"\n")

    choice = input("Enter Number What you want to do: ")

    if choice == '1':
        item = input("Enter the item to add: "+"\n")
        add_item(item)
    elif choice == '2':
        item = input("Enter the item to remove: "+"\n")
        remove_item(item)
    elif choice == '3':
        display_cart()
    elif choice == '4':
        print("Thank you for shopping with us!","\n Created by Qavi Shaikh")
        break
    else:
        print("Invalid choice. Please select a valid option.")
