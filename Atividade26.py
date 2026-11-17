# Pergunte a velocidade do carro (número). Se for menor ou igual a 80, "Siga em paz". Se for entre 81 e 100, "Multa leve de 50 moedas". Se for maior que 100, "Multa gravíssima de 200 moedas e carro apreendido!". 

velocidade = int(input("Então Guarda 2, qual a velocidade do meliante? "))

if velocidade >= 80:
    print("Siga em paz cidadão.")

elif velocidade < 80:
    print("O meliante ultrapassou o limite de velocidade, multa de 50 moedas e você está livre pra ir.")

elif velocidade < 100:
    print(f"Você chegou a {velocidade} km, guarda 2, apreenda o carro , a multa será de 200 moedas.")