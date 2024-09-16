import os
import unittest
from unittest.mock import patch
from src.bank_account import BankAccount
from src.api_exchange_rate import Api_Exchange_Rate
from src.exceptions import InsufficientFundsError, WithdrawalDayRestrictionError,WithdrawalTimeRestrictionError


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
      

    def test_deposit_positive_amount_increase_balance(self):      
      
      new_balance = self.account.deposit(500)
      
      self.assertEqual(new_balance,1500,"El balance no es igual")

    @patch("src.bank_account.datetime") 
    def test_withdraw_positive_amount_decrease_balance(self,mock_datetime):
      
      # 8 am monday
      mock_datetime.now.return_value.hour = 8
      mock_datetime.now.return_value.weekday.return_value = 0
      new_balance = self.account.withdraw(500)
      
      self.assertEqual(new_balance,500,"El balance no es igual")

    def test_get_balance(self):
     
     self.assertEqual(self.account.get_balance(),1000)

    @patch("src.bank_account.datetime") 
    def test_transfer_positive_amount_decrease_balance(self,mock_datetime):
      # 8 am monday
      mock_datetime.now.return_value.hour = 8
      mock_datetime.now.return_value.weekday.return_value = 0
      assert self.account.transfer(200,self.other_account) == 800  

    def test_transfer_positive_amount_insufficient_balance(self):     
       with self.assertRaises(ValueError): 
         self.account.transfer(2000,self.other_account)
         assert self._count_lines(self.account.log_file) == 2
         assert self._get_last_transaction(self.account.log_file) == f"Insufficient Balance: {self.account.balance} - Amount: 2000"
     
    def test_transaction_log(self):
       self.account.deposit(500)
     
       self.assertTrue(os.path.exists("transaction_log.txt"))

    
    def test_count_transactions(self):
       assert self._count_lines(self.account.log_file) == 1

       self.account.deposit(500)
       assert self._count_lines(self.account.log_file) == 2

    @unittest.skipUnless(available_api,"Api exchange rate no available")
    def test_deposit_in_dollars(self):
      self.assertEqual(self.account.deposit_in_dollars(100),1375) 
       
   
    @patch("src.bank_account.datetime") 
    def test_withdraw_during_bussiness_hour(self,mock_datetime):
      mock_datetime.now.return_value.hour = 8
      new_balance = self.account.withdraw(100)
      self.assertEqual(new_balance,900)
    
    @patch("src.bank_account.datetime") 
    def test_withdraw_disallow_before_bussiness_hour(self,mock_datetime):
      mock_datetime.now.return_value.hour = 7
      with self.assertRaises(WithdrawalTimeRestrictionError):
        self.account.withdraw(100)  

    @patch("src.bank_account.datetime") 
    def test_withdraw_disallow_after_bussiness_hour(self,mock_datetime):
      mock_datetime.now.return_value.hour = 19
      with self.assertRaises(WithdrawalTimeRestrictionError):
        self.account.withdraw(100)  

    @patch("src.bank_account.datetime") 
    def test_withdraw_day_allowed(self,mock_datetime):
      # 8 am monday
      mock_datetime.now.return_value.hour = 8
      mock_datetime.now.return_value.weekday.return_value = 0
      new_balance = self.account.withdraw(100)
      self.assertEqual(new_balance,900)

    @patch("src.bank_account.datetime") 
    def test_withdraw_disallowed_in_saturday(self,mock_datetime):
      # 8 am saturday
      mock_datetime.now.return_value.hour = 8
      mock_datetime.now.return_value.weekday.return_value = 5
      with self.assertRaises(WithdrawalDayRestrictionError):
        self.account.withdraw(100)  

    @patch("src.bank_account.datetime") 
    def test_withdraw_disallowed_in_sunday(self,mock_datetime):
      # 8 am sunday
      mock_datetime.now.return_value.hour = 8
      mock_datetime.now.return_value.weekday.return_value = 6
      with self.assertRaises(WithdrawalDayRestrictionError):
        self.account.withdraw(100)      


    def test_deposit_multiple_ammounts(self):
       
       # define los casos de prueba 
       test_cases = [
         {"ammount":100, "expected": 1100} ,
         {"ammount":3000, "expected": 4000} ,
         {"ammount":4500, "expected": 5500} ,
       ]
       
       for case in test_cases:
         with self.subTest(case=case):
           self.account = BankAccount(balance=1000,log_file="transaction.txt")
           new_balance = self.account.deposit(case["ammount"])
           self.assertEqual(new_balance,case["expected"])
