#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

#Sample Order Data:

def format_orders(orders):    
    formatted_orders = []

    for order in orders:
        name, item, quantity = order
        name_cell = 16 - len(name)
        item_cell = 16 - len(item)
        quant_cell = 16 - len(str(quantity))
        formatted = "|" + (" " * name_cell) + f"{name}|" + (" " * item_cell) + f"{item}|" + (" " * quant_cell) + str(quantity) + "|"
        formatted_orders.append(formatted)
    
    return formatted_orders


def print_orders(orders):
    print("\033[7m|Orderer Name    |Item Ordered    |Quantity Ordered|\033[0m\033[4m")
    
    formatted = format_orders(orders)
    
    for order in formatted:
        print(order)
    print("\033[0m")


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Keyboard", 4),
    ("Danny", "USB Drive", 16),
    ("Evelyn", "Mouse", 1),
    ("Francine", "Tablet", 3),
    ("Gerald", "Desktop", 1),
]
print_orders(orders)
