"""
for loop :
for loop is a iterative statement in python it is used to iterate all elements from an iterable (list,tuple,dictionary,set,frozenset). 

syntax:-
    for var in iterable:
        #body
        #code operation

range :
range is datatype in python which generate the sequence of whole numbers.

syntax:
    range(start,end,step) 

"""

t = (1,2,3,4,5,6,7,8,9,10)

for var in t:
    print(var)
    print('hello')
print('--'*50)
square =[]
for var in t:
    sq = var**2
    square.append(sq)
print(square)

print('--'*50)
str= "Python"
for i in str:
    print(i)
print('--'*50)
set= {'java','python','c','R'}
for i in set:
    print(i)
print('--'*50)

dict = {'name':'Amir','age':21,'roll_no':203}
for key in dict:
    print(dict[key])

print('--'*50)

for val in dict.values():
    print(val)
print('--'*50)
for item in dict.items():
    print(item)

for i,j in dict.items():
    print(i,j)
print('--'*50)
for i in range(1,20):
    print(i)

print('--'*50)

for i in range(11,21,2):
    print(i)

print('--'*50)

for i in range(30,20,-1):
    print(i)
print('--'*50)

list =[]
for i in range(50,101):
    list.append(i)
print(list)

print('--'*50)
dict = {}
for i in range(11,21):
    sq =i**2
    dict[i]=sq
print(dict)

print('--'*50)

product = {
    'laptop': 60000,
    'mobile':30000,
    'bag':10000,
    'fan':10000
}
dis = 10/100
for i,j in product.items():
    dis_pr = j*dis
    sp = j-dis_pr
    print(f'selling price of {i}: {sp}')
