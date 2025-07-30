class Account:
    def __init__(self, name, initial_balance, pin):
        self.name = name
        self.__balance = initial_balance
        self.__pin = pin

    def deposit(self, amount):
        if (amount > 0):
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if(amount > 0 and amount <= self.__balance):
            self.__balance = self.__balance - amount
            self.transactionSuccess = True
        elif(amount > self.__balance):
            self.transactionSuccess = False
            print("Insufficient Balance")

    def getBalance(self):
        return self.__balance
    
    def verifyPin(self, pin):
        return self.__pin == pin