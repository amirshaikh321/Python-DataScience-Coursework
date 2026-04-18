class Student:
    
    def __init__(self, name, marks, attendance_per, familly_income):
        self.name = name
        self.marks = marks
        self.atper = attendance_per
        self.income = familly_income
    def check_eligiblity(self):
        if self.marks >= 75 and self.atper >= 80 and self.income <300000:
            print("eligible")
        else:
            print("not eligible")
    def calculate_scholarship(self):
        if self.marks >= 90:
            scholrship = 50000
        elif 89 > self.marks >80:
            scholrship = 30000
        else:
            scholrship = 10000
        return scholrship
    
    def penalty_check(self):
        if self.atper >75:
            penalty = self.calculate_scholarship() - self.calculate_scholarship*20/100
        return penalty
    def final_amount(self):
        final_amount  = self.calculate_scholarship() - self.penalty_check()
        return final_amount 

    def display_details(self):
        details = f"""
        Name : {self.name} 
        marks : {self.marks}
        attendance : {self.atper}
        final amount : {self.final_amount()}

"""
s1= Student(101,92,87,200000)
s1.display_details()