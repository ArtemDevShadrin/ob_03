from dz.class_animals import Bird, Mammal, Reptile
from dz.class_employee import ZooKeeper, Veterinarian
from dz.class_zoo import Zoo
from dz.func import animal_all_info, employees_info, employees_role_info

zoo = Zoo()

# Добавление животных
cow = Mammal("Крис", 3)
parrot = Bird("Кеша", 1)
python = Reptile("Снек", 2)

zoo.add_animal(cow)
zoo.add_animal(parrot)
zoo.add_animal(python)

# Добавление сотрудников
zookeeper = ZooKeeper("John")
veterinarian = Veterinarian("Alice")

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

# Получение информации
employees_role_info(zoo.employees)
animal_all_info(zoo.animals)
zookeeper.feed_animal(python)
veterinarian.heal_animal(parrot)

