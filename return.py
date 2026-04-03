
# def square(num):
#     sq = num**2
#     return sq

# def cube(num):
#     cu = num**3
#     return cu

# sq = square(5)
# cu = cube(5)
# print(sq+cu)

# def add(a,b):
#     print("addition of 2 numbers")
#     sum = a+b
#     return sum # return the value and terminate the function
#     print("end")# not run

# add(3,4)

# """
# The return statement is used inside a function to exit the function and send a specific value or object back to the caller. It marks the end of the function's execution any code written after a return statement in the same block will not be executed
# """

# def cal(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add, sub, mul, div

# print(cal(5,10))


# def si(p,r,t):

#     si =  p*(r/100)*t
#     total = p+si
#     return p, si, total

# principal, simple_iterest, total = si(50000,10,3)
# print(principal)
# print(simple_iterest)
# print(total)



def is_pal(word):
    w1 = word[::-1]
    if word == w1:
        return True
    else: 
        return False

print(is_pal('aba'))

def ispal(word):
    rev =''
    for ch in word:
        rev = ch+rev
        if rev == word:
            return True
        else:
            return False

print(ispal('abc'))

"""
Lambda Function->
    singel line function
    simple operation
    define using lambda keyword
    syntax :
        lambda parameters : expression
"""

print((lambda a,b : a+b)(34,65))
print((lambda fn,mn,sn : f'{fn} {mn} {sn}')("","prakash","yadav"))

print((lambda word : word[::-1]== word)('aba'))# word 
print((lambda num : num%2 == 0)(66)) # print True if num is even
print((lambda num : num%10 == 0)(66)) # print True if num is divisible by 10
