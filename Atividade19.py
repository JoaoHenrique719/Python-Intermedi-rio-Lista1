#O pai deu a mesada, mas perguntou! "Você tirou nota A em matemática?" se a resposta for "sim", a mesada recebe um bonûs de 20 moedas. Se for "não", recebe apenas o valor normal. Imprima o total final.

print("Pai: A sua mesada de 100 reais está aqui.")
print("Pai: Você tirou 10 em matemática?")

resposta = input("Filho: ")
resposta.lower

if resposta == "sim":
    print("Pai: Boa garoto, toma mais 20 reais.")

elif resposta == "não":
    print("Pai: ok.")

else: 
    print("Não respondeu a minha pergunta.")