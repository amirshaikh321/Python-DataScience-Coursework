student_db = {101 : {'name':'vaibhav patil','course':'Data Analytics','tfees':40000,'pfees':30000,'rfees':10000}}

course_details = {"Data Science":50000,"Data Analytics":40000,"Web Development":30000,"AWS":20000}

while True:
    print("The Kiran Academy".center(100,'-'))
    print('''
    1.Add Student Details
    2.Display Student Record
    3.Update Student Record
    4.Delete Record
    5.Filter
    6.Search
    7.LogOut
    ''')
    print('-'*100)
    ch = int(input("Enter Your Choice: "))
    if ch==1:
        name = input("Name: ")
        sr = 1
        for coursename in course_details:
            print(f'{sr}.{coursename}')
            sr = sr+1
        ch = int(input("Select Your Course: "))
        all_acourse = list(course_details.keys())
        index = ch-1
        course =all_acourse[index]
        course_fees = course_details[course]
        print(f'fees for {course} :- {course_fees}')
        dis = float(input("Discount in Per: "))
        tfees = course_fees-course_fees * dis/100
        print(f'fees after {dis} % dis {course} - {tfees}')
        pfees = eval(input("enter pfees amount: "))
        rfees = tfees-pfees
        print(f'Total : {tfees}\nPaid Fees : {pfees}\nRfees: {rfees}')
        reg = 101+len(student_db)
        #v[k]=val
        student_db[reg]={'name':name,'course':course,'tfees':tfees,'pfees':pfees,'rfees':rfees}
        
    elif ch==2:
        print('-'*127)
        print(f"|{'RegNo':^20}|{'Student Name':^20}|{'Course Name':^20}|{'Tfees':^20}|{'Pfees':^20}|{'Rfees':^20}|")
        print('-'*127)

        for reg in student_db:
            print(f"|{reg:^20}|{student_db[reg]['name']:^20}|{student_db[reg]['course']:^20}|{student_db[reg]['tfees']:^20}|{student_db[reg]['pfees']:^20}|{student_db[reg]['rfees']:^20}|")
            print('-'*127)


    elif ch==3:
        reg = int(input("Reg: "))
        while reg not in student_db:
            print("Invalid Reg number")
            reg = int(input("Enter Again: "))
        print('''
        1.Name
        2.fees
        3.course change
            ''')
        ch = int(input("enter your choice: "))
        if ch==1:
            uname = input("Enter Name: ")
            #v[k]=uval
            student_db[reg]['name']=uname
            print("name updated successfully....")
        elif ch==2:
            tfees =student_db[reg]['tfees']
            pfees = student_db[reg]['pfees']
            rfees =student_db[reg]['rfees']

            print(f'''
                Tfees: {tfees}
                Pfees: {pfees}
                Rfees: {rfees}
            ''')
            amount = eval(input("enter amount: "))
            student_db[reg]['pfees'] = pfees+amount
            student_db[reg]['rfees'] = rfees-amount
            print(f"Rfees: {student_db[reg]['rfees']}")
        elif ch==3:
            sr = 1
            for coursename in course_details:
                print(f'{sr}.{coursename}')
                sr = sr+1
            ch = int(input("Select Your Course: "))
            all_acourse = list(course_details.keys())
            index = ch-1
            course =all_acourse[index]
            for i in course_details:
                if i == course:
                    course_fee = course_details[i]
            student_db[reg]['course'] = course  
            student_db[reg]['tfees'] = course_fee
            pfee = student_db[reg]['pfees']
            student_db[reg]['rfees']= course_fee-pfee

        else:
            print("Invalid Input")

    elif ch==4:
        reg = int(input("Reg: "))
        while reg not in student_db:
            print("Invalid Reg number")
            reg = int(input("Enter Again: "))
        student_db.pop(reg)
        
    elif ch==5:
        sr = 1
        for coursename in course_details:
            print(f'{sr}.{coursename}')
            sr = sr+1
        ch = int(input("Select Your Course: "))
        all_acourse = list(course_details.keys())
        index = ch-1
        coursename =all_acourse[index]

        print('-'*127)
        print(f"|{'RegNo':^20}|{'Student Name':^20}|{'Course Name':^20}|{'Tfees':^20}|{'Pfees':^20}|{'Rfees':^20}|")
        print('-'*127)

        for reg in student_db:
            if student_db[reg]['course']==coursename:
                print(f"|{reg:^20}|{student_db[reg]['name']:^20}|{student_db[reg]['course']:^20}|{student_db[reg]['tfees']:^20}|{student_db[reg]['pfees']:^20}|{student_db[reg]['rfees']:^20}|")
                print('-'*127)
    elif ch==6:
        #search Student Record
        reg = int(input('Enter Reg no: '))
        print('-'*127)
        print(f"|{'RegNo':^20}|{'Student Name':^20}|{'Course Name':^20}|{'Tfees':^20}|{'Pfees':^20}|{'Rfees':^20}|")
        print('-'*127)

        print(f"|{reg:^20}|{student_db[reg]['name']:^20}|{student_db[reg]['course']:^20}|{student_db[reg]['tfees']:^20}|{student_db[reg]['pfees']:^20}|{student_db[reg]['rfees']:^20}|")
        print('-'*127)
        
    elif ch==7:
        print('Loging out')
        break
    else:
        print("invalid input")