"""
Program Name: Credit Union Accounts
Author: Rebecca Davidson
Date: 3/20/2023
Description: This program will display a member's bank account summary including
balances and subshares
"""


class Account:
    """
    Credit Union Account
    """

    def __init__(self, account_number, full_name, account_balance):
        self.__account_number = account_number
        self.full_name = full_name
        self.account_balance = account_balance

    def account_summary(self):
        summery = f"{self.full_name}'s account number is {self.__account_number} and the account balance is {self.account_balance}"
        return summery


class Checking(Account):
    """
    Checking Account
    """

    def __init__(self, account_number, full_name, account_balance, checks="Checks"):
        self.checks = checks
        super().__init__(account_number, full_name, account_balance)

    def account_summary(self):
        summery = super().account_summary()
        summery = f"{summery} and has {self.checks} check(s)"
        return summery


class Credit(Account):
    """
    Credit Card
    """

    def __init__(
        self, account_number, full_name, account_balance, credit_card="Credit Card"
    ):
        self.credit_card = credit_card
        super().__init__(account_number, full_name, account_balance)

    def account_summary(self):
        summery = super().account_summary()
        summery = f"{summery} and has {self.credit_card} credit card(s)"
        return summery


if __name__ == "__main__":
    Katy = Account("123456", "Katy Perry", "$100,000")
    print(Katy.account_summary())
    Miley = Checking("234567", "Miley Cyrus", "$500,000", 1)
    print(Miley.account_summary())
    Taylor = Credit("4567890", "Taylor Swift", "$800,000", 2)
    print(Taylor.account_summary())
