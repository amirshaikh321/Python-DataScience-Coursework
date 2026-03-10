"""
List methods ->

    - append() -> add data at the end of list
    - extend() -> extend the list by given object

"""
l1 = [1,2,3,4,5]
l2 = [11,22,33]

l1.append(l2) # append the list means add the object at the last index of the list
print(l1)

l1 = [1,2,3,4,5]
l2 = ["a","b","c"]
l1.extend(l2)# join the l2 list at the end of the l1 
print(l1)

l1 = [1,2,3,4,5]
l1.insert(2,l2)# insert the object at given index
print(l1)

l1.remove(3) # delete the given element 
print(l1)

l1.pop(2) # delete the element of the given index also return deleted value
print(l1)

passed = ["sunil","karan","faizal","abhi"]
failed = ["janvi","sai","kumar","john"]
passed.append(failed.pop(3))
print(passed)
print(failed) 

l1 = [1,2,3,4,5]
del l1[1]
print(l1)

l2 = [5,4,3,2,1]
del l2[1:3]
print(l2)

students = ['ramesh','sujay','tushar','amar','pranav','atul','kunal','ajay','ravi']

print(students[2])
print(students[3:-3])
students.append("amir")
students.insert(2,"vijay")
students.remove('kunal')
print(students)


nums = [10,20,30,[11,22,44,55,[1,2,3,4,5],66,77],40,50,60,70]
nums.append(20)
nums.remove (20)
print(nums)
print("hello"+"world")