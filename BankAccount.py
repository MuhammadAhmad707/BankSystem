class BankAccount:
    
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount:.2f} successfully. New balance: {self.balance:.2f}"
        return "Error: Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew: {amount:.2f} successfully. New balance: {self.balance:.2f}"
            return "Error: Insufficient funds."
        return "Error: Withdrawal amount must be positive."

    def display_balance(self):
        return f"Current Balance for {self.account_holder}: {self.balance:.2f}"


if __name__ == "__main__":
    acc1 = BankAccount("Alice") 
    acc2 = BankAccount("Bob")

    while True:
        print("\n--------- Bank Menu ---------") 
        print("1. Deposit")  
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1': 
            amount = float(input("Enter amount to deposit: "))
            result = acc1.deposit(amount)
            print(result)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            result = acc1.withdraw(amount)
            print(result)
        elif choice == '3':
            result = acc1.display_balance()
            print(result)
        elif choice == '4':
            print("Thank you for using bank")
            break
        else:
            print("Invalid option. Please try again.")