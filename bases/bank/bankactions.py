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
        return df.loc[df['Account_Holder'] == self.name, 'Balance']
