# Mostre um menu com 3 poções e preços diferentes. Peça para o usuário digitar 1, 2 ou 3. Use if/elif/else para calcular o valor da compra baseado na escolha.

pocao_dano = 50
pocao_cura = 100
pocao_estamina = 30
moedas = 200

print(f"1 - Poção de dano está por {pocao_dano} moedas")
print(f"2 - Poção de cura está por {pocao_cura} moedas")
print(f"3 - Poção de estamina está por {pocao_estamina} moedas")
escolha = int(input("Você tem 200 moedas. Qual poção deseja comprar:"))

if escolha == 1:
    moedas -= pocao_dano

    print(f"Uma poção de dano foi adicionada ao inventário. Você tem {moedas} moedas.")

elif escolha == 2:
    moedas -= pocao_cura

    print(f"Uma poção de cura foi adicionada ao inventário. Você tem {moedas} moedas.")

elif escolha == 3:
    moedas -= pocao_estamina
    print(f"Uma poção de estamina foi adicionada ao inventário. Você tem {moedas} moedas.")


else:
    print("Escolha uma opção válida.")