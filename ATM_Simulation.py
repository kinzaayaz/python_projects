class ATM:
    def __init__(self):
        self.balance = 1000
        
    def check_balance(self):
        print(f"Your current balance is {self.balance}")
    
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposited successfully. Your new balance is {self.balance}")
    
    def withdraw(self):
        amount = int(input("Enter amount for withdrawal: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is {self.balance}")
        else:
            print("Insufficient balance")
        
    def exit_atm(self):
        print("Thank you for using ATM.")

def main():
    atm = ATM()
    while True:
        print("""
        Welcome to the ATM!
        1. Check balance
        2. Deposit
        3. Withdraw
        4. Exit
        """)
        choice = int(input("Please choose an option: "))
        if choice == 1:
            atm.check_balance()
        elif choice == 2:
            atm.deposit()
        elif choice == 3:
            atm.withdraw()
        elif choice == 4:
            atm.exit_atm()
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
