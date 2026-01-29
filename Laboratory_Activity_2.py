class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Successfully deposited ₱{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Successfully withdrew ₱{amount:.2f}")

    def display_balance(self):
        print(f"\nAccount Owner: {self.owner}")
        print(f"Current Balance: ₱{self.balance:.2f}")


def main():
    owner = input("Enter account owner name: ")
    account = BankAccount(owner)

    while True:
        try:
            print("\n--- Bank Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == "3":
                account.display_balance()

            elif choice == "4":
                print("Thank you for using the bank system.")
                break

            else:
                print("Invalid menu option.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
