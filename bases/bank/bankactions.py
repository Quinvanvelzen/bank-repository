import pandas as pd

from components.fake_data_base.data import hardcoded_data
from components.log.core import get_logger

logger = get_logger("greet-FastAPI-logger")


class BankActions:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def load_data():
        hardcoded_df = pd.DataFrame(hardcoded_data)
        return hardcoded_df

    def check_balance(self):
        df = self.load_data()

        # Check if the 'name' exists in the 'Account_Holder' column
        balance = df.loc[df['Account_Holder'] == self.name, 'Balance']

        # Check if the balance is not empty
        if not balance.empty:
            return balance.iloc[0]
        else:
            return "OH NO! You entered a wrong name :("