class Employee:
    def __init__(self,salary):
        self.salary = salary
        self.HRA = self.salary*20/100
        self.DA = self.salary*10/100
        self.gross_sal = self.salary + self.HRA + self.DA 
        self.net_sal = self.gross_sal-self.gross_sal*10/100

    def allowances(self):
        self.HRA = self.salary*20/100
        self.DA = self.salary*10/100
        print(f"HRA is {self.HRA} | DA is {self.DA}")
    
    def calculate_gross_salary(self):
        print(self.gross_sal)

    def calculate_net_salary(self):
        # self.net_sal = self.gross_sal-self.gross_sal*10/100
        print(self.net_sal)

    def pay_slip(self):

        print(f"HRA : {self.HRA} | DA {self.DA}\nBasic salary: {self.salary} | Gross salary: {self.gross_sal}")
emp = Employee(20000)
emp.allowances()
emp.calculate_gross_salary()
emp.pay_slip()