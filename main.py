class BankAccount:

  def __init__(self):
    self.balance = 0
    print("Bank account details ")

  def deposit(self):
    amount = float(input("enter the amount:"))
    self.balance += amount
    print("amount is deposit in your account ", amount)

  def withdraw(self):
    amount = float(input("enter your amount:"))
    if self.balance >= amount:
      self.balance -= amount
      print("your withdraw:", amount)
    else:
      print("you don't have enough money")

  def display(self):
    print("available balance:", self.balance)


s = BankAccount()
s.deposit()
s.withdraw()
s.display()
