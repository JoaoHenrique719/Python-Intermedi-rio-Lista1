# Melhore o exercício anterior. Adicione um else poderoso no final para o caso de o usuário digitar "5" ou qualquer letra errada, fazendo o chápeu responder: "Hmm, escolha inválida. O chápeu está confuso!"

print("Escolha apenas 1:\n" \
"1 - Livros\n" \
"2 - Esportes\n" \
"3 - Natureza\n" \
"4 - Pegadinhas\n")

resposta = int(input("Qual a sua resposta:"))

if resposta == 1:
    print("A sua casa será Corvinal.")

elif resposta == 2:
    print(" A sua casa é Grifnória.")

elif resposta == 3:
    print("A sua casa é Lufa-Lufa.")

elif resposta == 4:
    print("A sua casa é Sonserina.")

else:
    print("Muito engraçadinho, você vai para o ármario de limpeza.")