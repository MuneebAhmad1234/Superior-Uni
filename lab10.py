class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

def add_employee(employee):
    pass

def display_all_employees():
    pass

def update_employee_information(employee):
    pass

def delete_employee(employee):
    pass

def menu():
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Update Employee Information")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice

while True:
    choice = menu()

    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        print("Exiting Employee Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
