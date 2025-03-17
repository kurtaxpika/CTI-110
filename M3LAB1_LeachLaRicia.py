# LaRicia Leach
# 03/13/2025
# M3LAB1
# Reading csv data into class obejects

import csv

# Make a class!
class Customer:
    # Create the __init__ function
    def __init__(self, first, last, phone, email, state, address):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.state = state
        self.address = address

    def display_info(self):
        return f"{self.first} {self.last}\n{self. phone}\n{self.email}\n{self.address},{self.state}"
    
# (not important)
#customer1 = Customer("Janice", "Miller", "704-555-4521", "jayjay@aol.com", "NC", "255 Hull Rd")
#print(customer1.display_info())

# Create empty list to hold csv info
customer_input = []

with open('customer.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        customer_input.append(row)

# print(customer_input)

# To do 
'''
iterate through the nested list. Ignore the first inner list.'
For each remaining list, create a Customer object from the list data.'
For those three Customer objects, call the display_info method on each one.

'''

# Create Customer 
customers = []

# Skip the first list and add it into the customer 
for row in customer_input[1:]:o
    customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5])
    customers.append(customer)

# Call and display info then print results
for customer in customers:
    print(customer.display_info())
    print("\n")
