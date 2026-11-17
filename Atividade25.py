#Pergunte a idade do aluno e se ele prefere gatos ou cachorros. Crie 4 respostas combinando os dados (Ex: "Jovem e prefere gatos, "Adulto e prefere cachorros.)

idade = int(input("Qual a sua idade? "))
animal = input("Você prefere gatos ou cachorros? ")

if idade <= 10:
    idade2 = "criança"

elif idade > 17:
    idade2 = "adulto"

elif idade >10:
    idade2 = "adolescente"


if animal == "cachorro":
    print(f"O aluno é um {idade2} e prefere cachorro.")

elif animal == "gato":
    print(f"O aluno é um {idade2} e prefere gato.")