
marks = {'ajay pawar':{'t1':45,'t2':78},'vijay raut':{'t1':78,'t2':88}}

print(marks['ajay pawar']['t2'])
marks['vijay raut']['t3'] = 57
marks['ajay pawar']['t3'] = 75
print(marks)

marks = {'ajay pawar': {'t1': 45, 't2': 78, 't3': 75}, 'vijay raut': {'t1': 78, 't2': 88, 't3': 57}}

result = {}
t1 = marks['ajay pawar']['t1']
t2 = marks['ajay pawar']['t2']
t3 = marks['ajay pawar']['t3']
total = (t1+t2+t3)/3
result['ajay pawar']= total

t1 = marks['vijay raut']['t1']
t2 = marks['vijay raut']['t2']
t3 = marks['vijay raut']['t3']
total = (t1+t2+t3)/3
result['vijay raut']= total

print(result)

product  = {'p1':1000,'p2':5000}
selling_price = {}

p1 = product['p1']
p2 = product['p2']
p1_discount = p1*20/100
p2_discount = p2*20/100
selling_price['P1'] = p1-p1_discount
selling_price['P2'] = p2-p2_discount
print(selling_price)


bill_unit = {'c1':100, 'c2':300}
per_unit = 7

c1_unit = bill_unit['c1']
c2_unit = bill_unit['c2']
total_bill = {}

total_bill['c1_bill']= c1_unit*per_unit
total_bill['c2_bill']= c2_unit*per_unit

print(total_bill)

emp = {'name':'om raut', 'emp_id':101, 'basic_salry': 30000}
HRA = emp['basic_salry']*10/100
DA = emp['basic_salry']*8/100
gross = emp['basic_salry']+HRA+DA

emp.update(HRA=HRA,DA=DA,gross_sal=gross)
print(emp)