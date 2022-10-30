# mostenire - o clasa o sa ia denumirea de parinte, si o clasa ia denumirea de copil
# clasa copil o sa mosteneasca toate atributele si metodele din clasa parinte
# o clasa parinte poate sa aiba oricati copii

# clasa parinte
class Chef:
    def make_salad(self):
        print("make salad")

    def make_eggs(self):
        print("make eggs")

    def make_fries(self):
        print("make fries")


class Chef_Italian(Chef):
    def make_pasta(self):
        print("make pasta")
    def make_pizza(self):
        print("make pizza")

class Chef_Japanesse(Chef):
    def make_sushi(self):
        print("make sushi")
    def make_rice(self):
        print("make rice")


mariuca = Chef()
mariuca.make_eggs()

antonio = Chef_Italian()
antonio.make_eggs()

yung = Chef_Japanesse()
yung.make_rice()