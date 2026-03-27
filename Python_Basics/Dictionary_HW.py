student = {'name':'Amir',
           'roll_no':'1',
           'course':'Data science'}

print(student)

batch = {'std1':{'name':'karan','roll_no': 2,'course':'data science'},
         'std2':{'name':'kunal','roll_no': 3,'course':'data science'}}

multiple_batch = {'B01':{'std1':{'name':'karan','roll_no': 2,'course':'data science'},
                        'std2':{'name':'kunal','roll_no': 3,'course':'data science'}},
                  'B02':{'std1':{'name':'sam','roll_no':43,'course':'java fullstack'},
                        'std2':{'name':'sahil','roll_no': 44,'course':'java fullstack'}}}

course = {'python':{'B01':{'std1':{'name':'Janvi','roll_no': 22,'course':'Python fullstack'},
                        'std2':{'name':'Suhani','roll_no': 32,'course':'Python fullstack'}},
                    'B02':{'std1':{'name':'Aarya','roll_no':13,'course':'Python fullstack'},
                        'std2':{'name':'shreya','roll_no': 65,'course':'Python fullstack'}},
          'Java':{'B10':{'std1':{'name':'ram','roll_no':54,'course':'java fullstack'},
                        'std2':{'name':'Tommy','roll_no': 55,'course':'java fullstack'}},
                  'B10':{'std1':{'name':'John','roll_no':56,'course':'java fullstack'},
                        'std2':{'name':'robert','roll_no': 57,'course':'java fullstack'}}}}}

print("\nStudent details:")
print("--"*50)
print(student)

print("\nStudent details of Batch:")
print("--"*50)
print(batch)

print("\nStudent details of Multiple Batch:")
print("--"*50)
print(multiple_batch)

print("\nStudent details as per course:")
print("--"*50)
print(multiple_batch)