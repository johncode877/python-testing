import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    
    def setUp(self) -> None:
      self.account = BankAccount(balance=1000) 
      self.other_account = BankAccount(balance=800) 

    def test_deposit(self):      
      #account = BankAccount(balance=1000) 
      new_balance = self.account.deposit(500)
      assert new_balance == 1500

    def test_withdraw(self):
      #account = BankAccount(balance=800)
      new_balance = self.account.withdraw(500)
      assert new_balance == 500

    def test_get_balance(self):
      #account = BankAccount(balance=200)
      assert self.account.get_balance() == 1000

    def test_transfer(self):
      #account = BankAccount(balance=200)
      assert self.account.transfer(200,self.other_account) == 800  

    def test_transfer_insuficiente(self):     
       with self.assertRaises(ValueError): 
         self.account.transfer(2000,self.other_account)
