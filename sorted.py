
numbers = [1,23,4,74,33,1,2,44,32,75]
print(sorted(numbers))

numbers = {5:32,1:65,6:98,3:65,9:75,2:97,4:13}
print(sorted(numbers.values()))
print(sorted(numbers.items(), key=lambda x: x[1]))