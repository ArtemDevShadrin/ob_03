class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print("Чирик!")

    def eat(self):
        print("Cемена!")


class Mammal(Animal):
    def make_sound(self):
        print("Muuu!")

    def eat(self):
        print("Траву!")


class Reptile(Animal):
    def make_sound(self):
        print("SSSSSS!")

    def eat(self):
        print("Насекомых!")
