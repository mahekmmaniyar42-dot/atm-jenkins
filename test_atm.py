import pytest
from atm import deposit, withdraw

def test_deposit():
    assert deposit(5000, 1500) == 6500

def test_withdraw_success():
    assert withdraw(5000, 2000) == 3000

def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(1000, 2000)
