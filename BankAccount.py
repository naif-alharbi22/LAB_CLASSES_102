import random
class BankAccount:
    def __init__(self, account_holder , initial_balance = 0 ) -> None:
        card=[]
        while True:
            number="".join(random.choices('123456789' , k=10))
            if not number in card:
                card.append(number)
                break
        account_number=number
        self.account_number=account_number
        self.account_holder=account_holder
        self.initial_balance=initial_balance
    def deposit(self, pay:int)-> int:
        self.initial_balance+=pay
        return self.initial_balance
    def withdraw(self , pay:int):
        if self.initial_balance <= pay:
            return f"The balance is insufficient. Your balance is {self.initial_balance} riyals"
        else:
            self.initial_balance=self.initial_balance-pay
            return f"The transaction was completed successfully, your balance is now {self.initial_balance} riyals"
    def get_balance(self):
        return self.initial_balance
    def get_account_holder(self):
        return self.account_holder
    def get_account_number(self):
        return self.account_number