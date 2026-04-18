
class  Employee:
    cname = "Microsoft"
    location = "Bengluru"
    def __init__(self,eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary
    
    def calculate_allowances(self):
        HRA = self.salary*20/100
        DA = self.salary*10/100
        return HRA, DA
    def calculate_gross_salary(self):
        HRA, DA = self.calculate_allowances()
        gross_sal = self.salary + HRA + DA
        return gross_sal
    def calculate_net_salary(self):
        gs = self.calculate_gross_salary()
        tax = gs*10/100
        net_salary = gs- tax
        return net_salary, tax
    def payslip(self):
        HRA, DA = self.calculate_allowances()
        gs = self.calculate_gross_salary()
        ns,tax = self.calculate_net_salary()
        details = f"""
        Company name: {Employee.cname}, Location: {Employee.location}\n
        Employee name: {self.name} EID: {self.eid} Basic salary: {self.salary}
        -------------------------------------------------
        HRA : {HRA} | DA : {DA}
        Gross salary : {gs}
        Tax: {tax}
        Net salary : {ns}
        
"""
        print(details)

e1= Employee('amir',101,60000)
e1.payslip()
