# Simple ATM Project

balance = 1000   # Starting balance
correct_pin = "1234"

print("===== Welcome to ATM =====")

pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:
    while True:
        print("\nSelect an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your current balance is: ${balance}")

        elif choice == "2":
            deposit = float(input("Enter amount to deposit: "))
            if deposit > 0:
                balance += deposit
                print(f"${deposit} deposited successfully.")
                print(f"New balance: ${balance}")
            else:
                print("Invalid deposit amount!")

        elif choice == "3":
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= balance and withdraw > 0:
                balance -= withdraw
                print(f"${withdraw} withdrawn successfully.")
                print(f"Remaining balance: ${balance}")
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == "4":
            print("Thank you for using ATM !..")
            break

        else:
            print("Invalid choice! Please select 1-4.")

else:
    print("Incorrect PIN! Access denied.")