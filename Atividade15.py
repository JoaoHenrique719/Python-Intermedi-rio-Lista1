#Peça a senha secreta. Adicione um elif para testar se o usuário digitou a senha certa, mas toda em MAIÚSCULAS, e imprima um aviso:"Quase! Mas você gritou a senha (Caps Lock). Tente em minúsculas."

senha = "galinha"

senha1 = input("Qual a senha secreta?")

if senha1 == senha:
    print("A senha está correta, seja bem vindo.")

elif senha1 == "GALINHA":
    print("Qual a necessidade de gritar? (Caps Lock), tenta falar mais baixo, por favor (minúsculas).")

else:
    print("Senha incorreta")