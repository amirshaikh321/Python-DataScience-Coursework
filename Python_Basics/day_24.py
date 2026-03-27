num = [1,2,3,4,5,6,7,8,9,10]

for i in num:

    if i %2!=0:
        continue
    print(i)

toppers = ['kunal kale','rajesh patil','vijay chopde','ajay satav','pranav deshmukh']
name = input('name: ')
for nm in toppers:
    if name == nm:
        print('yes')
        break
else:
    print('No')

"""
python allows yyou to use else clause with a for and while loop. The code within the else block is executed only if the loop completes all its iterations without encountering a break statement.
""" 