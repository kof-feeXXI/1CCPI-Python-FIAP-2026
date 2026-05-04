# Atividade 1: Duplas – Repetições encadeadas
#   ▪ Dado um conjunto de nomes de quatro pessoas, escreva um algoritmo que imprima todas as possíveis
#     duplas que podem ser formadas.
#   ▪ Primeiro, crie um vetor e coloque quatro nomes nele.
#   ▪ A seguir, exiba as possíveis duplas.

# dupla[0] = Ana Lara
# dupla[1] = Ana Luiz
# dupla[2] = Ana Caio
# dupla[3] = Lara Luiz
# dupla[4] = Lara Caio
# dupla[5] = Luiz Caio

# --- --- --- --- ---

nomes = ["Ana", "Lara", "Luiz", "Caio"]

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(nomes[i], nomes[j])

#   ✔   Corrigido!   ✔
