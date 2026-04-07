# Base class
class BankAccount:
    def __init__(self, name, balance):
        self.name = name              # public attribute
        self.__balance = balance     # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# Derived class (Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest of {interest} added.")


# Main program
acc1 = SavingsAccount("Abhinendra", 1000, 5)

acc1.deposit(500)
acc1.withdraw(300)
acc1.add_interest()

print("Final Balance:", acc1.get_balance())