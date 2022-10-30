# #cum citim de la tastatura mai multe variabile
# nume,prenume,varsta = input("Vreau un nume, un prenume, varsta").split()
# print(f"numele meu e {nume}, prenumele {prenume} si am {varsta} ani")
# print("numele neu e " + nume + "dsgfdhfghfg")
#
#
# text = input("vreau un string")
# text_separat = text.split(' ')
# print(type(text_separat))
#
# lista = ["ana", "maria", "dfdg", "vasile"]
# print(lista[0])
#
# lungime = float(input("lungime ="))
# latime = float(input("latime ="))
# print("aria este " + str(float(lungime)* float(latime)))
# print(f"aria este {lungime*latime}")

text = "ana are mere si pere"
#de unde incepem: pana unde vrem sa mearaga: si din cat in cat
print(text[2:-2])

#tipuri de date - liste, tuple, set, dictionare
#lista - pastreaza mai multe valori intr-o singura variabila
lista_masini = ["mazda", "dacia", "aro"]
lunile_anului = ["ianuarie","februarie", "martie"]
lista = ["ana", " maria", 465567, 67.8, 434565, True, False, "SFDG"]
lista_browsers = ["chrome", "firefox", "safari"]
#lista e ordonata - fiecare element are un index , incepe de la 0, daca adaugam un element il adauga la final

#lista e mutabila - se pot sterge si adauga elemente
print(lista_masini[0])
print(lista[4])
#cum adaugam in lista
#cu append fara sa ii dam pozitia adauga tot timpul la final
lista_masini.append("renault")
print(lista_masini)
#si ii zicem pozitia pe care sa adauge
lista_masini.insert(1, "bmw")
print(lista_masini)


lista_castigatori = ["ion", "vasile", "stefan"]
lista_castigatori.append(0)
lista_castigatori.insert(99, 5.6)
print(lista_castigatori)
lista_castigatori.insert(80, "pop")
#asa aflam pe ce pozitie e un element
print(lista_castigatori.index("pop"))
print(lista_castigatori)
#cum stergem
#stergem dupa valoare
print(lista_castigatori.remove("ion"))
print(lista_castigatori)
#asa stergem o anumita pozitie
print(lista_castigatori.pop(1))
print(lista_castigatori)
#asa stergem ultimul
print(lista_castigatori.pop())
print(lista_castigatori)

#putem avea valori duplicate
lista= ["ion", "ion", "ion", "dsdfsd", 5, 6, 7 , 9 , 20, 45, 56]
#lungimea listei
print(len(lista))
print(lista)
#de unde , pana unde, din cat in cat
print(lista[2:])
print(lista[2::3])
print(lista[::-1])
lista.reverse()
print(lista)
lista =[4,6,7,89,67]
print(max(4,6,7,89,67))
print(lista)
lista.sort()
print(lista)


varsta =[4,6,7,89,67]
print(varsta[-1])
varsta.pop(2)
print(varsta)
text="anaaremere"
nume="ion"
print(text[1]+nume[-1])

lista1= ["ion", "ion", "ion", "dsdfsd", 5, 6, 7, 9 , 20, 45, 56]
#asa schimbam valori din lista, suprascriem
lista1[0]="vasile"
lista1[10]="sdfsdf"
print(lista1)

lista = [3,4,"ioana", [3,4,5,[3,4,5,6,0]], ["ana", "maria", "cristina"]]
print(lista[1])
print(lista[3][1])
print(lista[3][3])
print(lista[3][3][4])
print(lista[4][2])
lista2=[1,2,3]
lista3=[4,5,6]
lista = lista2+lista3
print(lista)
#extinde lista cu o alta lista
print(lista2)
lista2.extend(lista3)
print(lista2)
lista1= ["ion", "ion", "ion", "dsdfsd", 5, 6, 7, 9 , 20, 45, 56, True, 4.5]
print(type(lista1[0]))
print(type(lista1[4]))
print(type(lista1[-2]))
print(type(lista1[-1]))
print(lista1[0]+lista1[1])
print(lista1[0]+str(lista1[4]))

#set-valori unice, nu sunt ordoate sau indexate, sunt imutabile - nu putem schimba locatia elementelor
#se pot adauga si sterge elemente
#len- lungime

culori = {"alb", "rosu", "verde"}
print(culori)
culori.add("gri")
print(culori)
lista = list(culori)
print(lista)
print(lista[0])

#tuple
#valorile sunt ordonate, au index, doar ca aici nu putem adauga si etrge elemente
fructe=("mere", "pere")
chrome =("dfdsvdsv", "DSAf")
yahoo = ("lola@yahoo.com", "start123")
print(fructe[0])
print(fructe.index("mere"))