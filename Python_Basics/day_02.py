#WAP to calculate percentage of marks

math = 78
phy = 89
chem = 88
geo = 87
eng = 79 

percentage = (math + phy + chem + geo + eng)/5

print(percentage,"%")

#WAP of calculate total salary

basic_sal = 50000
Hra = basic_sal* (20/100)
Da = basic_sal * (10/100)
gross = basic_sal + Hra + Da
tax = gross * (8/100)
net_sal = gross - tax

print(f"Basic salary = {basic_sal}")
print(f"HRA = {Hra}")
print(f"Da = {Da}")
print(f"tax = {tax}")
print(f"Gross salary = {gross}")
print(f"Net salary = {net_sal}")


#WAP to calculate new sal after increment

old_sal = 50000
inc = old_sal * (8/100)

new = old_sal +inc
print("new salary will be :",new)

#WAP to cal discount percentage

mrp = 100
sp = 80

dis_price = mrp -sp
discount = (dis_price/mrp) *100
print(discount)