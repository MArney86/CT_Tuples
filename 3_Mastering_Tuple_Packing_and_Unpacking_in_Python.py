#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

#Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

#Sample Order Data:

def format_orders(orders): #function to format the give order list into a list of formatted strings for printing
    formatted_orders = [] #initialize list of formatted order strings to return from function 

    for order in orders: #iterate through the list of order tuples
        name, item, quantity = order #unpack the current order tuple into constituent parts
        name_cell = 16 - len(name) #figure out spacing for formatting
        item_cell = 16 - len(item) #figure out spacing for formatting
        quant_cell = 16 - len(str(quantity)) #figure out spacing for formatting
        formatted = "|" + (" " * name_cell) + f"{name}|" + (" " * item_cell) + f"{item}|" + (" " * quant_cell) + str(quantity) + "|" #build the formatted string for the order with left justified cells
        formatted_orders.append(formatted) #add formatted order string to list
    
    return formatted_orders #return the list of formatted strings


def print_orders(orders):
    print("\033[7m|Orderer Name    |Item Ordered    |Quantity Ordered|\033[0m\033[4m") #heading for formatted strings with inverted text then switch to underlined for orders using ANSI escape codes
    
    formatted = format_orders(orders) #store the formatted strings for the orders in our list
    
    for order in formatted: #iterate through the formatted string list
        print(order) #print the formatted string
    print("\033[0m") #ANSI escape code to return text to normal


orders = [ #list of order tuples to be formatted and print
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Keyboard", 4),
    ("Danny", "USB Drive", 16),
    ("Evelyn", "Mouse", 1),
    ("Francine", "Tablet", 3),
    ("Gerald", "Desktop", 1),
]

print_orders(orders) #calling the function to print the formatted orders from the orders list of tuples
