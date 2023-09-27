print('Calculadora Estranha')
num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

resultado1 = (2 * num_int1) * (num_int2 / 2)

resultado2 = (3 * num_int1) + num_real

resultado3 = num_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"O terceiro elevado ao cubo é: {resultado3}")