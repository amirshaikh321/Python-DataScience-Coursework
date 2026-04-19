roll = (1,5,8,3,9,10)
print(sorted(roll,reverse=True))

result = {5:66,1:55,7:89,2:33,3:78,4:78}

print(dict(sorted(result.items()))) 
print(dict(sorted(result.items(), key= lambda x: x[1])))
