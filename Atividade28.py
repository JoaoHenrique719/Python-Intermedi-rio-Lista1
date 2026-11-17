# Peça para o usuário digitar um ano. if ano for menor que 1500: "Você encontrou dinossauros ou cavaleiros!". Elif ano menor que 2000: "Você está no século passado!"
# . elif ano igual a 2026:" Você está no presente!". else: "Você está no futuro com os carros voadores.

ano = int(input("Digite um ano para a máquina do tempo: "))

if ano <= 1500:
    print("Você está navegando junto aos colonos, voc^também sente um enjoo do mar.")

elif ano == 33:
    print("A crucificação de Cristo, ainda mais dolorosa do que foi retratado em filmes e livros.")

elif ano >= 2026 and ano <= 2100:
    print("A atualiadade, bizarro como o mundo ainda não acabou.")

elif ano >= 0:
    print("Período Jurássico, isso sim me dá medo.")