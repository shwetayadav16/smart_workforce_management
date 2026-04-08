class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def to_tuple(self):
        return (self.emp_id, self.name, self.age, self.department, self.salary)