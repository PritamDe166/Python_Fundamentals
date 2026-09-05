
## classes

class Car:
    def __init__(self, make:str, model:str, year: int):
        self.car_make = make
        self.car_model = model
        self.car_year = year

    def display_car_info(self):
        print(f"Car Make: {self.car_make}")
        print(f"Car Model: {self.car_model}")
        print(f"Car Year: {self.car_year}")

class BankAccount:
    def __init__(self, owner:str, balance:float):
        self.account_owner = owner
        self.account_balance = balance

    def deposit(self, amount:float):
        self.account_balance += amount
    
    def withdraw(self, amount:float):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient funds.")

    def show_balance(self):
        print(f"Account Owner: {self.account_owner}")
        print(f"Account Balance: {self.account_balance}")


class Employee:
    def __init__(self, name:str, salary:float):
        self.employee_name = name
        self.employee_salary = salary

    def give_raise(self, amount:float):
        self.employee_salary += amount

class Manager(Employee):
    def __init__(self, name:str, salary:float, team: list[str]):
        super().__init__(name, salary)
        self.team_members = team
    

        

## main function
def main():
    ## Create instances of the Car class
    nexon_car = Car("Tata", "Nexon", 2022)
    mercedes_car = Car("Mercedes-Benz", "C-Class", 2021)
    nexon_car.display_car_info()
    mercedes_car.display_car_info()

    ## Create instances of the BankAccount class
    john_account = BankAccount("John Doe", 1000.0)
    john_account.show_balance()
    john_account.deposit(500.0)
    john_account.withdraw(200.0)

    ## Create instances of the Employee and Manager classes
    employee1 = Employee("Alice", 50000.0)
    manager1 = Manager("Bob", 80000.0, ["Alice", "Charlie"])
    print(f"Manager: {manager1.employee_name}, Salary: {manager1.employee_salary}, Team Members: {manager1.team_members}")


main()