#Faça daus perguntas 1: "Prefere atacar de longe(1) ou de perto(2)". Dentro do priumeiro if (longe), pergunte "Magia(A) ou Arco(B)?" para definir mago ou arqueiro.
#  Dentro do else (perto), pergunte "Espada(A) ou Adaga(B)?" para definir Guerreiro ou assassino.

pergunta1 = int(input("O herói vai atacar de longe(1) ou irá atacar de perto(2):"))

if pergunta1 == 1:
    pergunta2 = input("Aparentemente o herói é frágil e vai atacar a distânica, mas ele vai usar magia(A) ou um arco(B)?")

    if pergunta2 == "A":
        print("O herói é um bruxo, vamos levar ele para fogueira.")

    elif pergunta2 == "B":
        print("O herói é um arqueiro? Ninguém dá moral pra homens que preferem um arco do que uma espada.")

elif pergunta1 == 2:
    pergunta2 = input("O herói tá correndo na direção do inimigo como um louco! Ele vai usar uma espada(A), ou um par de adagas(B).")

    if pergunta2 == "A":
        print("O herói é um guerreiro com uma espada longa, lógico, nada de original nesse herói.")

    elif pergunta2 == "B":
        print("O herói é um assassino que luta com adagas, é um covarde que ataca pelas costas, um herói sem honra.")