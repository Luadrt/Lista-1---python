altura = float(input("Digite sua altura em metros: "))

sexo = input("Digite seu sexo (M para masculino, F para feminino): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
    exit(1)

print(f"Seu peso ideal é aproximadamente {peso_ideal:.2f} kg")
