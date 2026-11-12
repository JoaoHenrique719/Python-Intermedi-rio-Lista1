#Pergunte a idade do usuário. Se for maior ou igual a 14 diga "Bem-vindo à equipe avançada!". Senão, diga "Faltam X anos para você entrar na equipe avançada!".

idade_min = 14

idade_jogador = int(input("Qual a idade do jogador?"))
if  idade_jogador <= idade_min:

    resto = idade_min - idade_jogador
    print(f"Ainda faltam {resto} anos para você poder entrar na Guilda avançada.")

else:
    print("Seja bem vindo a Guilda Avançada.")