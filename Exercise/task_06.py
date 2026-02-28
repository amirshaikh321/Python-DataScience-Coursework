# Task 6: Fuel Cost Calculator

# A person wants to calculate total fuel cost.

# Details:

# Person Name

# Fuel Quantity (in liters)

# Rules:

# Cost per liter = â‚¹105

# Total Cost = Quantity Ã— Cost per liter

# Task:

# Write a Python program to:

# Accept name and fuel quantity

# Calculate total fuel cost

# Display details using string formatting

print("*"*7," Fuel Cost Calculator ","*"*7)
cost = 105
print(f"\nFuel cost per liter : {cost}\n","-"*20)

name = input("Enter your Name: ")
quantity = int(input("Quantity of fuel: "))

Total_cost = quantity*cost
print(f"\n{name} your Total Fuel cost will {Total_cost}")