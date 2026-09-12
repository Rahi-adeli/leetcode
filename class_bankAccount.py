
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit (self):
        amount = int(input ("how much do you wanna deposit:"))
        self.balance += amount

    def withdraw (self):
        amount = int(input ("how much do you wanna withdraw:"))
        self.balance -= amount

    def show_the_balance (self):

        print(f"{self.owner} balances is {self.balance} euro")


this_account = BankAccount ("maya", 100000000000)
this_account.deposit()
this_account.withdraw()
this_account.show_the_balance()



#  بعدا اپشن انتخاب و لاک این و رمز و شماره کارت رو هم اضافهر کن