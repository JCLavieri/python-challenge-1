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
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize order list
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Continuous loop for ordering
while True:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")
    
    # Check if the customer's input is a number
    if not menu_category.isdigit():
        print("You didn't select a number.")
        continue

    # Convert the menu category to an integer
    menu_category = int(menu_category)

    # Check if the customer's input is a valid option
    if menu_category not in menu_items:
        print(f"{menu_category} was not a menu option.")
        continue

    # Save the menu category name to a variable
    menu_category_name = menu_items[menu_category]
    print(f"You selected {menu_category_name}")

    # Print out the options for the selected menu category
    i = 1
    menu_items = {}
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    for key, value in menu[menu_category_name].items():
        if isinstance(value, dict):  # Check if the value is another dictionary
            for sub_key, sub_value in value.items():
                print(f"{i}      | {key} - {sub_key}".ljust(30) + f" | ${sub_value}")
                menu_items[i] = (f"{key} - {sub_key}", sub_value)
                i += 1
        else:
            print(f"{i}      | {key}".ljust(30) + f" | ${value}")
            menu_items[i] = (key, value)
            i += 1

    # Ask customer for their menu item selection
    menu_selection = input("Please enter the item number you would like to order: ")

    # Check if menu_selection is a number, otherwise print an error
    if not menu_selection.isdigit():
        print("You didn't select a number.")
        continue

    # Convert the menu_selection to an integer
    menu_selection = int(menu_selection)

    # Check if the selection is in menu_items
    if menu_selection not in menu_items:
        print("That item was not a menu option.")
        continue

    # Extract item name and price from menu_items
    item_name, item_price = menu_items[menu_selection]

    # Prompt the customer for quantity
    quantity = input(f"How many of '{item_name}' would you like to order? ")
    
    # Default quantity to 1 if input is not a number
    if not quantity.isdigit():
        print("Invalid quantity. Setting quantity to 1.")
        quantity =
