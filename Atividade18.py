#Peça o valor do tesouro do herói. Se o tesouro for maior que 1000 moeas, o rei cobra uma taxa de 10% (calcule a matemática e mostre o desconto). Se for menor ou igual a 1000, o herói não paga imposto.

tesouro = int(input("Quantas moedas tem no báu?"))

if tesouro >= 1000:
    imposto = tesouro / 10

    print(f"O Rei cobra imposto sobre o seu tesouro, o imposto é de {imposto} moedas.")
    tesouro -= imposto

    print(f"Ainda lhe restam {tesouro} moedas.")