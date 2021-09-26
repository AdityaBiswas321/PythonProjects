
    
    def foo(filepath):
        filepath=filepath
        with open(filepath, 'r') as file:
            balance=int(file.read())

    def withdraw( amount):
        balance=balance - amount
    
    def deposit(amount):
        balance=balance + amount

    def commit():
        with open(filepath, 'w') as file:
            file.write(str(balance))




account=(Account("account//balance.txt"))
print(account.balance)

#account.withdraw(100)
account.deposit(200)
print(account.balance)
account.commit()