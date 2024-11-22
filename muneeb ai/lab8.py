class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        print(f"Department: {self.department}")

def read_employee_info(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip())

def add_employee_info(file_name, employee_info):
    with open(file_name, 'a') as file:
        file.write(employee_info + '\n')

def save_employee_info(file_name, employee_info_list):
    with open(file_name, 'w') as file:
        for info in employee_info_list:
            file.write(info + '\n')




