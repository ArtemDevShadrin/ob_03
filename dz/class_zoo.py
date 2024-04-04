from dz.class_animals import Animal
from dz.class_employee import Employee


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
