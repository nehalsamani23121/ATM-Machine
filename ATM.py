# Description:- Simple ATM Machine Program In Python
# Author:- Nehal Samani
# Date:- 04-13-2025

balance = 5000  # initial balance
pin = "1234"    # ATM PIN

# Authenticate user
user_pin = input("Enter your ATM PIN: ")
if user_pin != pin:
    print("❌ Incorrect PIN. Access denied!")
else:
    print("✅ Welcome to the ATM!\n")

    while True:
        print("------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"💰 Your balance is: ₹{balance}\n")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"✅ ₹{amount} deposited. New balance: ₹{balance}\n")
            else:
                print("❌ Invalid amount!\n")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"✅ ₹{amount} withdrawn. New balance: ₹{balance}\n")
            else:
                print("❌ Insufficient funds or invalid amount!\n")

        elif choice == '4':
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.\n")