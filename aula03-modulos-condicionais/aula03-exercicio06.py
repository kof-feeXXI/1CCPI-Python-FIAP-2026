# EXERCÍCIO 6:
# ▪ Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações
# matemáticas (+, -, *, /)
# ▪ O programa deve calcular o valor final de acordo com a operação selecionada.
# ▪ Ou seja, se a entrada for 5, 6 e *, então seu programa dever mostrar 30

A = float(input("Digite o primeiro número: "))
B = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {A + B}")
elif op == "-":
    print(f"Resultado: {A - B}")
elif op == "*":
    print(f"Resultado: {A * B}")
elif op == "/":
    if B == 0:
        print("Erro: divisão por zero!")
    else:
        print(f"Resultado: {A / B}")
else:
    print("Operação inválida!")