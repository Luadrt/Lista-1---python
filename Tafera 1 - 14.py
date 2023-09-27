peso_peixes = float(input("Digite o peso dos peixes em quilos: "))

limite_peso = 50.0

if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    
    multa = excesso * 4.0
    
    print(f"Peso dos peixes: {peso_peixes:.2f} kg")
    print(f"Limite de peso: {limite_peso} kg")
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a ser paga: R$ {multa:.2f}")
else:
    print(f"Peso dos peixes: {peso_peixes:.2f} kg")
    print(f"Você não excedeu o limite de peso. Não há multa a ser paga.")
