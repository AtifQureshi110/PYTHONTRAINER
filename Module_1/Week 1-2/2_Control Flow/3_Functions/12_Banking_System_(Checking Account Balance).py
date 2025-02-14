def has_sufficient_balance(balance, amount):
    """Checks if the user has enough balance for a transaction."""
    if balance >= amount:
        return True
    else:
        return False

# Real-world example:
current_balance = 5000
withdraw_amount = 2000

if has_sufficient_balance(current_balance, withdraw_amount):
    print("Transaction Approved!")
else:
    print("Insufficient Balance!")
