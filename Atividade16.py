#Pergunte o valor da mesada guardada e o preço de um jogo que o aluno quer. Se o valor for suficiente, calcule e mostre o troco. Senã, diga exatamente quanto dinheiro falta.
cofre = int(input("Quantos reais você tem no cofre?"))

if cofre >= 1200:
    cofre = cofre - 1200
    print(f"Já podemos comprar o foguete! E vamos ter {cofre} reais de troco.")

else:

    cofre = 1200 - cofre
    print(f"Falta pouco, ainda restam {cofre} reais para comprarmos o foguete.")