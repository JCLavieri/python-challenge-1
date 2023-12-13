
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        }
    }
}

# Initialize an empty list to store customer's order
customer_order = []

# Function to print menu
def print_menu(menu):
    print("Please select an item by entering the corresponding number:")
    item_number = 1
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            if isinstance(price, dict):
                for sub_item, sub_price in price.items():
                    print(f"{item_number}. {item} - {sub_item}: ${sub_price:.2f}")
                    item_number += 1
            else:
                print(f"{item_number}. {item}: ${price:.2f}")
                item_number += 1

# Function to get item name and price from menu selection
def get_item_details(menu, selection):
    item_number = 1
    for category, items in menu.items():
        for item, price in items.items():
            if isinstance(price, dict):
                for sub_item, sub_price in price.items():
                    if item_number == selection:
                        return f"{item} - {sub_item}", sub_price
                    item_number += 1
            else:
                if item_number == selection:
                    return item, price
                item_number += 1
    return None, None

# Function to add order to list
def add_to_order(item_name, price, quantity):
    order_item = {
        "Item name": item_name,
        "Price": price,
        "Quantity": quantity
    }
    customer_order.append(order_item)

# Function to get the total number of items in the menu
def get_total_menu_items(menu):
    total = 0
    for category, items in menu.items():
        for item, price in items.items():
            if isinstance(price, dict):
                total += len(price)
            else:
                total += 1
    return total

# Function to display current order
def display_current_order(order):
    print("\nCurrent Order:")
    if not order:
        print("No items in the order.")
        return
    for item in order:
        item_name = item["Item name"]
        quantity = item["Quantity"]
        total_price = item["Price"] * quantity
        print(f"{item_name:25} - Quantity: {quantity} - Total: ${total_price:.2f}")
    total_order_price = sum(item["Price"] * item["Quantity"] for item in order)
    print(f"Total Order Price: ${total_order_price:.2f}")


# Main ordering loop
def main():
    while True:
        total_items = get_total_menu_items(menu)
        print_menu(menu)
        menu_selection = input("Please enter the number of your selection from the menu: ")

        # Input validation for menu selection
        if not menu_selection.isdigit() or not 1 <= int(menu_selection) <= total_items:
            print(f"Invalid selection. Please enter a number between 1 and {total_items}.")
            continue

        menu_selection = int(menu_selection)
        item_name, price = get_item_details(menu, menu_selection)
        if not item_name:
            print("Error: Invalid menu selection.")
            continue

        # Prompt for quantity
        while True:
            quantity_input = input(f"How many of {item_name} would you like? (Default is 1): ")
            if not quantity_input.isdigit() or int(quantity_input) < 1:
                print("Invalid quantity. Please enter a valid number.")
                continue
            break

        quantity = int(quantity_input) if quantity_input else 1

        # Add to order
        add_to_order(item_name, price, quantity)

        # Display current order
        display_current_order(customer_order)

        # Check if customer wants to keep ordering
        while True:
            keep_ordering = input("Would you like to add more items to your order? (Y/N): ").lower()
            if keep_ordering in ['y', 'n']:
                break
            print("Invalid input, please enter Y or N.")

        if keep_ordering == 'n':
            break

    # Print final receipt
    print("\nFinal Order Receipt:")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    for item in customer_order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        item_name_spaces = " " * (25 - len(item_name))
        price_str = f"${price:.2f}"
        price_spaces = " " * (7 - len(price_str))
        print(f"{item_name}{item_name_spaces}|{price_str}{price_spaces}| {quantity}")

    total_price = sum(item["Price"] * item["Quantity"] for item in customer_order)
    print(f"Total Price: ${total_price:.2f}")

if __name__ == "__main__":
    main()
