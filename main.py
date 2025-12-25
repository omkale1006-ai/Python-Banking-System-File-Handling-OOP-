import os
import random
from datetime import datetime

class Bank:
    def __init__(self):
        self.account_file = "accounts.txt"
        self.transaction_file = "transactions.txt"

        if not os.path.exists(self.account_file):
            open(self.account_file, "w").close()

        if not os.path.exists(self.transaction_file):
            open(self.transaction_file, "w").close()

    # ---------- Create Account ----------
    def create_account(self):
        name = input("Enter name: ")
        mobile = input("Enter mobile number: ")
        pin = input("Set 4-digit PIN: ")

        # Step 1: check if account already exists
        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1] == name and data[2] == mobile:
                    print("❌ You already have an account")
                    return   

        # Step 2: create account ONLY ONCE
        acc_no = "ACC" + str(random.randint(10000, 99999)) + str(int(datetime.now().timestamp()))

        with open(self.account_file, "a") as f:
            f.write(f"{acc_no},{name},{mobile},{pin},0,card-no\n")

        print("\n✅ Account Created Successfully")
        print("🏦 Your Account Number:", acc_no)


    # ---------- Login ----------
    def login(self):
        acc_no = input("Enter Account Number: ")
        pin = input("Enter PIN: ")

        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no and data[3] == pin:
                    print(f"\n✅ Welcome {data[1]}")
                    return acc_no

        print("\n❌ Invalid Account Number or PIN")
        return None

    # ---------- Search by Name ----------
    def search(self):
        name = input("Enter name: ")
        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1] == name:
                    print("🏦 Account Number:", data[0])
                    return
        print("❌ No account found")

    # ---------- Search by Phone ----------
    def search_phone(self):
        phone = input("Enter phone number: ")
        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[2] == phone:
                    print("🏦 Account Number:", data[0])
                    return
        print("❌ No account found")

    # ---------- Deposit ----------
    def deposit(self, acc_no):
        amount = float(input("Enter amount to deposit: "))
        updated = []

        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    data[4] = str(float(data[4]) + amount)
                    self.save_transaction(acc_no, "Deposit", amount)
                updated.append(",".join(data))

        with open(self.account_file, "w") as f:
            f.write("\n".join(updated) + "\n")

        print("✅ Amount Deposited")

    # ---------- Withdraw ----------
    def withdraw(self, acc_no):
        amount = float(input("Enter amount to withdraw: "))
        updated = []

        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    balance = float(data[4])
                    if amount > balance:
                        print("❌ Insufficient Balance")
                        return
                    data[4] = str(balance - amount)
                    self.save_transaction(acc_no, "Withdraw", amount)
                updated.append(",".join(data))

        with open(self.account_file, "w") as f:
            f.write("\n".join(updated) + "\n")

        print("✅ Amount Withdrawn")

    # ---------- Balance ----------
    def check_balance(self, acc_no):
        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    print("💰 Balance:", data[4])
                    return

    # ---------- Transactions ----------
    def save_transaction(self, acc_no, t_type, amount):
        with open(self.transaction_file, "a") as f:
            f.write(f"{acc_no},{t_type},{amount},{datetime.now()}\n")

    def transaction_history(self, acc_no):
        print("\n📄 Transaction History")
        found = False
        with open(self.transaction_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no:
                    print(f"{data[3]} | {data[1]} | ₹{data[2]}")
                    found = True
        if not found:
            print("No transactions found")

    # ---------- Reset PIN ----------
    def reset_pin(self):
        acc_no = input("Enter Account Number: ")
        mobile = input("Enter Registered Mobile Number: ")
        new_pin = input("Enter New 4-digit PIN: ")

        updated = []
        found = False

        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == acc_no and data[2] == mobile:
                    data[3] = new_pin
                    found = True
                updated.append(",".join(data))

        if found:
            with open(self.account_file, "w") as f:
                f.write("\n".join(updated) + "\n")
            print("✅ PIN Reset Successful")
        else:
            print("❌ Account details not matched")
    # ---------- change mobile number ----------
    def change_phone(self):
        acc_no = input("Enter Account Number: ")
        pin = input("Enter pin Number: ")
        new_number = input("Enter your new phone number: ")
        upadate_number = []
        found = False

        with open("accounts.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0]== acc_no and data[3] == pin:
                    data[2] = new_number
                    found = True
                upadate_number.append(",".join(data))
        if found:
            with open(self.account_file, "w") as f:
                f.write("\n".join(upadate_number) + "\n")
            print("✅ mobile number change Successful")
        else:
            print("❌ Account details not matched")




    #--------------chard applying---------
    def card_apply(self, ):
        updated = []
        found = False

        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")

                if data[5] != "card-no":
                    print("❌ You already have a card")
                    return
                else:
                    card_number = "OK" + str(random.randint(100000, 999999))
                    data[5] = card_number
                    found = True
                    print("✅ Card Applied Successfully")
                    print("💳 Your Card Number:", card_number)

            updated.append(",".join(data))

        if found:
            with open(self.account_file, "w") as f:
                f.write("\n".join(updated) + "\n")






# ---------- Main Program ----------
bank = Bank()

while True:
    print("\n🏦 BANK MENU")
    print("1. Create Account")
    print("2. Login")
    print("3. Get Account No (Name)")
    print("4. Get Account No (Phone)")
    print("5. Reset PIN")
    print("6. change phone number")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        user = bank.login()
        if user:
            while True:
                print("\n--- Customer Menu ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. card apply.")
                print("6. Logout")

                ch = input("Choose: ")

                if ch == "1":
                    bank.deposit(user)
                elif ch == "2":
                    bank.withdraw(user)
                elif ch == "3":
                    bank.check_balance(user)
                elif ch == "4":
                    bank.transaction_history(user)
                elif ch == "5":
                    bank.card_apply()
                elif ch == "6":
                    break

    elif choice == "3":
        bank.search()

    elif choice == "4":
        bank.search_phone()

    elif choice == "5":
        bank.reset_pin()
    
    elif choice == "6":
        bank.change_phone()

    elif choice == "7":
        print("🙏 Thank you for using Banking System")
        break

    else:
        print("❌ Invalid choice")
