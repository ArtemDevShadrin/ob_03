from dz.class_animals import Bird, Mammal, Reptile

def animal_sound(list_animal):
    for animal in list_animal:
        if isinstance(animal, Bird):
            animal_type = "птица"
        elif isinstance(animal, Mammal):
            animal_type = "млекопитающее"
        elif isinstance(animal, Reptile):
            animal_type = "рептилия"
        else:
            animal_type = "неизвестный вид"

        print(f"Это {animal_type} {animal.name}, ему {animal.age}. Он говорит - ", end="")
        animal.make_sound()


def animal_eats(list_animal):
    for animal in list_animal:
        if isinstance(animal, Bird):
            animal_type = "птица"
        elif isinstance(animal, Mammal):
            animal_type = "млекопитающее"
        elif isinstance(animal, Reptile):
            animal_type = "рептилия"
        else:
            animal_type = "неизвестный вид"

        print(f"Это {animal_type} {animal.name}, ему {animal.age}. Он кушает - ", end="")
        animal.eat()


def animal_all_info(list_animals):
    for animal in list_animals:
        if isinstance(animal, Bird):
            animal_type = "птица"
        elif isinstance(animal, Mammal):
            animal_type = "млекопитающее"
        elif isinstance(animal, Reptile):
            animal_type = "рептилия"
        else:
            animal_type = "неизвестный вид"

        print(f"Это {animal_type} {animal.name}, ему {animal.age}. Он кушает - ", end="")
        animal.eat()
        print(f"А говорит ", end="")
        animal.make_sound()


def employees_info(list_employees):
    for employee in list_employees:
        print(employee.name)

def employees_role_info(list_employees):
    for employee in list_employees:
        print(f"{employee.name} - {employee.role}")
