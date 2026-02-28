# Task 8: Online Food Order Bill

# A food app wants to generate bill.

# Details:

# Customer Name

# Food Item Price

# Rules:

# Delivery Charge = â‚¹40

# GST = 5% of Food Price

# Total Bill = Price + GST + Delivery Charge

# Task:

# Write a Python program to:

# Accept details

# Calculate GST and total bill

# Display bill using string formatting

print("*"*7," Online Food Order Bill ","*"*7)

name = input("Enter your Name: ")
recharge_amount = int(input("Recharge amount: "))
delivery_charge = 40
gst = recharge_amount*18/100
Total_amount = recharge_amount + gst
print(f"\n{name} you have to pay {Total_amount}")
