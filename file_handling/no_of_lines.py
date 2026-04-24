def count_linnes(file_name):
    count= 0
    f = open(file_name,'r')
    for i in f:
        count +=1
    return count

# print(count_linnes('details.txt'))

def count_words(file_name):
    count= 0
    f = open(file_name,'r')
    data = str(f)
    l1 = list(data.split(' '))
    for word in l1:
        count += 1
    return count

print(count_words("data2.txt"))