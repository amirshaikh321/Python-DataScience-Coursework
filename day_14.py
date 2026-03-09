"""
Datatype -> List
    - Indexing

List -
list is a collection of data, list is mutable.
"""

list1 = [10,20,30,40,50]
print(list1)
print(type(list1))

list2 = [10,20,30,"list",23.6, "abc"] # store different datatype
print(list2)

list3 = [1,2,3,[41,53.5,763.55,[63,"spice"],3+6j],5,65] # nested list
print(list3)

print(list3[3])
print(list3[3][3])