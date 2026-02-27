# Task 5: Area & Cost of Painting

# A house owner wants to calculate painting cost.

# Details:

# Owner Name

# Length of wall

# Breadth of wall

# Rules:

# Area = Length Ã— Breadth

# Painting cost per sq unit = â‚¹15

# Total Cost = Area Ã— Cost per unit

# Task:

# Write a Python program to:

# Accept details

# Calculate area and total cost

# Display output using string formatting

print("*"*7," Painting cost calculator ","*"*7)
cost = 15
print(f"\nPainting cost per sq unit : {cost}\n","-"*20)

name = input("Enter your Name: ")
length = int(input("Enter length of your wall: "))
width = int(input("Enter width of your wall: "))

area = length*width
Total_cost = area * cost
print(f"\n{name} your Total Painting cost will {Total_cost}")