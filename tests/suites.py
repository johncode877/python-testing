import unittest
from tests.test_bank_account import BankAccountTests


def bank_account_suite():
    print("bank_account_suite")
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit_positive_amount_increase_balance"))
    suite.addTest(BankAccountTests("test_withdraw_positive_amount_decrease_balance"))
    return suite



if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())