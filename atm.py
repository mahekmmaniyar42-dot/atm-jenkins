import sys

def deposit(balance, amount):
    if amount <= 0:
        raise ValueError("Deposited amount must be positive")
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    if amount <= 0:
        raise ValueError("Withdraw amount must be positive")
    return balance - amount

if __name__ == "__main__":
    balance = float(sys.argv[1]) if len(sys.argv) > 1 else 5000.0
    dept_amt = float(sys.argv[2]) if len(sys.argv) > 2 else 1500.0
    with_amt = float(sys.argv[3]) if len(sys.argv) > 3 else 2000.0

    print(f"Initial Balance: {balance}")
    balance = deposit(balance, dept_amt)
    print(f"After deposit({dept_amt}): {balance}")
    balance = withdraw(balance, with_amt)
    print(f"After withdrawal({with_amt}): {balance}")
