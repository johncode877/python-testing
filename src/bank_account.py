from __future__ import annotations
from src.api_exchange_rate import Api_Exchange_Rate

class BankAccount:
  
  api_exchange_rate = Api_Exchange_Rate()  

  def __init__(self, balance=0.0, log_file=None):
    self.balance = balance
    self.log_file = log_file
    self._log_transaction("Cuenta creada")


  def exchange_rate():
    return 

  def _log_transaction(self,message):
    if self.log_file:
      # abre el archivo en modo append
      with open(self.log_file,"a") as f:
       f.write(f"{message}\n")
  

  def deposit_in_dollars(self, amount):
    if amount > 0:      
      if self.api_exchange_rate.is_available():
        self.balance += amount * self.api_exchange_rate.get_exchange_rate()
        self._log_transaction(f"Deposited {amount} in $$. New balance: {self.balance}")
      else:
        self._log_transaction(f"No se pudo depositar porque el api no esta disponible")  
    return self.balance 

  def deposit(self, amount):
    if amount > 0: 
      self.balance += amount
      self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
    return self.balance

  def withdraw(self, amount):
    if amount > 0:
      self.balance -= amount
      self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
    return self.balance
  
  def get_balance(self):
    self._log_transaction(f"Checked balance. Current balance: {self.balance}")
    return self.balance
  
  def transfer(self, amount, account: BankAccount):
    if self.balance < amount:
       self._log_transaction(f"Insuficient Balance: {self.balance} - Amount: {amount}")
       raise ValueError("Balance insuficiente")
        
    account.deposit(amount)
    return self.withdraw(amount)

