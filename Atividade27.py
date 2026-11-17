#Peça as notas de duas provas. Calcule a média. Se a média for >= 7, Aprovado. Se for >5 e <7, recuperação. Se for < 5, Reprovado. Mostre a média e o veredeito.

nota1 = int(input("Qual a nota da primeira prova: "))
nota2 = int(input("Qual a nota da segunda prova: "))

media = (nota1 + nota2) / 2


if media > 10:
    print("Houve um erro na coleta dos dados, coloque o valor correto.")
elif media >= 7:
    print(f"Parábens o aluno foi aprovado com {media} de média.")
elif media >= 5 and media > 7:
    print(f"O aluno ficou de recuperação com média de {media}.")

else:
    print(f"O aluno reprovou na matéria com média de {media}.")