from src.bank import Bank


class Bank_Netherlands(Bank):

    def check_balance_netherlands(self):
        print("the balance is converted to euro's")
        return self.check_balance()[0] / 1.1
