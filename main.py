# Write a Program to Simulate Working of an Automatic Teller Machine (ATM)
# Python code

# 1. Store user data (username, pin, balance)
user_data = {
    'ihtisham': {'pin': '1234', 'balance': 50000}
}


# 2. Function to update database text
def update_db(username, balance):
    # logic to write data to storage text file
    # for simplicity here we just update dict
    user_data[username]['balance'] = balance
    # print(user_data)
    # return True


# 3. Function to check balance
def check_balance(username):
    balance = user_data[username]['balance']
    print(f"Your Balance is Rs.{balance}\n")


# 4. Function to deposit amount
def deposit_amount(username):
    amount = float(input("Enter amount to deposit: Rs. "))
    if amount > 0:
        new_balance = user_data[username]['balance'] + amount
        update_db(username, new_balance)
        print("Deposited successfully.")
        check_balance(username)
    else:
        print("Invalid amount!")


# 5. Function to withdraw amount
def withdraw_amount(username):
    amount = float(input("Enter amount to withdraw: Rs. "))
    if amount > 0:
        if amount <= user_data[username]['balance']:
            new_balance = user_data[username]['balance'] - amount
            update_db(username, new_balance)
            print("Withdrawal successful.")
            check_balance(username)
        else:
            print("Insufficient balance!")


# 6. Function to show menu
def show_menu(username):
    while True:
        print("--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            check_balance(username)
        elif choice == '2':
            deposit_amount(username)
        elif choice == '3':
            withdraw_amount(username)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Main function
def main():
    print("--- Welcome to the ATM ---")
    username = input("Enter username: ")
    pin = input("Enter PIN: ")

    if username in user_data and user_data[username]['pin'] == pin:
        print("Login successful!\n")
        show_menu(username)
    else:
        print("Invalid username or PIN!")


# Run the ATM program
main()