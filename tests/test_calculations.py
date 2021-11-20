import pytest
from calculations import BankAccount, InsufficientFunds, add, add_string, divide, multiply, subtract

# Simple tests to check if the functions are returning the correct value


def test_add():
    print("Testing add function...")
    assert add(2, 3) == 5
    assert add(10, 10) == 20


def test_add_negative():
    assert add(-2, 3) == 1
    assert add(10, -10) == 0


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(10, 10) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 10) == 1


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(10, 10) == 100


def test_add_string():
    assert add_string('2', '3') == 5
    assert add_string('10', '10') == 20


def test_add_string_negative():
    assert add_string('-2', '3') == 1
    assert add_string('10', '-10') == 0

# Parametrizing tests
# https://docs.pytest.org/en/6.2.x/parametrize.html


@pytest.mark.parametrize('a,b,expected', [
    (1, 1, 2),
    (2, 2, 4),
    (3, 3, 6),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Simple tests for BankAccount class


def test_test_bank_set_initial_balance():
    bank_account = BankAccount()
    assert bank_account.balance == 0


def test_test_bank_set_initial_balance_with_value():
    bank_account = BankAccount(100)
    assert bank_account.balance == 100


def test_test_bank_deposit():
    bank_account = BankAccount()
    bank_account.deposit(100)
    assert bank_account.balance == 100


def test_test_bank_deposit_with_value():
    bank_account = BankAccount()
    bank_account.deposit(100)
    assert bank_account.balance == 100


def test_test_bank_withdraw():
    bank_account = BankAccount()
    bank_account.deposit(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50


def test_test_bank_withdraw_with_value():
    bank_account = BankAccount()
    bank_account.deposit(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50


def test_test_bank_get_balance():
    bank_account = BankAccount()
    bank_account.deposit(100)
    assert bank_account.get_balance() == 100


def test_test_bank_get_balance_with_value():
    bank_account = BankAccount(100)
    assert bank_account.get_balance() == 100


def test_test_bank_str():
    bank_account = BankAccount()
    assert str(bank_account) == "Account balance: 0"


def test_test_bank_str_with_value():
    bank_account = BankAccount(100)
    assert str(bank_account) == "Account balance: 100"


def test_test_bank_transfer_to():
    bank_account_1 = BankAccount()
    bank_account_2 = BankAccount()
    bank_account_1.deposit(100)
    bank_account_1.transfer_to(bank_account_2, 50)
    assert bank_account_1.balance == 50
    assert bank_account_2.balance == 50


def test_test_bank_transfer_from():
    bank_account_1 = BankAccount()
    bank_account_2 = BankAccount()
    bank_account_2.deposit(100)
    bank_account_1.transfer_from(bank_account_2, 50)
    assert bank_account_1.balance == 50
    assert bank_account_2.balance == 50


def test_add_accounts_balance():
    bank_account_1 = BankAccount(100)
    bank_account_2 = BankAccount(200)
    assert add(bank_account_1, bank_account_2) == 300


def test_interest():
    bank_account = BankAccount(100)
    assert round(bank_account.interest(1.1)) == 110


# Fixtures
# https://docs.pytest.org/en/6.2.x/fixture.html


@pytest.fixture
def bank_account_chequing():
    return BankAccount()


@pytest.fixture
def bank_account_savings():
    return BankAccount()


def test_bank_account_deposit(bank_account_chequing):
    bank_account_chequing.deposit(100)
    assert bank_account_chequing.balance == 100


def test_bank_account_chequing_withdraw(bank_account_chequing):
    bank_account_chequing.deposit(100)
    bank_account_chequing.withdraw(50)
    assert bank_account_chequing.balance == 50


def test_bank_account_chequing_get_balance(bank_account_chequing):
    bank_account_chequing.deposit(100)
    assert bank_account_chequing.get_balance() == 100


def test_bank_account_chequing_str(bank_account_chequing):
    assert str(bank_account_chequing) == "Account balance: 0"


def test_bank_account_transfer_to(bank_account_chequing, bank_account_savings):
    bank_account_chequing.deposit(100)
    bank_account_chequing.transfer_to(bank_account_savings, 50)
    assert bank_account_chequing.balance == 50
    assert bank_account_savings.balance == 50


def test_bank_account_transfer_from(bank_account_chequing, bank_account_savings):
    bank_account_chequing.deposit(100)
    bank_account_savings.transfer_from(bank_account_chequing, 50)
    assert bank_account_chequing.balance == 50
    assert bank_account_savings.balance == 50


def test_add_accounts_balance(bank_account_chequing, bank_account_savings):
    bank_account_chequing.deposit(100)
    bank_account_savings.deposit(200)
    assert add(bank_account_chequing, bank_account_savings) == 300


def test_interest(bank_account_chequing):
    bank_account_chequing.deposit(100)
    assert round(bank_account_chequing.interest(1.1)) == 110


# Parametrized fixtures
# https://docs.pytest.org/en/6.2.x/fixture.html#parametrized-fixtures

@pytest.mark.parametrize("deposited, withdrawn, expected", [
    (100, 50, 50),
    (100, 100, 0),
    (100, 0, 100),
])
def test_bank_account_transactions(bank_account_chequing, deposited, withdrawn, expected):
    bank_account_chequing.deposit(deposited)
    bank_account_chequing.withdraw(withdrawn)
    assert bank_account_chequing.balance == expected

# Testing exceptions
# https://docs.pytest.org/en/6.2.x/usage.html#exceptions

def test_insufficient_funds(bank_account_chequing):
    with pytest.raises(InsufficientFunds):
        bank_account_chequing.withdraw(1)