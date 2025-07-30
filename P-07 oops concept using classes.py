#OOPS CONCEPTS

#ENCAPSULATION
class Person:
    def __init__(self, a='coco', b='female'):
        self.name = a
        self.gender = b

    def showinfo(self):
        print("Name:", self.name)
        print("Gender:", self.gender)
p = Person()
p.showinfo()


#INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
dog = Dog("Buddy")
print(dog.speak())
print(cat.speak())


#OVERRIDING
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.speak()
d.speak()


#POLYMORPHISM
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"
def animal_sound(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()
animal_sound(cat)  
animal_sound(dog)
