from abc import ABC


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):

    EMPLOYEE_WORK_LOAD = 8
    TAX = 0.15

    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.work_load = Employee.EMPLOYEE_WORK_LOAD
        self.__department = department

    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.work_load

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self.__department = department


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * Manager.TAX


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * Seller.TAX

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value
