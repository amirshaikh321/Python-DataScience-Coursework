"""
If else revision:
Syntax ->
    if Condition:
        code which execute if cond is true
    
    else Condition:
        code which is default it execute if condition is false

elif ->
use when there are multiple conditions
Syntax:
    if con1:
        code
    elif con2:
        code
    elif con3:
        code
    else:
        code
"""

numbers =  [10,20,30,40,50,60,70]
for num in numbers:
    if num >= 40:
        print(num)


numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num%2 == 0:
        square = num**2
        print(f'The Square of {num} is {square}')
    else:
        cube = num**3
        print(f'The cube of {num} is {cube}')


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,33,53,]
l1 =[]
l2 =[]
l3 =[]
l4 =[]
for num in numbers:
    if num<=7:
        l1.append(num)
    elif num<=15:
        l2.append(num)
    elif num<=20:
        l3.append(num)
    else:
        l4.append(num)

print(f'List 1 : {l1} \nList 2 : {l2} \nList 3 : {l3} \nList 4 : {l4}')

student = ['vijay','kunal','arun','kiran','sujay','karan','veeru','ajay']

for name in student:
    if name[0] == 'k':
        print(name)
    
for name in student:
    if name[-3:] == 'jay':
        print(name)

print('--'*50)

student = {'vijay':78,'kunal':23,'arun':90,'kiran':66,'sujay':18,'karan':76,'veeru':71,'ajay':31}

for name,marks in student.items():
    if marks >40:
        print(f'{name} is pass with {marks} marks')

print()
print("--"*50)
pass_std = []
fail_std = []
for name,marks in student.items():
    if marks >40:
        pass_std.append(name)
    else:
        fail_std.append(name)
    
print("Pass Students :",pass_std)
print("Fail Students :",fail_std)

print()
print("--"*50)

numbers = [1,2,3,4,5,6,7,8,9,10]
square = {}
cube = {}
for num in numbers:
    if num%2 == 0:
        square[num] = num**2
    else:
        cube[num] = num **3
print("Dictionary of square of even numbers :",square)
print("Dictionary of cube of odd numbers :",cube)

print()
print("--"*50)
emp_sal = {'vijay':78000,'kunal':23000,'arun':90000,'kiran':66000,'sujay':18000,'karan':76000,'veeru':71000,'ajay':31000}
print("Salary before Increment: ",emp_sal)
for name, sal in emp_sal.items():
    if sal<50000:
        inc_sal = sal*15/100
        new_sal = sal + inc_sal
        emp_sal[name]=new_sal
    else:
        inc_sal = sal*10/100
        new_sal = sal + inc_sal
        emp_sal[name]=new_sal

print("Salary after Increment: ",emp_sal)


print()
print("--"*50)
marks = {'vijay':78,'kunal':23,'arun':90,'kiran':66,'sujay':18,'karan':76,'veeru':71,'ajay':31}
grade ={}
for name,mk in marks.items():
    if mk>=90:
        grade[name]='A+'
    elif mk>=80:
        grade[name]='A'
    elif mk>=70:
        grade[name]='B+'
    elif mk>=60:
        grade[name]='B'
    else:
        grade[name]='C'
print(grade)