"""
String methods:
    - isalpha() -> true if string contain alphabets only
    - isnumeric() -> true if string contain numbers only
    - isalnum() -> true if string contain alphabets and number 
    - isupper() -> true if string is caplital
    - islower() -> true if string is in lower case
    - istitle() -> true if string is in title format
    - isspace() -> return true if the string contain only space
    - replace() -> replace the given character with the the another character
    - index() -> index method find the index of the given element
    - count() -> this method count the no of times given element found in string
"""

name = "Amir Shaikh"
password = "321"

print("isalpha(): ",password.isalpha())
print("isalpha(): ",name.isalpha())
print("isnumeric(): ",password.isnumeric())

name = "Amir321"
print("isalnum(): ",name.isalnum())
name = "amir"
print("isalnum(): ",name.isalnum())
name = "12453"
print("isalnum()",name.isalnum())

name = "AMIR"
print("isupper(): ",name.isupper())
print("islower(): ",name.islower())
print("istitle(): ",name.istitle())

name = "  "
print("isspace(): ",name.isspace())

institute = "The Keeran Academy"
print("isreplace(): ",institute.replace("ee", "i"))
print("index(): ",institute.index('e',4))

print("count(): ",institute.count("e")) 
print(institute.startswith("T"))
print(institute.endswith("y"))
print(institute.center(50,"*"))