"""
Program Name: Credit Union Accounts
Author: Rebecca Davidson
Date: 3/20/2023
Description: This program will display a member's bank account summary including balances and subshares
"""


class Account:
    """
    Credit Union Account
    """

    def __init__(self, account_number, full_name):
        self.__account_number = account_number
        self.full_name = full_name

    def account_summary(self):
        return f"{self.full_name}'s account number is {self.__account_number}"


if __name__ == "__main__":
    member = Account("123456", "Luis Santiago")
    print(member.account_summary())
