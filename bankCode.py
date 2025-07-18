class BankSystem:
    def __init__(self, pin):
        self.correct_pin = pin
        self.balance = 0

    def login(self):
        attempts = 0
        while attempts < 3:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.correct_pin:
                print("Access granted!\n")
                return True
            if entered_pin < 4-digits:
                print("Pin should be 4-digits\n")
            else:
                attempts += 1
                print(f"Incorrect PIN. Attempts left: {3 - attempts}")
        print("Too many incorrect attempts. Access denied.")
        return False

    def deposit(self, amount):
        if amount < 500:
            print("Deposit failed: Minimum deposit is 500 KES.\n")
        else:
            self.balance += amount
            print(f"Deposit successful! New balance: {self.balance} KES\n")

    def withdraw(self, amount):
        if self.balance < 1500:
            print("Withdrawal failed: Balance must be at least 1500 KES.\n")
        elif amount > self.balance:
            print("Withdrawal failed: Insufficient balance.\n")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: {self.balance} KES\n")

    def check_balance(self):
        print(f"Your current balance is: {self.balance} KES\n")


