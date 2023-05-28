import unittest
import employee

class TestEmployeeManagement(unittest.TestCase):
    def test_add_employee(self):
        management = employee.EmployeeManagement()
        employee1 = employee.Employee("John Doe", 22, 600, 'Sales')
        management.add_employee(employee1)
        self.assertIn({employee1.id: [employee1.name, employee1.age, employee1.dept]}, management.employees)

    def test_show_employees(self):
        management = employee.EmployeeManagement()
        employee1 =  employee.Employee("John Doe", 22, 600, 'Sales')
        employee2 =  employee.Employee("Ahmed", 26, 601, 'Marketing')
        employee3 = employee.Employee("Bob Johnson", 40, 602, 'HR')
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.add_employee(employee3)
        expected_output = {employee1.id: [employee1.name, employee1.age, employee1.dept]}
        self.assertEqual(expected_output, management.show_employee(employee1.id))

    def test_delete_employee(self):
        management = employee.EmployeeManagement()
        employee1 =  employee.Employee("John Doe", 22, 600, 'Sales')
        employee2 =  employee.Employee("Ahmed", 26, 601, 'Marketing')
        employee3 = employee.Employee("Bob Johnson", 40, 602, 'HR')
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.add_employee(employee3)
        management.delete_employee(employee1.id)
        expected_output = {employee1.id: [employee1.name, employee1.age, employee1.dept]}
        self.assertNotIn(expected_output, management.employees)

    def test_duplicate_id(self):
        management = employee.EmployeeManagement()
        employee1 = employee.Employee("John Doe", 22, 600, 'Sales')
        employee2 = employee.Employee("Ahmed", 26, 600, 'Marketing')
        management.add_employee(employee1)
        with self.assertRaises(Exception):
            management.add_employee(employee2)

    def test_delete_missing_employee(self):
        management = employee.EmployeeManagement()
        with self.assertRaises(Exception):
            management.delete_employee(12345)


if __name__ == "__main__":
     unittest.main()