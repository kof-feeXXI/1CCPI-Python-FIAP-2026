lista_frutas = ["Maçã", "Banana", "Pêssego"]

# Lista_frutas[0] = "Maçã"
# Lista_frutas[1] = "Banana"
# Lista_frutas[2] = "Pêssego"
print(lista_frutas[0])

lista_frutas.append("Uva")
print(lista_frutas)
# Lista_frutas[3] = "Uva"

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)