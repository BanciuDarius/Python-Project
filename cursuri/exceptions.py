#exceptie - o eroare , ceva ce nu poate sa faca codul si il opreste din executie

# lista = [1,2,3,4,5]
# print(lista[6])

#in try punem codul periculos
try:
    lista = [1, 2, 3, 4, 5]
    print(lista[6])
#punem numele erorii ce ne apare
except IndexError as error:
    print("ai o pozitie mai mare decat lungimea listei")

numar = int(input("da un numar"))
if numar > 30:
    raise IndexError("Limita elivilor e 30")