#O clube secreto aceita todo mundo, exceto quem se chamar "Voldemort". Pergunte o nome e use o operador de diferença (!+) para barrar o vilão e liberar os outros.

nome = input("Seja bem vindo ao clube secreto, qual o seu codinome??")

if nome != "Voldemort":
    print(f"Seja bem vindo caro{nome}")

else:
    print("Você não é bem vindo aqui.")