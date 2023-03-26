"""
Program Name: Test for Classes
Author: Rebecca Davidson
Date: 3/20/2023
Description: This program will display a member's bank account summary including balances and subshares
"""

from main import Account


def test_account_number():
    """
    Test that the account number is correct
    """
    test_member = Account("246812", "Test McTest")
    summary = test_member.account_summary()
    assert "246812" in summary


def test_name():
    """
    Test that the account number is correct
    """
    test_member2 = Account("3691113", "Testianna Testerson")
    summary2 = test_member2.account_summary()
    assert "Testianna Testerson" in summary2
