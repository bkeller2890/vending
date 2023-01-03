# Set the cost of the soda to $1.75
cost = 1.75

# Keep track of how much money has been inserted and stop when $1.75 or more has been inserted.
money_inserted = 0
while money_inserted < cost:
    amount = float(input("Please insert at least $1.75: "))
    money_inserted += amount
    print(f"Total amount inserted: ${money_inserted}")
print("Thank you for inserting the correct amount.")

# Check if the user has inserted enough money
if money_inserted >= cost:
  # Display a list of sodas
  print("Please choose a soda:")
  print("1. Coke")
  print("2. Sprite")
  print("3. Mountain Dew")

# Define the valid choices
choices = ["1", "2", "3"]

# Prompt the user for their choice
choice = input("Enter the number of the soda you would like: ")

# Keep asking the user for their choice until they enter a valid choice
while choice not in choices:
    print("Invalid choice. Please try again.")
    choice = input("Enter your choice (1, 2, or 3): ")

print("Thank you for entering a valid choice.")

# Give the user the chosen soda
if choice == "1":
  print("Here is your Coke.")
elif choice == "2":
  print("Here is your Sprite.")
elif choice == "3":
  print("Here is your Mountain Dew.")
  
# Calculate and give the user their change
change = money_inserted - cost
print(f"Your change is ${change:.2f}.")
# Constants for the different coin denominations
DOLLAR = 1.00
QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01

# Calculate the number of each coin to return
dollars = int(change / DOLLAR)
change = change - dollars * DOLLAR
quarters = int(change / QUARTER)
change = change - quarters * QUARTER
dimes = int(change / DIME)
change = change - dimes * DIME
nickels = int(change / NICKEL)
change = change - nickels * NICKEL
pennies = int(change / PENNY)

# Print the results
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")