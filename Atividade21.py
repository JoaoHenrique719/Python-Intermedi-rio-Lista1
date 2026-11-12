#Faça  uma pergunta: "Você prefere: 1-livros, 2-esportes, 3-natureza, 4-pegadinhas". Use if/elif/else para sortear o aluno em uma das 4 casa da escola de magia (ex: Corvinal, Grifnória, lufa-lufa, Sonserina).

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