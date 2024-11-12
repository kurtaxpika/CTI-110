# Example similar to P4HW1

# List of avaliable items (not needed in your homework)
avaliableItems = ["litter", "cat food", "feather", "collar", "toy", \
                   "litter box", "flea meds", "treat"]
# Get number of items to purchase
numItems = int(input("How many items will you purchase? "))


# Empty list to hold valid responses
cart = []

# Loop to get the items
for item in range(numItems):
    thisItem = input(F"Enter item #{item +1}: ")
    # Loop to ensure thisItem is in avaliableItems
    while thisItem not in avaliableItems:
        print(f"{thisItem} is not avaliable!")
        thisItem = input(F"Enter item #{item +1} again: ")
    # Add the valid item to the cart 
    cart.append(thisItem)

# Loop to print each item in the cart
print("Items we purchased are: ")
for product in cart:
    print(product)
