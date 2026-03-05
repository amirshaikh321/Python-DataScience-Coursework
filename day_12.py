"""
Indexing and Slicing example

String methods ->
    lower() -> this method convert string into lower case
    upper() -> this method convert string into upper case
    title() -> this method convert each word's first character of string into capital 
"""
print("\nString Slicing")
print("--"*10)
name = "Sham"
# indexing 
print(name[1])
print(name[3])

# slicing
print(name[0:2])
print(name[-1::-1])

# start index -> forward index = 0, reverse index =-1

print(name[:3:1])
print(name[::-1])

institute  = "the kiran academy"

print(institute[:])
print(institute[:3])
print(institute[4:-8])
print(institute[-7:])
print(institute[2::-1])

# String methods

institute = "the kiran academy"
print("\nString methods")
print("--"*10)
institute = institute.upper()
print("Upper case: ",institute)
print("lower case: ",institute.lower())
print("Title form: ",institute.title())
print("capitalize ",institute.capitalize())