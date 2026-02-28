# Task 7: Mobile Recharge Bill

# A telecom company wants to calculate recharge bill.

# Details:

# Customer Name

# Recharge Amount

# Rules:

# GST = 18% of Recharge Amount

# Final Bill = Recharge Amount + GST

# Task:

# Write a Python program to:

# Accept details

# Calculate GST and final bill

# Display bill using string formatting

print("*"*7," Mobile Recharge Bill system ","*"*7)

name = input("Enter your Name: ")
recharge_amount = int(input("Recharge amount: "))
gst = recharge_amount*18/100
Total_amount = recharge_amount + gst
print(f"\n{name} you have to pay {Total_amount}")