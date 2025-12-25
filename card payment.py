import os
from datetime import datetime

class Card:
    def __init__(self):
        self.account_file = "accounts.txt"
        self.transaction_file = "transactions.txt"

        if not os.path.exists(self.account_file):
            open(self.account_file, "w").close()

        if not os.path.exists(self.transaction_file):
            open(self.transaction_file, "w").close()

    # ---------- Card + PIN Verification ----------
    def check_card(self, card_no, pin):
        with open(self.account_file, "r") as f:
            for line in f:
                data = line.strip().split(",")

                if data[5] == card_no and data[3] == pin:
                    return data[0]   # ✅ return account number

        print("❌ Invalid Card Number or PIN")
        return None

    # ---------- Withdraw using Card ----------
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
                    self.save_transaction(acc_no, "ATM Withdraw", amount)

                updated.append(",".join(data))

        with open(self.account_file, "w") as f:
            f.write("\n".join(updated) + "\n")

        print("✅ Please collect your cash")

    # ---------- Save Transaction ----------
    def save_transaction(self, acc_no, t_type, amount):
        with open(self.transaction_file, "a") as f:
            f.write(f"{acc_no},{t_type},{amount},{datetime.now()}\n")


# ---------- ATM Simulation ----------
atm = Card()

while True:
    print("\n🏧 ATM MACHINE")
    card_no = input("Enter Card Number: ")
    pin = input("Enter PIN: ")

    acc_no = atm.check_card(card_no, pin)

    if acc_no:
        atm.withdraw(acc_no)

    ch = input("Do you want another transaction? (yes/no): ").lower()
    if ch != "yes":
        print("🙏 Thank you for using ATM")
        break
