# class student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print(sum/3)

# s1 = student("ABC", [90,80,70])
# s1.get_avg()


class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.accnum = acc

    def debit(self, amount):
        self.balance =- amount
        print(amount,"debited from",self.accnum)
    
    def credit(self, amount):
        self.balance =+ amount
        print(amount,"credited to", self.accnum)

    def get_balance(self):
        return self.balance
    
