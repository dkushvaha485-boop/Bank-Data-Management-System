import os
import time

# File jahan data rahega
DATA_FILE = "bank_records.txt"

def clear_screen():
    # Windows ke liye 'cls', Mac/Linux ke liye 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize():
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, "w").close()

def login():
    clear_screen()
    print("====================================")
    print("      SECURE BANK LOGIN SYSTEM      ")
    print("====================================")
    user = input("Enter Admin Username: ")
    pwd = input("Enter Admin Password: ")
    
    if user == "admin" and pwd == "1234":
        print("\nVerifying...")
        time.sleep(1) # Thoda drama/feel ke liye delay
        return True
    else:
        print("\n❌ Access Denied! Galat Password.")
        time.sleep(2)
        return False

def add_user():
    clear_screen()
    print("--- 👤 NEW USER ONBOARDING ---")
    acc = input("Assign Account No: ")
    
    # Check if exists
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.startswith(acc + ","):
                print("\n❌ Error: Ye Account No pehle se booked hai!")
                input("\nPress Enter to go back...")
                return

    name = input("Customer Full Name: ")
    phone = input("Contact Number: ")
    try:
        bal = float(input("Opening Balance (Rs): "))
        with open(DATA_FILE, "a") as f:
            f.write(f"{acc},{name},{phone},{bal}\n")
        print("\n✅ User Added Successfully in Database!")
    except:
        print("\n❌ Invalid Input! Account nahi bana.")
    
    input("\nPress Enter to continue...")

def view_all():
    clear_screen()
    print("--- 📋 ALL REGISTERED CUSTOMERS ---")
    print(f"{'ACC':<10} {'NAME':<20} {'BALANCE':<10}")
    print("-" * 45)
    
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()
        if not lines:
            print("Database Khali Hai!")
        for line in lines:
            d = line.strip().split(",")
            print(f"{d[0]:<10} {d[1]:<20} Rs.{d[3]}")
            
    input("\nPress Enter to return to Menu...")

def transaction(mode):
    clear_screen()
    print(f"--- 💰 {mode.upper()} SYSTEM ---")
    acc_id = input("Enter Customer Account No: ")
    found = False
    temp_list = []

    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        data = line.strip().split(",")
        if data[0] == acc_id:
            found = True
            current_bal = float(data[3])
            try:
                amt = float(input(f"Amount to {mode}: Rs."))
                if mode == "Withdraw" and amt > current_bal:
                    print("❌ Insufficient Balance!")
                else:
                    if mode == "Withdraw":
                        current_bal -= amt
                    else:
                        current_bal += amt
                    data[3] = str(current_bal)
                    print(f"\n✅ Transaction Done! New Balance: Rs.{current_bal}")
            except:
                print("❌ Invalid Amount!")
        temp_list.append(",".join(data) + "\n")

    if found:
        with open(DATA_FILE, "w") as f:
            f.writelines(temp_list)
    else:
        print("❌ Account Not Found!")
    
    input("\nPress Enter to continue...")

# --- MAIN FLOW ---
initialize()
if login():
    while True:
        clear_screen()
        print("====================================")
        print("      BANK DATA MANAGEMENT v1.0     ")
        print("====================================")
        print("1. Register New Customer")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View All Records")
        print("5. Exit System")
        print("====================================")
        
        choice = input("Select Service (1-5): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            transaction("Deposit")
        elif choice == '3':
            transaction("Withdraw")
        elif choice == '4':
            view_all()
        elif choice == '5':
            print("\nShutting down system...")
            time.sleep(1)
            break
        else:
            print("Wrong Choice!")
            time.sleep(1)