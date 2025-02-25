class Account:
    def init(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance


class Bank:
    def init(self):
        self.accounts = {}
    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            return "Initial deposit must be positive"
        account_number = len(self.accounts)+1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        return f"Account created successfully, Account_number: {account_number}"
    def view_account(self, account_number):
        if account_number in self.accounts:
            return str(self.accounts[account_number])
        else:
            return "Account not found"
        
    def deposit(account_number, amount):
        if amount < 0:
            return "Deposit cannot be negative"
        if not isinstance(amount, int) or amount == '':
            raise ValueError(f"amount cannot be {amount!r}")
        else:
            return "Amount added successfully"