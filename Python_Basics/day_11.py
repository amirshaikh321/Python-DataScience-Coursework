""" String Example:

String is the collection of characters with in a single and double inverted comma

Indexing  -> 
 - Positive index -> starts from 0 and direction is left to right
 - Negative index -> starts from -1 and direction is right to left

Indexing is use to access single charcter from a string.
EX.
    name = "Karan"
    print(name[2]) -> r

Slicing ->
Slicing is use for access multiple characters from a string.

syntax: 
    var[start index : end index : step value]
"""

name = "Amir shiakh"
print(type(name)) # <class 'str'>

no = 100
print(type(no)) # <class 'int'>

print("\nIndexing -")
print("*"*30)

print(name[3])
print(name[-4])

institute = "The kiran academy"
print(institute[2])
print(institute[5])
print(institute[-4])
print(institute[-9])


print("\nSlicing -")
print("*"*30)
name = "pavankumar yadav"
print(institute[4:9])
print(name[0:5])
print(name[1:6:2])
print(name[-1:-5:-1])

language = "python programming language"
print(language[0:6])
print(language[7:17])
print(language[-8:])
print(language[-1:-9:-1])
print(language[7:])
print(language[5::-1])