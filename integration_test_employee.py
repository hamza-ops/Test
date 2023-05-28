import unittest
import employee

class TestEmployeeManagement(unittest.TestCase):
    def test_integrate(self):
        management = employee.EmployeeManagement()
        employee1 =  employee.Employee("John Doe", 22, 600, 'Sales')
        employee2 =  employee.Employee("Ahmed", 26, 601, 'Marketing')
        employee3 = employee.Employee("Bob Johnson", 40, 602, 'HR')
        management.add_employee(employee1)
        management.add_employee(employee2)
        management.add_employee(employee3)
        expected_output = {employee1.id: [employee1.name, employee1.age, employee1.dept]}
        self.assertEqual(expected_output, management.show_employee(employee1.id))
        self.assertIn(expected_output, management.employees)
        management.delete_employee(employee1.id)
        expected_output = {employee1.id: [employee1.name, employee1.age, employee1.dept]}
        self.assertNotIn(expected_output, management.employees)

if __name__ == "__main__":
     unittest.main()