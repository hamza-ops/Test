class Employee:
    def __init__(self, name, age, id, dept):
        self.name = name
        self.age = age
        self.id = id
        self.dept = dept


class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        for dict in self.employees:
            if employee.id in dict:
                raise Exception()
            if (not isinstance(employee.id, int)) or (not isinstance(employee.age, int)) or (
                    not isinstance(employee.name, str)) or (not isinstance(employee.dept, str)):
                raise Exception()
            if (employee.id < 0 or employee.age < 0):
                raise Exception()
        self.employees.append({employee.id: [employee.name, employee.age, employee.dept]})

    def show_employee(self, id):
        #    print(self.employees)
        for employee in self.employees:
            if id in employee:
                return employee
        raise Exception

    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if id in employee:
                del self.employees[i]
                return
        raise Exception()


emp = Employee('Hamza', 20, 600, 'Marketing')
emp2 = Employee('Omar', 30, 601, 'HR')
emp3 = Employee('Ali', 40, 602, 'Sales')
emp_manage = EmployeeManagement()
emp_manage.add_employee(emp)
emp_manage.add_employee(emp2)
emp_manage.add_employee(emp3)
print(emp_manage.show_employee(emp.id))
print(emp_manage.show_employee(emp2.id))
print(emp_manage.show_employee(emp3.id))
emp_manage.delete_employee(emp.id)
# print(emp_manage.show_employee(emp.id))
# print(emp_manage.show_employee(emp2.id))
print(emp_manage.employees)
