class Animal():
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


class Cow(Animal):
    def make_sound(self):
        print("Muuu!")


animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
