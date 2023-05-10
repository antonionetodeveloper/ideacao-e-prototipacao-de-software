numero = int(input("Digite um número: "))

soma = 0
for n in range(1, numero + 1):
    soma += n

print(f"A soma dos números de 1 até {numero} é {soma}.")