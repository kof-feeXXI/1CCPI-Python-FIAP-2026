# EXERCÍCIO 3:
# ▪ Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é o maior número.")
elif num2 > num1:
    print(f"O número {num2} é o maior número.")
else:
    print("Os números são iguais.")