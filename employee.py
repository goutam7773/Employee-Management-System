class Employee :
    def __init__(self, id,name ,age, salary,contact):
        self._id = id
        self.name = name
        self.age = age
        self.salary = salary
        self.contact = contact

    def __str__(self):
        return f'Employee id {self._id} name {self.name} has age {self.age} and salary {self.salary}  contact {self.contact}'
    def __repr__(self):
        return f'Employee (id ={self._id}, name ={self.name} , age={self.age}, salary ={self.salary}, contact={self.contact})'

         