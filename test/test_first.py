
import unittest
from bases.bank.bankactions import BankActions
from components.fake_data_base.data import hardcoded_data
import numpy as np

class TestBankActions(unittest.TestCase):

    def test_hardcoded_data(self):
        # Check if hardcoded_data is not None or empty
        self.assertIsNotNone(hardcoded_data, "The hardcoded data should not be None")
        self.assertTrue(len(hardcoded_data) > 0, "The hardcoded data should not be empty")

    def test_check_balance(self):
        # Test the check_balance function of BankActions with a sample user 'john'
        bank_user = BankActions('John')
        balance_info = bank_user.check_balance()

        # Check if balance_info is of a numeric type and within expected range
        self.assertIsInstance(balance_info, (int, float, np.float64), "Balance info should be a number")
        self.assertGreaterEqual(balance_info, 0, "Balance should be non-negative")  # Example check, adjust if needed


if __name__ == '__main__':
    unittest.main()
