from math import sqrt

def Bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return f"Não há raízes reais, pois o delta é {delta:.2f}."
    
    elif delta == 0:
        x = -b / (2 * a)
        return x

    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return x1, x2


primeiro_valor = float(input("Digite o valor de a: "))
segundo_valor = float(input("Digite o valor de b: "))
terceiro_valor = float(input("Digite o valor de c: "))

resultado = Bhaskara(primeiro_valor, segundo_valor, terceiro_valor)

if type(resultado) == tuple:
    print(f"As raízes da equação são {resultado[0]:.2f} e {resultado[1]:.2f}.")

elif type(resultado) == float or type(resultado) == int:
    print(f"A raiz da equação é {resultado}.")

else:
    print(resultado)