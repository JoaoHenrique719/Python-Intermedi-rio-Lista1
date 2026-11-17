# Crie um sistema que une todos os temas!

senha1 = "Coisa"
senha2 = 4842
idade_min = 14
azul = "Calmo"
vermelho = "Irritado"
verde = "Animado"
Amarelo = "Feliz"
dinheiro = 50

while True:
    
    tentativa1 = input("Porteiro: Digite a senha secreta para acessar a Taverna: ")
    if tentativa1 == senha1:
        print("Porteiro: Primeira senha correta!")

        tentativa2 = int(input("Porteiro: Agora digite a segunda senha que é ainda mais secreta que a primeira: "))
        if tentativa2 == senha2:
            print("Porteiro: Segunda senha correta!")
            print("Porteiro: Bem-vindo a Taverna do Dragão Bêbado.")

        else:
            print("Porteiro: Senha incorreta, chamando a segurança.")
            break
    else:
        print("Porteiro: Segunda senha incorreta, chamando a segurança.")
        break


    idade_jogador = int(input("Bartender: Qual a idade do bravo guerreiro? "))
    if  idade_jogador <= idade_min:
        print(f"Bartender: Uma criança brincando de ser herói, se contente com o seu suquinho.")

    else:
        print("Bartender: Um nobre guerreiro experiente, tome essa poção, cortesia da casa.")

        

    sentir = input(f"* Um amuleto antigo brilha em seu peito, um vendedor suspeito no estabelecimento nota esse brilho.* Qual a cor do brilho? ")

    if sentir == azul:
        print("Vendedor: Pelo visto você é um cara paciente, que tal esse relogio que reduz a progressão do tempo? Faço por por um preço camarada para você.")
        print("O tal relogio custa 25 moedas.")
        acao = input("O herói decide levar o item?")
        if acao == "sim":
            print("O herói levou o item, e o comerciante sumiu em uma neblina de fumaça, esquisito.")
            dinheiro -= 25
            break

        else:
            print("Vendendor: Bom, é você que sai perdendo, nunca mais verá um relógio como esse.")
    elif sentir == vermelho:
        print("Vendedor: Não precisa sacar a sua espada, mas, se eu te der uma espada imbuída em chamas vermelhas? Sai por preço de banana.")
        print("A espada dos seus sonhos custa 50 moedas.")
        acao = input("O herói decide realizar o seu sonho?")
        if acao == "sim":
            print("Mais um sonho realizado, o herói sai da taverna doido para cortar algo.")
            dinheiro -= 50
            break

        else:
            print("Vendendor: Droga, vou ter que oferecer essa espada para outro herói, ela combina com o seu amuleto.")
        break

    elif sentir == verde:
        print("Vendendor: O Seu animo é contagiante, me dá até vontade de dançar, mas, e uma flauta que faz todos dançarem contigo?")
        print("A flauta custa 15 moedas.")
        acao = input("Será que uma flauta seria útil em combate? ")
        if acao == "sim":
            print("O herói chegou a uma conclusão, a flauta seria indispensável em uma luta, por isso a compra")
            dinheiro -= 15
            break

        else:
            print("Vendendor: Bom, uma demonstração para a sua ingratidão. *O vendedor misterioso tampa os ouvidos e começa a tocar, todos na taverna começam a dançar inclusive o herói." \
            " Apesar da raiva gerada em todos, eles não podem fazer nada, a não ser dançar.")
        break

    elif sentir == Amarelo:
        print(f"Vendedor: Olha só, um herói de coração puro, leve, e alegre, que tal uma agulha altruísta? Ela remove o senso de dor da pessoa espetada.")
        print("A agulha custa 10 moedas.")
        acao = input("A agulha não parece ser tão higiênica, mas vale o risco pra não levar mais dor?")
        if acao == "sim":
            print("O herói se sente imbatível, sem medo de sentir dor, e sem tempo para perder, ele parte em sua aventura com uma agulha fincada no braço.")
            dinheiro -= 10
            break

        else:
            print("Uma pessoa tão feliz e bondosa, recusando uma ofera tão generosa, mas eu não posso fazer nada.")
        break

    else:
        print("Vendedor: Não consegui interpretar a cor do seu amuleto, mas um arco de flechas infinitas é legal, não concorda?")
        print("O arco maneiro custa 100 moedas.")
        acao = print("O herói não tem condições de levar essa arma magnifíca")
        
        print("Vendendor: Se fosse mais experiente, saberia que um item como esse não se vê todo dia, mas como você tá liso...")
        break