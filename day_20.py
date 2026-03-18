"""
Tuple  : 

Tuple is Comma seperated values within ()
syntax :
    var = (v1,v2)

t = (11,22,33,44)
print(type(t)) #<class[tup]>

Tuple is ordered, immutable and hetrogeneous collection of data where duplicates are not allowed.
it support both packing and unpacking

"""
from sys import getsizeof

t = (11,22,33,44,55,66)

# Indexing -> 
print(t[-3])
# Slicing -> 
print(t[2:5:1])
# methods
print(t.count(11))
print(t.index(33))

t = 1,2,3
print(type(t))

x,y,z = t
print(x)
print(y)
print(z)

a=1
b=2
c =3
t = a,b,c
print(t)

# tuple require less memory as compare to list
tup = 1,2,3
l = [1,2,3]
print(getsizeof(t))
print(getsizeof(l))

"""
set :

empty set syntax ->
    set = set()

tuple with single value 
    tup = (1,)

frozenset ->
    f = frozenset({1,2,3})
    - it is unordered,it is hetrogeneous collection of immutable elements only
    - duplicates are not allowed

"""
set=set()
print(type(set))

f = frozenset({1,2,3,55,33})
print(type(f))
print(f)
l = frozenset({1,23,44,23,23,55,"afa"})
print(l)

l1 = l.copy()
print(l1)

print(l.difference(f))
print(l.intersection(f))
print(f.difference(l))
print(f.isdisjoint(l))
print(l.issubset(f))
print(l.issuperset(f))
print(l.symmetric_difference(f))
print(f.union(l))