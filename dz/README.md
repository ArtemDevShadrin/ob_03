# Zoo Management System

Данный проект представляет собой систему управления зоопарком. Включает в себя классы для животных, сотрудников 
зоопарка и самого зоопарка.

## Использование

### 1. Импортирование необходимых классов
from dz.class_animals import Bird, Mammal, Reptile
from dz.class_employee import ZooKeeper, Veterinarian
from dz.class_zoo import Zoo
from dz.func import animal_all_info, employees_info, employees_role_info

###  2. Создание экземпляра зоопарка
zoo = Zoo()

### 3. Добавление животных в зоопарк
cow = Mammal("Крис", 3)
parrot = Bird("Кеша", 1)
python = Reptile("Снек", 2)

zoo.add_animal(cow)
zoo.add_animal(parrot)
zoo.add_animal(python)

### 4. Добавление сотрудников в зоопарк
zookeeper = ZooKeeper("John")
veterinarian = Veterinarian("Alice")

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

### 5. Получение информации о сотрудниках и животных:
employees_role_info(zoo.employees)
animal_all_info(zoo.animals)

### 6. Вызов специфических методов сотрудников:
zookeeper.feed_animal(python)
veterinarian.heal_animal(parrot)


Структура проекта
zoo-management-system/


├── dz/<br />
│   ├── class_animals.py <br />
│   ├── class_employee.py <br />
│   ├── class_zoo.py <br />
│   ├──  func.py <br />
│   ├── README.md <br />



Лицензия
Этот проект лицензируется в соответствии с лицензией MIT. Подробности см. в файле LICENSE.

