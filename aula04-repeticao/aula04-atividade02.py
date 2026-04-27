def verificador_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite novamente a 1a nota: "))
    return nota

notaA = float(input("Digite a 1a nota: "))
notaA = verificador_nota(notaA)

notaB = float(input("Digite a 2a nota: "))
notaB = verificador_nota(notaB)

media = (notaA + notaB) / 2
print(media)