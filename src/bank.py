import pandas as pd


class Bank:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def load_data():
        from fake_data_base.data import hardcoded_data
        hardcoded_bank_data = pd.DataFrame(hardcoded_data)
        return hardcoded_data

    def check_balance(self):
        df = self.load_data()
        return df.loc[df['Account_Holder'] == self.name, ['Balance']]
