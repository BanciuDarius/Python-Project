# o clasa abstracta e o clas afara corp are doar metode cu logica definate
# o interfata e o clasa care contine doar metode abstracte
# metodele abstracte sunt metode ce trebuie implementate neaparat de toti mostenitorii

'''
Abstraction from Google
Abstraction is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementation of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
VS
An Abstract class can contain the both method normal and abstract method.
Abstract methods have no budy, they have just the name and
An Interface contains only abstract methods
'''
# avem nevoie de acest import pt abstractizare in python
from abc import ABC, abstractmethod


# clasa abstracta poate sa contina metode abstracte
# interfata contine doar metode abstracte

class Bird(ABC):
    def describe(self):
        print("I am a bird!!!!!!")

    # se foleste acest decorator ca sa evidentiem ca e o metoda abstracta
    # metoda abstracta = metoda fara corp(fara logica interna)
    @abstractmethod
    def fly(self):
       pass

    def sing(self):
        print("I cip cip cirip!!")

class Parrot(Bird):
    def varsta(self):
        print("am 4 ani")

    def fly(self):
        print("I can flyyyyyy!!!")

coco = Parrot()
coco.describe()

# clasa interfata(Interface) - toate metodele sunt abstracte
# obliga clasele mostenitoare sa implementeze toate functiile - ca o reteta, ca si cum ar fi functii required
class Animal(ABC):
    @abstractmethod
    def sound(self):
        raise NotImplementedError
    @abstractmethod
    def pedigree(self):
        raise NotImplementedError
    @abstractmethod
    def home(self):
        raise NotImplementedError

# a class implements an interface
class Dog(Animal):
    def nume(self,nume):
        print(f"numele meu este {nume}")

    def sound(self):
        print("ham ham")

    def pedigree(self):
        return True

    def home(self):
        print("doarme in pat")

rex = Dog()
rex.nume("Rex")