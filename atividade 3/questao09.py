capacidade_maxima = float(input("Digite a capacidade máxima do elevador: "))

peso_pessoa1 = float(input("Digite o peso da primeira pessoa: "))
peso_pessoa2 = float(input("Digite o peso da segunda pessoa: "))
peso_pessoa3 = float(input("Digite o peso da terceira pessoa: "))
peso_pessoa4 = float(input("Digite o peso da quarta pessoa: "))
peso_pessoa5 = float(input("Digite o peso da quinta pessoa: "))

peso_total = peso_pessoa1 + peso_pessoa2 + peso_pessoa3 + peso_pessoa4 + peso_pessoa5

if peso_total > capacidade_maxima:
    print("O elevador está sobrecarregado.")

else:
    print("Liberado para subir.")