def add():
    a= int(input("Enter Num1: "))
    b= int(input("Enter Num2: "))
    return print(a+b)

def sub():
    a= int(input("Enter Num1: "))
    b= int(input("Enter Num2: "))
    return print(a-b)

def mul():
    a= int(input("Enter Num1: "))
    b= int(input("Enter Num2: "))
    return print(a*b)

def div():
    a= int(input("Enter Num1: "))
    b= int(input("Enter Num2: "))
    return print(a/b)

def square(num):
    sq = num**2
    print(sq)

def iseven(num):
    if num%2==0:
        print(True)
    else:
        print(False)

def div_5(num):
    if num%5==0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

def si(principal,rate,time):

    si = principal*(rate/100)*time
    print(principal+si)

def fullname(fname,mname,sname,gender):
    if gender == 'male':
        title = 'mr.'
    elif gender == 'female':
        title = 'ms.'
    fullname=f"{title} {fname} {mname} {sname}"
    print(fullname)

def email(empname,companyname):
    em = empname+'@'+companyname+'.com'
    print(em)