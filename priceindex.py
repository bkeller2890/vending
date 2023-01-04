items = {
    "A": 1.50,
    "B": 2.00,
    "C": 1.00,
    "D": 0.75
}

while True:
    selection = input("Please make a selection: ")
    if selection in items:
        price = items[selection]
        print(f"You selected item {selection}, which costs ${price:.2f}")
        break
    else:
        print("Sorry, that item is not available or is not a valid selection.")
