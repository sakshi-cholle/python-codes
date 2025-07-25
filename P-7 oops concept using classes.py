#OOPS CONCEPTS

#ENCAPSULATION
class Person:
    def __init__(self, a='coco', b='female'):
        self.name = a
        self.gender = b

    def showinfo(self):
        print("Name:", self.name)
        print("Gender:", self.gender)

p = Person() #creating object
p.showinfo()

#INHERITANCE




