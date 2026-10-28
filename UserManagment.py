from EmpManager import *

class frontend_Manager:
    def __init__(self):
        self.EmpManager =  EmpManager()

    def menu_print(self):
        print("\n Program Options ")

        Messages = [
            '1)Add a new Employee',
            '2) List all Employees',
            '3) delete by EMployee',
            '4) find employee details',
            '5) Update salary by id & name',
            '6) End the Program !'
        ]
        print('\n'.join(Messages))
        msg = f'Enter your choice (from 1 to {len(Messages)})'
        return input_is_valid(msg,1,len(Messages))
    def run(self):
        while True:
            choice = self.menu_print()
            if  choice == 1:
                self.EmpManager.Add_Employee()
            elif choice == 2:
                self.EmpManager.list_Employee()
            elif choice == 3:
                _id = int(input("Enter employee id: \n"))
                self.EmpManager.Delete_employee_with_id(_id)
            elif choice == 4:
                _id = int(input("Enter employee id: \n"))
                self.EmpManager.find_employee_with(_id)
            elif choice == 5:
                 _id= int(input("Enter employee id : \n"))
                 salary = float(input("Enter employee salary \n"))
                 self.EmpManager.Update_salary_by_id(_id,salary)
            else:
                break
                