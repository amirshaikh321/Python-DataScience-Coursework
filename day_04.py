# String Formating

n1= 10
n2 = 20
sum = n1 + n2
print('sum of',n1,'and',n2,'is',sum)
print('sum of %d and %d is %d '%(n1,n2,sum))


# Simple interest
p = 100000
r = 10
t = 3

simple_interest = p*(r/100)*t

compound = p*(1 +(r/100))**t
print("Simple Interest is %d and Compound interest is %d "%(simple_interest,compound))# %d -> Integer
print("Simple Interest is %.4f and Compound interest is %.2f "%(simple_interest,compound))# %f -> Float

name = "Amir"
city = "Pune"
age = 21
print('My name is %s and I am from %s'%(name,city))
print('My name is {} and I am from {}'.format(name,city))
print('My name is {1} and I am from {0}'.format(city,name))
print('My name is {nm} and I am from {ct}'.format(ct= city, nm = name))
print(f'my name is {name} and my age is {age}')