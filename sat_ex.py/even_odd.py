
# 1. Even-odd Checker
# num = int(input('Enter Number: '))

# if num%2 ==0:
#     print("Number is even")
# else:
#     print("Number is odd")

#2. Positive, Negative or Zero

# num = int(input("Enter Number: "))
# if num >0:
#     print(f"{num} is Positive")
# elif num<0:
#     print(f"{num} is Negative")
# else:
#     print("number is Zero")

# 3. voting checker
# age = int(input("Enter your age: "))
# if age >=18:
#     print("You can vote")
# elif age <18:
#     print("You can't vote")

# 4. seperate even and odd numbers
# numbers = [1,3,4,5,6,7,8,12,34,56,78,45]
# even = []
# odd = []

# for i in numbers: 
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# 5. seperate the eligible for voting and not ligible for voting
# voter = {
#     'kunal':45,'kiran':23,'sujay': 67,'jay':11,'ishwar':14,'prakash':47,'rajesh':15}
# eligible =[]
# not_eligible = []

# for i in voter:
#     if voter[i]>=18:
#         eligible.append(i)
#     else:
#         not_eligible.append(i)

# print(f"eligible for voting: {eligible}")
# print(f"not eligible for voting: {not_eligible}")

# 6.
# num1= int(input('enter num1: '))
# num2= int(input('enter num2: '))

# if num1>num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num2} is greater than {num1}")

# 7.
# numbers = [10,40,50,30,77,55,1,90,3]
# greater =0
# for i in numbers:
#     if i >greater:
#         greater = i
# print(greater) 

# 8.
# numbers = [10,40,50,30,77,55,1,90,3]
# minimum =numbers[0]
# for i in numbers:
#     if i <minimum:
#         minimum = i
# print(minimum)

"""
Write a program to check the number is divisible by 4 and 7
"""
# num = int(input("Enter a number: "))

# if num%4==0 and num%7==0:
#     print("Number is divisible by 4 and 7")
# else:
#     print("number is not divisible by 4 and 7 both")

# 
# st = int(input("start from : "))
# en = int(input("end at :"))
# for i in range(st,en):
#     if i%4==0 and i%7==0:
#         print(f"{i} is divisible by 4 and 7")

"""if number is divisible by 3 print(mango)
if number is divisible 5 print(apple)
if number is divisible by 3 and 5 print(mango and apple)

"""

# num = int(input("Enter number: "))
# if num%3==0 and num%5==0:
#     print('Mango and Apple')
# elif num%3==0:
#     print('mango')
# elif num%5==0:
#     print("apple")
# else:
#     print(num)

# marks = eval(input("Enter your marks: "))

# if marks  >= 40:
#     print("pass")
# else:
#     print('Fail')

"""grade calculator
marks:
90 and above -> A
75-89 -> b
60 - 74 ->c
40 - 59 -> d
below 40 -> fail"""

# marks = int(input("Enter your marks: "))

# if marks >=90:
#     print("A grade")
# elif marks >=75:
#     print("B grade")
# elif marks >=60:
#     print("C grade")
# elif marks >=40:
#     print("D grade")
# elif marks >= 0:
#     print("Fail")
# else:
#     print("Invalid input")

"""ATM withdrawl"""

# balance = int(input("Enter the balance : "))
# withdraw = int(input("Enter the amount to withdraw: "))

# if withdraw<=balance:
#     balance -= withdraw
#     print(f"{withdraw}.rs withdraw")
#     print(f"Remaining balance: {balance}")
# else:
#     print("insufficient Balance")

"""Login System"""

# username = input("enter Username:")
# password  = input("password: ")

# user_data = {'username':'virat', 'password': 'RCB'}
# if username == user_data['username'] and password == user_data['password']:
#     print("Login sucessfuly")
# else:
#     print("invalid credentials")


"""print name of max salary of employee"""

# emp_sal = {'ramesh':30000,'umesh':70000,'suraj':20000,'harish':45000}
# max_sal =0

# for name, sal in emp_sal.items():
#     if max_sal<sal:
#         max_sal = sal
#         emp_name = name
# print(emp_name)

emp_details ={
    101:{'name':'pavan','department':'Operation','salary':36000},
    102:{'name':'vijay','department':'Placement','salary':50000},
    103:{'name':'arun','department':'Operation','salary':60000},
    104:{'name':'vikas','department':'Placement','salary':33000},
    105:{'name':'omkar','department':'Operation','salary':40000},
    106:{'name':'suresh','department':'Placement','salary':55000},
    107:{'name':'madhav','department':'Operation','salary':65000},
    108:{'name':'sujay','department':'Placement','salary':27000},
    109:{'name':'naresh','department':'Operation','salary':80000}
    }
max_placement_sal = 0
max_operation_sal = 0
for eid in emp_details:
    if emp_details[eid]['department']== 'Placement':
        if emp_details[eid]['salary']>max_placement_sal:
            max_placement_sal = emp_details[eid]['salary']
    elif emp_details[eid]['department']== 'Operation':
        if emp_details[eid]['salary']>max_operation_sal:
            max_operation_sal = emp_details[eid]['salary']
print(max_operation_sal,max_placement_sal)