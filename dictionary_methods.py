"""
Dictionary Methods: 
    - clear -> it delete all the elements from dictionary
    -
"""


emp = {'eid':101,'name':'Jarvis','salary': 50000}
emp.clear()
print("clear:",emp)
emp = {'eid':101,'name':'Jarvis','salary': 50000}
emp1 = emp.copy()
print("copy:",emp1)
print(emp.items())
print(emp.keys())
print(emp.values())
emp2 = {"name":"Yogita"}
emp.update(emp2)
print(emp)