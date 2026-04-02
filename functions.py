def apply_dis():
    amount = int(input("Enter Product amount: "))
    dis = int(input("Enter Discount: "))
    final_dis = amount*dis/100
    final_amt = amount-final_dis
    print(final_amt)

# apply_dis()


"""
Function for calculate simple interest
"""
def cal_simple_interest():
    p = int(input('enter your loan amount: '))
    r = int(input("rate of interest: "))
    t = int(input("No of years:"))
    si = p*(r/100)*t
    print(f'{si:.2f}')
# cal_simple_interest()

"""create a function to calculate no of charcter in given string"""

# def len_char():
#     n =0
#     ch = input("Enter a string: ")
#     for i in ch:
#         n += 1
#     print(n)

# len_char()


"""create a function to count total number of words in given sentence"""

def len_word():
    sent = input("Sentence: ")
    word_count =0
    word_list = sent.split()
    for ch in word_list:
        word_count += 1
    print(word_count)

# len_word()

"""count no of vowels"""
def count_vowels():
    vowel = ['a','e','i','o','u']
    count = 0
    word = input('enter word :')
    for ch in word:
        if ch in vowel:
            count += 1
    print(count)
# count_vowels()

"""create a function to count the repitation of char"""

def count_ch():
    word = input('Enter word: ')
    char = input("character to search: ")
    count = 0

    for ch in word:
        if char == ch:
            count +=1      
    print(count)
# count_ch()

def count_word_rep():

    sentence = input('Enter sentence: ')
    word = input('Enter word: ')
    count = 0
    l1= sentence.split()
    for i in l1:
        if word == i:
            count += 1
    print(count)
count_word_rep()