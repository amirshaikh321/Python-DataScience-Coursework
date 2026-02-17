from math import sqrt

#WAP to find area of rectangle
length = 34
width = 13
area = length * width
print(area)

#WAP to find the diagonal
diagonal = (length*length)+ (width*width)
print(sqrt(diagonal))

#WAP calculate simple impression & compound impression
p = 100000
r = 10
t = 3
# n =12

simple_interest = p*(r/100)*t
print(simple_interest)

compound = p*(1 +(r/100))**t
print(compound)