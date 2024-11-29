import re

# User Items
user_items = []

# Show welcome banner
def print_welcome_text():
    print("""\033[1;36m\
╭──────────────────────────────────────╮
│                                      │
│  Welcome to VendingMachineSystem.py  │
│                                      │
╰──────────────────────────────────────╯\033[0m""")

# Define vending machine items
items = {
    "0": {
        "index": 0,
        "name": "Mineral Water",
        # "stock": 25,
        "price": 1.10
    },
    "1": {
        "index": 1,
        "name": "Chocolate Bar",
        # "stock": 40,
        "price": 10.10
    },
    "2": {
        "index": 2,
        "name": "Mee Goreng",
        # "stock": 25,
        "price": 7.50
    },
    "3": {
        "index": 3,
        "name": "Nasi",
        # "stock": 40,
        "price": 6.00
    },
    "4": {
        "index": 4,
        "name": "Burger",
        # "stock": 20,
        "price": 7.00
    }
}

# Formats the array by joining commas
def format_array(ui_list):
    names = [items[item_id]["name"] for item_id in ui_list]
    return ", ".join(names)

# Display available items
def print_available_items():
    print("\033[1;32;4mAvailable items:\033[0m")
    for item_id, item_info in items.items():
        print(f"• \033[1m{item_info['name']} \033[1;94m[{item_info['index']}]\033[0m\n  : \033[3mRM {item_info['price']}0\033[0m")
    si = input("\n\033[31;3m[Step 1] Select \033[1;4man\033[0;31;3m item you want to buy from the list above.\n")

    selected_item = None
    for item_id, item_info in items.items():
        if str(item_info["index"]) == si:
            selected_item = item_id
            break

    if selected_item is None:
        print(f"\n\033[1;31m[!] \"{si}\" is an invalid selection. Please try again.\033[0m")
        print_available_items()
    else:
        user_items.append(si)
        get_user_confirmation()

# Gets the user's confirmation
def get_user_confirmation():
    confirmation = input(f"\033[31;3m[Step 2] Is the item you selected \033[1;4mcorrect\033[0;31m?\033[0m\n{format_array(user_items)}\n\033[92;1m[Yes]\033[0m or \033[91;1m[No]\033[0m:\n")
    if re.match("Yes", confirmation, re.IGNORECASE):
        get_user_retry_confirmation()
    elif re.match("No", confirmation, re.IGNORECASE):
        user_items.pop()
        print_available_items()
    else:
        print(f"\n\033[1;31m[!] \"{confirmation}\" is an invalid selection. Please try again.\033[0m")
        get_user_confirmation()

# Gets the user's retry confirmation
def get_user_retry_confirmation():
    retry_confirmation = input(f"\033[31;3m[Step 3] Are you finished with shopping?\nIf typed \"Yes\", you will be checked out with a receipt.\033[0m\n\033[92;1m[Yes]\033[31;0m or \033[91;1m[No]\033[0m:\n")
    if re.match("Yes", retry_confirmation, re.IGNORECASE):
        print("\n\033[3;4mThank you for shopping. Your receipt will be printed.\033[0m")
        print_receipt()
        exit()
    elif re.match("No", retry_confirmation, re.IGNORECASE):
        print_available_items()
    else:
        print(f"\n\033[1;31m[!] \"{retry_confirmation}\" is an invalid selection. Please try again.\033[0m")
        get_user_retry_confirmation()

# Prints the receipt
def print_receipt():
    print("\033[1;34mShopping Receipt:\033[0m")

    tp = 0
    for item_id in user_items:
        item = items[item_id]
        tp += item["price"]
        print(f"• {item['name']} - RM {item['price']}0")
    print("\033[1;33mTotal Price: RM {:.2f}\033[0m".format(tp))

print_welcome_text()
print_available_items()