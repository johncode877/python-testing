import os
import unittest
from src.bank_account import BankAccount
from src.api_exchange_rate import Api_Exchange_Rate

class BankAccountTests(unittest.TestCase):
    
    api_exchange_rate = Api_Exchange_Rate()
    available_api = api_exchange_rate.is_available() 

    # Se ejecuta antes de cada prueba
    def setUp(self) -> None:
      self.account = BankAccount(balance=1000, log_file=f"transaction_log.txt")      
      self.other_account = BankAccount(balance=800)
      

    # Se ejecuta despues de cada prueba 
    def tearDown(self) -> None:
      if os.path.exists(self.account.log_file):
          os.remove(self.account.log_file)
 

    def _count_lines(self,filename):
      with open(filename,"r") as f:
         return len(f.readlines())
    
    def _get_last_transaction(self,filename) -> str:
      transaction=""
      with open(filename,"r") as f:
         transaction = f.readlines()

      if len(transaction):
         return transaction[len(transaction)-1]
      

    def test_deposit(self):      
      #account = BankAccount(balance=1000) 
      new_balance = self.account.deposit(500)
      #assert new_balance == 1500
      self.assertEqual(new_balance,1500,"El balance no es igual")

    def test_withdraw(self):
      #account = BankAccount(balance=800)
      new_balance = self.account.withdraw(500)
      #assert new_balance == 500
      self.assertEqual(new_balance,500,"El balance no es igual")

    def test_get_balance(self):
      #account = BankAccount(balance=200)
      #assert self.account.get_balance() == 1000
     self.assertEqual(self.account.get_balance(),1000)

    def test_transfer(self):
      #account = BankAccount(balance=200)
      assert self.account.transfer(200,self.other_account) == 800  

    def test_transfer_insuficiente(self):     
       with self.assertRaises(ValueError): 
         self.account.transfer(2000,self.other_account)
         assert self._count_lines(self.account.log_file) == 2
         assert self._get_last_transaction(self.account.log_file) == f"Insuficient Balance: {self.account.balance} - Amount: 2000"
     
    def test_transaction_log(self):
       self.account.deposit(500)
       #assert os.path.exists("transaction_log.txt")
       self.assertTrue(os.path.exists("transaction_log.txt"))

    
    def test_count_transactions(self):
       assert self._count_lines(self.account.log_file) == 1

       self.account.deposit(500)
       assert self._count_lines(self.account.log_file) == 2

    @unittest.skipUnless(available_api,"Api exchange rate no available")
    def test_deposit_in_dollars(self):
      self.assertEqual(self.account.deposit_in_dollars(100),1375) 
       
   
    
