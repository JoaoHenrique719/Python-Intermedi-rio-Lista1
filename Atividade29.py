# A enfinge faz uma conta matemática surpresa (ex: Quanto é 15 * 3?). Se o usuário digitar 45, ele ganha o tesouro. Senão, ele perde 50 pontos de vida.

x = 17
y = 3
valor = x * y

print(f"Esfinge: Resolva o seguinte enigma... Quanto é {x} vezes {y}? ")
resposta =int(input("Jogador: A resposta é "))

if resposta == valor:
    print("Esfinge: Resposta correta, pegue esse báu e saia da masmorra!")

else:
    print("* A esfinge ataca cruelmente, removendo o escudo e causando 50 pontos de dano. *")