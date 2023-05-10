def dias_para_segundos(dias):
    return dias * 24 * 60 * 60

def horas_para_segundos(horas):
    return horas * 60 * 60

def minutos_para_segundos(minutos):
    return minutos * 60


dias_trabalhados = int(input("Digite o número de dias trabalhados: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
minutos_trabalhados = float(input("Digite o número de minutos trabalhados: "))
segundos_trabalhados = float(input("Digite o número de segundos trabalhados: "))

segundos_totais = dias_para_segundos(dias_trabalhados) + horas_para_segundos(horas_trabalhadas) + minutos_para_segundos(minutos_trabalhados) + segundos_trabalhados

print(f"O total de segundos trabalhados é {segundos_totais:.2f} segundos.")
