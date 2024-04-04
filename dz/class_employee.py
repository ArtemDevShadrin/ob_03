class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Zoo Keeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")
