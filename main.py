from account import Account
from utils import returnToHome
from interface import commands
accounts = {}

def createAccount():
    name = input("Enter users name: ")
    initial_Balance = int(input("Enter how much do you want to deposit: "))
    pin = int(input("Create a new 4 digit numberic pin: "))
    userName = name.split()[0]
    accounts[userName] = Account(name, initial_Balance, pin)
    print(f"Account ", userName, " with initial balance ", initial_Balance, " is created successfully.")
    returnToHome()

def authenticate(accountName):
    pin = int(input("Enter your password: "))
    if(accountName.verifyPin(pin)):
        return True
    else:
        return False
    
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
                if(authenticate(accountName)):
                    print("The balance of account ", key, " is ₹", accountName.getBalance())
                else:
                    print("Unauthorized Access!")
            else:
                print("Account not found!")
            returnToHome()

        elif(command == 3):
            key = input("Enter username: ")
            amt = int(input("Enter amount to deposit: "))
            if key in accounts:
                accountName = accounts[key]
                if(authenticate(accountName)):
                    accountName.deposit(amt)
                    print("₹", amt, " is successfully deposited to account ", key, ".")
                    print("Your current balance is ₹", accountName.getBalance())
                else:
                    print("Unauthorized Access!")
            else:
                print("Account not found!")
            returnToHome()

        elif(command == 4):
            key = input("Enter username: ")
            amt = int(input("Enter amount to withdraw: "))
            if key in accounts:
                accountName = accounts[key]
                if(authenticate(accountName)):
                    accountName.withdraw(amt)
                    if(accountName.transactionSuccess):
                         print("₹", amt, " is successfully withdrawn from account ", key, ".")
                         print("Your current balance is ₹",accountName.getBalance())
                else:
                    print("Unauthorized Access!")
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