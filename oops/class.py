"""
Class:-
-------
-> class is a blueprint of creating object.
-> properties and operations
-> imaginary entity
-> memory not required

syntax:- 
    class class_name:
        # body 
        # attributes and methods

Object:-
--------
-> object is a instance of a class
-> object is a physical entity
-> require memory for execution

syntax:- 
    cls_name()

reference variable | object reference:
--------------------------------------


"""

# class member : 
#     def __new__(cls):
        
#         print("Hello")
#         return super().__new__(cls)
#     def __init__(self):
#         print("I am init method")

# m1 = member()

class Employee():
    def __init__(self):
        print("hi")
    def __new__(cls):
        print("Hello")
    
emp =Employee()
print(emp)

