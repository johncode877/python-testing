from __future__ import annotations

class BankAccount:
  
  def __init__(self, balance=0):
    self.balance = balance

  def deposit(self, amount):
    if amount > 0: 
      self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount > 0:
      self.balance -= amount
    return self.balance
  
  def get_balance(self):
    return self.balance
  
  def transfer(self, amount, account: BankAccount):
    if self.balance < amount:
       raise ValueError("Balance insuficiente")
    
    account.deposit(amount)

    return self.withdraw(amount)

