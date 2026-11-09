import math

'''
 Polymorphism: Optional Arguments
'''
class Car:
    def __init__(self, manufacturer="Honda", model="CRV", color="black", year=2026):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.year = year

myCar1 = Car(manufacturer="Toyota", model="Corrolla", color="yellow", year=2016)
myCar2 = Car(manufacturer="Porsche", model="911 GT3RS", color="red", year=2018)
myCar3 = Car(manufacturer="Buggati", model="Chiron Pur Sport", color="grey", year=2017)


'''
 Polymorphism: Methods with the same name.
'''
class Solid:
    def __init__(self):
        pass

    def surfaceArea(self):
        pass

    def volume(self):
        pass



class Cube(Solid):
    def __init__(self, dblSideLength):
        self.dblSideLength = dblSideLength

    def surfaceArea(self):
        return 6 * (self.dblSideLength ** 2)

    def volume(self):
        return self.dblSideLength ** 3



class Sphere(Solid):
    def __init__(self, dblRadius):
        self.dblRadius = dblRadius

    def surfaceArea(self):
        return 4 * math.pi * (self.dblRadius ** 2)

    def volume(self):
        return (4/3) * math.pi * (self.dblRadius ** 3)


'''
Super, Part 1
'''
class Employee:
    def __init__(self):
        pass

    def describe(self):
        print("I am an employee.")

class Manager(Employee):
    def describe(self):
        super().describe()
        print("I manage a team.")

my_manager1 = Manager()
my_manager1.describe()



'''
Part 4: Super, Part 2
'''
class Account:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate

    def display_account(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interestRate}")

    def add_interest(self):
        self.balance += (self.balance * self.interestRate)
        return self.balance


my_savings_acc1 = SavingsAccount(543678965, 67.99, 0.05)
my_savings_acc1.display_account()
print(my_savings_acc1.add_interest())