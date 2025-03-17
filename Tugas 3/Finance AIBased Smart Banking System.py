class BankAccount:
    def __init__(self, account_holder, balance, currency):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency

    def __add__(self, amount):
        if isinstance(amount, BankAccount):
            if self.currency != amount.currency:
                converted_amount = self.convert_currency(amount.balance, amount.currency, self.currency)
                self.balance += converted_amount
            else:
                self.balance += amount.balance
        else:
            self.balance += amount
        return self

    def __sub__(self, amount):
        if isinstance(amount, BankAccount):
            if self.currency != amount.currency:
                converted_amount = self.convert_currency(amount.balance, amount.currency, self.currency)
                if self.balance >= converted_amount:
                    self.balance -= converted_amount
                else:
                    print("Insufficient balance for withdrawal!")
            else:
                if self.balance >= amount.balance:
                    self.balance -= amount.balance
                else:
                    print("Insufficient balance for withdrawal!")
        else:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient balance for withdrawal!")
        return self

    def apply_interest(self):
        if self.balance > 5000:
            self.balance *= 1.02
        else:
            self.balance *= 1.01
        print(f"Applying interest... New Balance = {self.balance:.2f} {self.currency}")

    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        rates = {
            "USD": 1,
            "EUR": 1.1,
            "IDR": 0.00007
        }
        return amount * (rates[to_currency] / rates[from_currency])

    def __str__(self):
        return f"{self.account_holder}'s Account: Balance = {self.balance:.2f} {self.currency}"

john = BankAccount("John", 5000, "USD")
emily = BankAccount("Emily", 1000, "EUR")

print(john)
john.apply_interest()

print(emily)
emily_withdraw = BankAccount("Emily", 1200, "USD")
emily - emily_withdraw
print(emily)