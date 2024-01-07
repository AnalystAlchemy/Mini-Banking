class BankAccount:
    def __init__(self, username, account_number, pin, balance=0,loan_limit=5000):
        self.username = username
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.loan_limit = loan_limit
        self.loan_amount = 0

    def login(self):
        entered_pin = input("Kindly enter the PIN to login: ")
        if entered_pin == self.pin:
            print(f"Login successful! Welcome, {self.username}!")
            return True
        else:
            print("Incorrect PIN. Login failed.")
            return False

    def deposit(self):
        amount = float(input("Enter the amount to deposit: Rs "))
        self.balance += amount
        print(f"Deposited Rs {amount}. Current balance: Rs {self.balance}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: Rs "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs {amount}. Current balance: Rs {self.balance}")
        else:
            print("Insufficient funds. Withdrawal failed.")

    def apply_loan(self):
        loan_amount = float(input("Enter the loan amount you want to apply for: Rs "))
        if loan_amount <= self.loan_limit and self.balance + self.loan_amount >= loan_amount:
            self.loan_amount += loan_amount
            self.balance += loan_amount
            print(f"Loan approved! You received Rs {loan_amount}. Current balance: Rs {self.balance}")
        else:
            print("Loan application rejected. Check eligibility and available balance.")

    def check_balance(self):
        print(f"Current balance: Rs {self.balance}")
        print(f"Loan amount: Rs {self.loan_amount}")


    def view_account_details(self):
        print("Account Details:")
        print(f"Username: {self.username}")
        print(f"Account Number: {self.account_number}")
        self.check_balance()




# Sample Usage
def create_account():
    username = input("Please enter your username: ")
    print(f"Hi {username} Welcome to SMR Banking services!!! ")
    account_number = input("Please enter your account number: ")
    pin = input("Set your PIN: ")
    print("A kindly REMAINDER!!!:The pin which has been set has to kept very confidential")
    return BankAccount(username, account_number, pin)

def main():
    # Create an account
    account = create_account()

    # Login
    if account.login():
        # Perform transactions
        account.deposit()
        account.check_balance()
        account.withdraw()
        account.apply_loan()
        account.check_balance()
        account.view_account_details()


if __name__ == "__main__":
    main()


