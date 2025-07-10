
class Employees:
    #constructor
    def __init__(self , name, email,dept ,salary):
        self.name= name
        self.email=email
        self.dept=dept
        self.salary=salary

    def emp_info(self):
        print(f'Name is {self.name}')
        print(f'Email is {self.email}')
        print(f'Department is {self.dept}')
        print(f'Salary is {self.salary}')


emp1 =Employees('Raju' , 'raju@email.com' ,'Sales' ,50000)
print(emp1.salary)