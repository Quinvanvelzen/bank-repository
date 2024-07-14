from src.bank import Bank
from src.bank_Netherlands.bank import Bank_Netherlands


def main():
    bank_john_doe = Bank('John Doe')
    print(bank_john_doe.check_balance())

    bank_john_doe_netherlands = Bank_Netherlands('John Doe')
    print(bank_john_doe_netherlands.check_balance_netherlands())


if __name__ == "__main__":
    main()
