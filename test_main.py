"""
Program Name: Test for Classes
Author: Rebecca Davidson
Date: 3/20/2023
Description: This program will display a member's bank account summary including balances and subshares
"""

from main import Account, Checking, Credit


def test_account_number():
    """
    Test that the account number is correct
    """
    test_member = Account("1111111", "Test McTest", "$1.00")
    summary = test_member.account_summary()
    assert "1111111" in summary


def test_name():
    """
    Test that the account number is correct
    """
    test_member2 = Account("2222222", "Testianna Testerson", "$2.00")
    summary2 = test_member2.account_summary()
    assert "Testianna Testerson" in summary2


def test_balance():
    """
    Test that the account blance is correct
    """
    test_member3 = Account("3333333", "Testian Testoppolus", "$3.00")
    summary3 = test_member3.account_summary()
    assert "$3.00" in summary3


def test_checks():
    """
    Test that the checking account has checks
    """
    test_member4 = Checking("4444444", "Test Test Jr.", "$4.00", 8)
    summary4 = test_member4.account_summary()
    assert "8" in summary4


def test_credit_card():
    """
    Test that the credit card has a credit card
    """
    test_member5 = Credit("5555555", "Testian Testoppolus", "$5.00", 5)
    summary5 = test_member5.account_summary()
    assert "5" in summary5
