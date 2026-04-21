""" Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows a class to derive attributes and methods from another class. It models an "is-a" relationship (e.g., a Dog is an Animal) and is primarily used to promote code reusability and simplify maintenance. """

# class A:
#     def m1(self):
#         print("m1 method")
#     def m2(self):
#         print("m3 method")

# class B(A):
#     def m3(self):
#         print("m3 method")
#     def m4(self):
#         print("m4 method")

# b1 = B()
# b1.m1()
# b1.m2()
# b1.m3()
# b1.m4()


class Saving_Account:
    bank_name = "Bank of India"
    branch = 'WAI'
    IFSC_code = 'SBIN0000545'
    all_transacttion = {}
    
    def __init__(self,nm, acc, bal):
        self.name = nm
        self.account = acc
        self.balance = bal
    
    def check_balance(self):
        print(f"Available Balance: {self.balance}")

    def deposite(self,amount):
        if isinstance(amount,(int,float)):
            if amount>0:
                self.balance+= amount
                self.add_transaction('deposite',amount,self.balance)
                return 'Amount deposite'
            else:
                return 'enter valid amount'
        else:
            return 'Enter Numeric value'
    
    def withdraw(self,amount):
        if isinstance(amount,(int,float)):
            if amount>0:
                if amount<self.balance:
                    self.balance-=amount
                    self.add_transaction('withdraw',amount,self.balance)
                    return 'amount is withdraw'
                else:
                    return "Insuficient balance"
            else:
                return "Enter Positive value"
        else:
            return 'Enter Numeric value'
    
    def add_transaction(self,type, amount, bal):
        from datetime import date
        date = str(date.today())
        id = 10001 + len(self.all_transacttion)
        self.all_transacttion[id]={'date':date,'type':type,'amount':amount, 'balance':bal}

    def transfer(self,account_ref, amount):
        self.withdraw(amount)
        account_ref.deposite(amount)

s1 = Saving_Account('Amir',8421652597,1200000)
s2 = Saving_Account('John',7641343545,145552)

s2.transfer(s1,20000)
print(s1.check_balance())
print(s2.check_balance())
print(s1.all_transacttion)