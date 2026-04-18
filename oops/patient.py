
class Patient: 
    pid = 110
    name= "Jitendra"
    def __init__(self, room_days:int, treatment_cost:int, insurance:str):
        
        self.room_days = room_days
        self.tc = treatment_cost
        self.insurance = insurance
    
    def calculate_room_charges(self):
        charges = self.room_days*2000
        return charges

    def calculate_total_bill(self):
        room_charge = self.calculate_room_charges()
        t_bill = room_charge+ self.tc
        return t_bill
    
    def apply_insurance(self):
        tbill = self.calculate_total_bill()
        if self.apply_insurance() == "yes":
            insurance_cover =tbill*70/100
            return insurance_cover
        else:
            return insurance_cover
    def add_tax(self):
        tbill = self.calculate_total_bill()
        insurance_cover = self.apply_insurance()
        bill = tbill - insurance_cover
        tax = bill*5/100
        final_bill = bill + tax
        return final_bill
    
    def generate_bill(self):


        final_bill = self.add_tax()

        details= f"""
        Patient name: {Patient.name} | Pid : {Patient.pid}
        Insurance Covered : {self.apply_insurance()}\n
        Final bill = {self.add_tax()}
"""     
        print(details)

p1 = Patient(10,20000,'yes')
p1.generate_bill()
