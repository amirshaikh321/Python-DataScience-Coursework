
x = lambda word,ch : word[0]==ch
print(x('amir','a'))

x = lambda word,ch : word[-1]==ch
print(x('java','a'))

"""
Higher order function in python is a function that either takes one o r more functions as arguments or returns a function as its result.

def f1():
    def f2():
        pass
    return f2

(lambda fun,p : pass)(f1,abc)

"""

numbers  = [1,2,3,5,6,6,73,42,65]
def iseven(num):
    return num%2==0

print(list(filter(iseven, numbers))) # even numbers

print(list(filter(lambda num: num%2!=0 , numbers))) # odd numbers 

print(list(filter(lambda num: num>20, numbers))) # numbers greater than 20 

students = ['tushar','rajesh','atharv','atul','om','prem','akash','anuradha']

print(list(filter(lambda name: name[0]=='a', students)))

students = {'tushar':70,'rajesh':90,'atharv':34,'atul':78,'om':54,'prem':76,'akash':86,'anuradha':99}

print(list(filter(lambda std: students[std]>=40,students)))
print(dict(filter(lambda  std: std[1]>=40, students.items())))

emp_salary = {'tushar':70000,'rajesh':90000,'atharv':34000,'atul':78000,'om':54000,'prem':76000,'akash':86000,'anuradha':99000}

print(list(filter(lambda emp: 32000<emp_salary[emp]<80000 , emp_salary)))

print(dict(filter(lambda emp: 32000<emp[1]<80000 , emp_salary.items())))

"""
map(fun,iterable)

"""

students = ['tushar','rajesh','atharv','atul','om','prem','akash','anuradha']
print(list(map(lambda name: name.upper(),students)))

numbers = [10,20,30,40,50,60,70,80]
print(list(map(lambda num: num/2, numbers)))

numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda num: num**2, numbers)))
print(dict(map(lambda num: (num,num**2), numbers)))

emp_salary = {'tushar':70000,'rajesh':90000,'atharv':34000,'atul':78000,'om':54000,'prem':76000,'akash':86000,'anuradha':99000}

print(dict(map(lambda emp: (emp[0],emp[1]+2000), emp_salary.items())))

numbers = [1,2,3,4,5]

def sum_num(numbers):
    sum =0
    for num in numbers:
        sum += num
    return sum
sum = sum_num(numbers)
print(sum)


from functools import reduce
print(reduce(lambda sum,num : sum+num, numbers,0))
print(reduce(lambda sum,num : sum+num, numbers))
x= ['jay','rajeshkumar','tope']
print(reduce(lambda new, name: new+ name+' ',x,''))