# encapsulation - cand ascundem atributele si folsoim getter sau setter sa ajunge la ele
# si metodele pot fi ascunse
# se ascund daca punem __

class Car:
    __color = "grey"

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def __init__(self, cutie):
        self.__cutie = cutie

    def describe(self):
        print(f"Vrum Vru!!!!My car is {self.color}")

    def __ascunsa(self):
        print("nu o poti vedea oricum")


dacia = Car()
print(dacia.get_color())
dacia.set_color("green")
print(dacia.get_color())
dacia.describe()