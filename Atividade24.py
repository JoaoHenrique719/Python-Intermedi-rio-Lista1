#Pergunte ao usuário uma cor (Azul, Amarelo, Vermelho). O sistema deve responder como ele está se sentindo usando elif (Ex: Azul = Calmo, Vermelho = Zangado).

azul = "Calmo"
vermelho = "Irritado"
verde = "Animado"
Amarelo = "Feliz"

sentir = input("Como você está hoje? Se expresse com cores!")

if sentir == azul:
    print(f"Você está {azul}.")

elif sentir == vermelho:
    print(f"O que aconteceu pra você estr {vermelho}?")

elif sentir == verde:
    print(f"Por que você está tão {verde} hoje?")

elif sentir == Amarelo:
    print(f"Que bom que você está {Amarelo}!")

else:
    print("Desculpa, não entendi essa cor.")