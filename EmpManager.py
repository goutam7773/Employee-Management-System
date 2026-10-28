from employee import *
from Utility import*

class EmpManager:
    def __init__(self):
        self.employees = []

    def Add_Employee(self):
         print("Enter Employee data")
         _id = input_is_valid("Enter Employee id :")
         name = input(" Enter Employee name:")
         age = input_is_valid("Enter Employee age:")
         salary = input_is_valid("Enter Employee salary:")
         contact = input_is_valid("Enter Employee contact Number:")
         self.employees.append(Employee(_id, name,age,salary,contact))

    def list_Employee(self):
        if len(self.employees) == 0:
            print("\n Employee list is empty !")
            return
        else:
            for emp in self.employees:
                print(emp)

    def Delete_employee_with_id(self, _id):
        for emp in self.employees:
            if emp._id == _id:
                print(f"Deleting Employee Deatails : {emp._id}")
                self.employees.remove(emp)
            print("Employee is not found!")

    def find_employee_with (self,_id):
        for emp in self.employees:
            if emp._id == _id:
                print("Employee deatils:")
                return emp   
        print("Employee is not found!")
        return None
    def Update_salary_by_id(self,_id,salary):
        emp = self.find_employee_with(_id)
        if emp is None:
            print("\n Employee is not found")
        else:
            emp.salary = float(salary)
            print("Employee salary is successfully update!")
            print(emp)
            