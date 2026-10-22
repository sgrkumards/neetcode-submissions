class BankAccount: 
    # TODO:  Add class and instance attributes at their appropriate places
    total_account = 0 # class attribute
    total_balance = 0 # class attribute

    def __init__(self, name : str, balance :int) -> None:
        self.name = name #Instance
        self.balance = balance # Instance 
        BankAccount.total_account += 1
        BankAccount.total_balance += balance
    


# TODO: Create two accounts
Alice = BankAccount("Alice", 1000)
Bob = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${Alice.balance}")
print(f"Bob's balance: ${Bob.balance}")
print(f"Total Accounts: {BankAccount.total_account}")
print(f"Total Balance: ${BankAccount.total_balance}")
