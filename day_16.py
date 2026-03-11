numbers = [11,22,33,[10,[1,2,3,4,5,6],20,30,40,50,60],55,66,77]
print("\nlist methods:")
print("**"*50)
numbers.pop(-2)
print(numbers)
numbers[3].insert(4,44)
numbers.append(88)
del numbers[3][1][2]
numbers.insert(-3,44)
numbers.pop(-3)
numbers[3].append(70)
print(numbers)

l1= [1,6,26,8,4,84,44,11,0,44]
print(l1.count(44))
l2 = l1.copy()
print(l2)
print(l1.index(84))
l1.reverse()
print(l1)
l1.sort()
print(l1)

"""
Set ->
set is a comma seperated values within '{}'
- set is mutable
- set is unordered
- set is hetrogeneous collection of immutable elements only
syntax:
    var = {v1,v2,v3,...}
"""
print("\nSet:")
print('**'*50)
num = {1,2,3,4}
print(type(num))

s = {1,2,(3,"sam","raj",4.3),77.99,4+5j}
s.add('karan')
s2 ={1,2,3,5,6,4}
print(s)
print(s.union(s2))
s.discard(2)
print(s)
s.pop()
print(s)
s.remove(77.99)
print(s)

s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,10,11}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
s1.difference_update(s2)
print(s1,s2)
s1 = {1,2,3,4,5,6,7}
s2 = {5,6,7,8,9,10,11}
s1.intersection_update(s2)
print(s1,s2)
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
s1.symmetric_difference_update(s2)
print(s1)
print()