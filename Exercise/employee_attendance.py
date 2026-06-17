
emp_attd = []
while True:

    eid = int(input("Enter Employee ID:"))
    
    if eid in emp_attd:
        print("employee already enter")
    elif eid == 0:
        print(emp_attd)
        break
    else:
        emp_attd.append(eid)
        print("Employee entered in office.")
    