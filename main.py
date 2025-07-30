from account import Account
from utils import returnToHome
from interface import commands
accounts = {}

def createAccount():
    name = input("Enter users name: ")
    initial_Balance = int(input("Enter how much do you want to deposit: "))
    userName = name.split()[0]
    accounts[userName] = Account(name, initial_Balance)
    print(f"Account ", userName, " with initial balance ", initial_Balance, " is created successfully.")
    returnToHome()
    
def main():
    while(True):
        commands()
        command = int(input("Enter your choice: "))

        if(command == 1):
            createAccount()

        elif(command == 2):
            key = input("Enter userName: ")
            if key in accounts:
                accountName = accounts[key]
                print("The balance of account ", key, " is ₹", accountName.getBalance())
            else:
                print("Account not found!")
            returnToHome()

        elif(command == 3):
            key = input("Enter username: ")
            amt = int(input("Enter amount to deposit: "))
            if key in accounts:
                accountName = accounts[key]
                accountName.deposit(amt)
                print("₹", amt, " is successfully deposited to account ", key, ".")
                print("Your current balance is ₹", accountName.getBalance())
            else:
                print("Account not found!")
            returnToHome()

        elif(command == 4):
            key = input("Enter username: ")
            amt = int(input("Enter amount to withdraw: "))
            if key in accounts:
                accountName = accounts[key]
                accountName.withdraw(amt)
                if(accountName.transactionSuccess):
                    print("₹", amt, " is successfully withdrawn from account ", key, ".")
                print("Your current balance is ₹",accountName.getBalance())
            else:
                print("Account not found!")
            returnToHome()

        elif(command == 5):
            print("Thanks for using Lena Dena Bank")
            break
        else:
            print("Enter valid command.")
            returnToHome()

if __name__ == "__main__":
    main()