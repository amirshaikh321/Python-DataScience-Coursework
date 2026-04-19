# write a program to find the sum of all numbers from 1 to 10.
# sum =0
# for i in range(1,11):
#     sum += i

# print(sum)

# write a program to find the sum of all even numbers from 1 to 10

# sum = 0
# for i in range(1,11):
#     if i%2==0:
#         sum += i

# print(sum)

# write a program to find the sum of all odd numbers from 1 to 10

# sum = 0
# for i in range(1,11):
#     if i%2!=0:
#         sum += i

# print(sum)

# write a program to calculate the length of an iterable (like a string or list) without using build-in len()

# len = 0
# str = "Java"
# for i in str:
#     len += 1 
# print(len)


# students = ['ishwar','rajesh','krishna','pavan','om','ram']
# len=0
# std_dict = {}
# for name in students:
#     for ch in name: 
#         len += 1
#     std_dict[name]=len
#     len = 0
# print(std_dict)

# WAP to count uppercase character

# name = "pavAnKumAr"
# count = 0
# for ch in name:
#     if ch == ch.upper():
#         count += 1

# print(count)

# students = ['iShwaR','RaJesH','kRiShNa','Pavan','OM','RaM']
# len=0
# std_dict = {}
# for name in students:
#     for ch in name: 
#         if ch.isupper():
#             len += 1
#     std_dict[name]=len
#     len = 0
# print(std_dict)

# WAP to count how many vowels (a,e,i,o,u) are present in a given string

# count =0
# name = "Karishma"
# vowels = ("a","e","i","o","u") 
# for ch in name: 
#     if ch in vowels:
#         count += 1
# print(count)

# WAP to count number of even numbers and number of odd numbers
# numbers = [10,20,30,11,21,45,33,78,14,27,89]
# even_count = 0
# odd_count = 0 
# dic = {}
# for num in numbers:
#     if num%2==0:
#         even_count += 1
#     else:
#         odd_count += 1
# dic["even"]=even_count
# dic['odd']= odd_count
# print(dic)

# name = "vaibhav"
# dic = {}
# for ch in name:
#     if ch in dic:
#         dic[ch] = dic[ch]+1
#     else:
#         dic[ch] = 1
# print(dic)

# WAP to reverse a string without using slicing

# name = "JAVA"
# new = ""
# for i in name:
#     new= i+ new
# print(new)

# students = ['ishwar','rajesh','krishna','pavan','om','ram']
# reverse ={}
# for name in students:
#     rev = ""
#     for i in name:
#         rev= i+ rev
#     reverse[name] = rev
# print(reverse)

str1= "aba"
rev = ""
for ch in str1:
    rev = ch +rev
if str1 == rev:
    print(f"{str1} is palindrome")
else:
    print(f"{str1} is not palindrome")