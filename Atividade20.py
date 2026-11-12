# Crie um sistema onde o usuário informa o dinheiro que tem e escolhe Lanche (R$ 15), Suco (R$ 8), ou Combo (20$). O sistema deve usar o elif para identificar a escolha,
#  verificar se o dinheiro dá para pagar, e liberar ou negar a venda.

lanche = 15
suco = 8
combo = 20

print("Menu:")
print("1 - Lanche: 15 reais")
print("2 - Suco: 8 reais")
print("3 - Combo: 20 reais")
reais = int(input("Quantos reais será que eu tenho na carteira?"))

escolha = int(input(f"Ótimo, eu tenho {reais} reais, o que eu vou escolher?"))
if reais >= 8:
    if escolha == 1:
        if reais < lanche:

            print("Não tenho dinheiro pro meu lanche.")

        else:
            reais -= lanche

            print(f"O lanche estava ótimo, mas eu devia ter pedido o suco pra acompanhar, bom, eu só tenho {reais} reais na carteira.")

    elif escolha == 2:
         
        reais -= suco

        print(f"O suco estava ótimo, mas sem o lanche eu não vou aguentar a fome por muito tempo, bem, eu ainda tenho {reais} reais comigo.")

    elif escolha == 3:

        if reais < combo:
            print("Não tenho dinheiro pra comprar o combo, talvez só um dos dois?")

        else:
    
             reais -= combo

             print(f"Perfeito, e ainda tenho {reais} reais pra gastar.")

    else:
        print("Quer saber? Não estou com tanta fome assim.")

else:
    print("Nop, muito caro pro meu orçamento.")