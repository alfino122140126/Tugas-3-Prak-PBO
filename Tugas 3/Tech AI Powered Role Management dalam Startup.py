class Employee:
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.task_completed = task_completed

    def work(self):
        pass

    def evaluate_performance(self):
        productivity = self.task_completed / self.hours_worked if self.hours_worked > 0 else 0
        if productivity > 1.5:
            return "High Performance"
        elif productivity > 1:
            return "Medium Performance"
        else:
            return "Low Performance"

class SoftwareEngineer(Employee):
    def work(self):
        print(f"{self.name} (Software Engineer) is coding.")

class DataScientist(Employee):
    def work(self):
        print(f"{self.name} (Data Scientist) is analyzing data.")

class ProductManager(Employee):
    def work(self):
        print(f"{self.name} (Product Manager) is managing the product roadmap.")

employees = [
    SoftwareEngineer("Alice", "Software Engineer", 40, 70),
    DataScientist("Bob", "Data Scientist", 35, 40),
    ProductManager("Charlie", "Product Manager", 50, 55),
    SoftwareEngineer("David", "Software Engineer", 30, 20)
]

for emp in employees:
    emp.work()
    print(f"Performance Rating: {emp.evaluate_performance()}")
    print()