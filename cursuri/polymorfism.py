# polymorphic function
# functii care se numesc la fel dar au comportament diferit

def sum(a,b,c=0):
    return a+b+c

print(sum(3,4,5))
print(sum(3,4))

# polymorphism with inheritance
class Bird:
    def describe(self):
        print("I am a bird!!!!!!")

    def fly(self):
        print("I can't fly!")

    def sing(self):
        print("I cip cip cirip!!")

class Randunica(Bird):
    def fac_cuib(self):
        print("adun iarba")

class Pinguin(Bird):
    def fly(self):
        print("nu sunt chiar asa bun la zbor")

class Parrot(Bird):
    def sing(self):
        print("Eu nu fac cip cirip eu vorbesc")

coco = Parrot()
coco.sing()

pingu = Pinguin()
pingu.describe()
# daca avem doua functii cu aceeasi nume se foloseste functia din clasa copil
pingu.fly()