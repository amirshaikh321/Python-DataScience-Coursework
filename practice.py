emp_details ={
    101:{'name':'pavan','department':'Operation','salary':36000},
    102:{'name':'vijay','department':'Placement','salary':50000},
    103:{'name':'arun','department':'Operation','salary':60000},
    104:{'name':'vikas','department':'Placement','salary':33000},
    105:{'name':'omkar','department':'Operation','salary':40000},
    106:{'name':'suresh','department':'Placement','salary':55000},
    107:{'name':'madhav','department':'Operation','salary':65000},
    108:{'name':'sujay','department':'Placement','salary':27000},
    109:{'name':'naresh','department':'Operation','salary':80000}
    }
total_salary ={}
total_count = {}
for empid in emp_details:
    dep = emp_details[empid]['department']
    sal = emp_details[empid]['salary']
    if emp_details[empid]['department'] in total_salary:
        total_salary[dep] = total_salary[dep]+sal
    else:
        total_salary[dep] = sal

print(total_salary)
