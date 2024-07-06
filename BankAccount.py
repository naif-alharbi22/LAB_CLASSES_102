import random
class BankAccount:

    _cards = []

    def __init__(self, account_holder , initial_balance = 0 ):
      self._account_number = self._generate_unique_account_number()
      self._account_holder = account_holder
      self._initial_balance = initial_balance

    def _generate_unique_account_number(self):
        while True:
            number = "".join(random.choices('123456789', k=10))
            if number not in BankAccount._cards:
                BankAccount._cards.append(number)
                return number
            
    def deposit(self, pay:int)-> int:
        self._initial_balance+=pay
        return f"Your account is now {self._initial_balance} riyals"
    
    def withdraw(self , pay:int):
        if self._initial_balance <= pay:
            return f"The balance is insufficient. Your balance is {self._initial_balance} riyals"
        else:
            self._initial_balance=self._initial_balance-pay
            return f"The transaction was completed successfully, your balance is now {self._initial_balance} riyals"
        
    def get_balance(self):
        return f"The amount in your account is {self._initial_balance} riyals"
    
    def get_account_holder(self):
        return f"The account holder's name is {self._account_holder}"
    
    def get_account_number(self):
        return f"{self._account_holder} account number is {self._account_number}"
    
    
