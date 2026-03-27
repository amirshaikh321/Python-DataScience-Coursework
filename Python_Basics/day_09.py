# Numeric data type

# data type is a classification that determines the kind of value a variable can store and the operations that can be performed on it.

# Datatypes ->
# int
# float 
# str
# complex
# bool

# dir is a predefine function which return the methods of the object
# type is a predefined function in python which returns the data type of the object

num =10
print(f"\nMethods of object: \n{dir(num)}\n \nData type of object : {type(num)}")
print("_"*50)

num1 = 11.4
print(f"\nMethods of object: \n{dir(num1)}\n \nData type of object : {type(num1)}")
print("_"*50)

complex_num = 556+67j
print(f"\nMethods of object: \n{dir(complex_num)}\n \nData type of object : {type(complex_num)}")
print("Real number in complex number -",complex_num.real)
print("Imaginary number in complex number -",complex_num.imag)

# Real part of the complex number can be int or float but the imaginary part of the complex number must be float and decimal
