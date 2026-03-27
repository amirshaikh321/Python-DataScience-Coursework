"""
Dictionary methods:
    - get
syntax :
    - new_var = var[key]
    - new_var = var.get('key')
      
"""
print('\nget data from dictionary ->')
print('--'*55)
product = {'pname':'laptop','pid':'p123','price':60000}
mrp = product['price']
print(mrp)

print(product['pname'])
print(product.get('pid'))
print(product.get('discount',0))

c_loan_details ={'lid':'l101','name':'Prakash patil','principal':2000000,'rate':8.5,'year':3}
p = c_loan_details['principal']
r = c_loan_details['rate']
t = c_loan_details['year']

print()
SI = p*r*t/100
print("Simple Interest : ",SI)
print("Total Loan amount : ",SI + p)


"""
adding data into dictionary
syntax : 
    var[key]= value

"""
print('\nadd data into dictionary ->')
print('--'*55)
c_loan_details['total_amount']= p + SI
print(c_loan_details)

ajay_marks = {'t1': 80,'t2':67,'t3':89}

om = ajay_marks['t1']+ ajay_marks['t2']+ ajay_marks['t3']
total_marks = 300
per = om/total_marks*100

result = {}
result['Obtained_marks']= om
result['Total_marks']= total_marks
result['Percentage']= float(f'{per:0.2f}')
print(result)

"""
How to update Data
syntax : 
    var[key]= updated_value
"""
print('\nupdate data of dictionary ->')
print('--'*55)
details = {'name':'Amir','age':21}
details['name']= 'Amir Shaikh'
print(details)

print('\nExample: ')
print('--'*55)

emp = {'eid':101,'name': 'Pranav Patil', 'salary': 50000}
inc = 14/100
inc_amount = emp['salary']*inc
new_sal = inc_amount+ emp['salary']
print('Before Update: ', emp)
emp['salary']= int(new_sal)
print('After Update: ',emp)

"""
How to delete the data from dictionary
syntax : 
    var.pop(key)
    var.popitem()
"""
print('\nDelete data from dictionary ->')
print('--'*55)
emp = {'eid':101,'name':'Jarvis','salary': 50000}
emp.pop('eid')
print(emp)

emp = {'eid':101,'name':'Jarvis','salary': 50000}
emp.popitem()

print(emp)