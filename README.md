# 🏧 ATM Machine in Python

A simple command-line based ATM Machine simulation built using Python. This program demonstrates fundamental programming concepts such as functions, conditionals, loops, and basic user interaction.

---

## ✨ Features

- User authentication (PIN-based)
- Balance enquiry 💰
- Deposit funds ➕
- Withdraw funds ➖
- Exit the system gracefully 🚪

---

## 🧾 Sample ATM Code

```python
class ATM:
    def __init__(self, pin, balance=0):
        self.correct_pin = pin
        self.balance = balance

    def authenticate(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.correct_pin:
            print("✅ Authentication successful!\n")
            return True
        else:
            print("❌ Incorrect PIN!\n")
            return False

    def check_balance(self):
        print(f"💼 Your current balance is: ₹{self.balance}\n")

    def deposit(self):
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            self.balance += amount
            print(f"✅ ₹{amount} deposited successfully!\n")
        else:
            print("❌ Invalid deposit amount!\n")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: ₹"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully!\n")
        else:
            print("❌ Insufficient balance or invalid amount!\n")

    def run(self):
        if not self.authenticate():
            return

        while True:
            print("====== ATM Menu ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("👋 Thank you for using our ATM. Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")

# Main execution
if __name__ == "__main__":
    atm = ATM(pin="1234", balance=5000)
    atm.run()