# Show welcome banner
def print_welcome_text():
    print("""\033[1;36m\
╭──────────────────────────────────────╮
│                                      │
│  Welcome to VendingMachineSystem.py  │
│                                      │
╰──────────────────────────────────────╯""")

# Define vending machine items
ITEMS = {
    "mw": {
        "index": 1,
        "name": "Mineral Water",
        "stock": 25,
        "price": 1.10
    },
    "cb": {
        "index": 2,
        "name": "Chocolate Bar",
        "stock": 40,
        "price": 10.10
    },
    "fm": {
        "index": 3,
        "name": "Mee Goreng",
        "stock": 25,
        "price": 7.50
    },
    "r": {
        "index": 4,
        "name": "Nasi",
        "stock": 40,
        "price": 6.00
    }
}

# Display available items
def print_available_items():
    print("\033[1;32;4mAvailable items:\033[0m")
    for item_id, item_info in ITEMS.items():
        print(f"• \033[1m{item_info['name']} \033[1;31m[{item_info['index']}]\033[0m\n  : \033[3mRM {item_info['price']}0\033[0m")
    si = input("\nPlease select \033[1;4man\033[0m item you want to buy: ")
    if si not in ["1", "2", "3", "4"]:
        si = None
        print("\033[1;31m>> Invalid selection. Please try again.\033[0m")
        print_available_items()
    return si

print_welcome_text()
print_available_items()