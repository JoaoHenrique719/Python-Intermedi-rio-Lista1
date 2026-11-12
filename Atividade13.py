#Crie um sistema bancário. Primeiro, ele pede a senha de letras. Se acertar, ele pede o PIN de 4 números. Só imprima "Acesso ao Cofre liberado" se ele acertar as duas coisas.
senha1 = "Coisa"
senha2 = 4842

tentativa1 = input("Digite a primeira senha do cofre:")

if tentativa1 == senha1:
    print("Primeira senha correta!")
    tentativa2 = int(input("Digite a segunda senha:"))

    if tentativa2 == senha2:
        print("Segunda senha correta")
        print("O cofre está aberto.")

    else:
        print("Senha incorreta, chamando a segurança.")

else:
    print("Senha incorreta, chamando a segurança.")
