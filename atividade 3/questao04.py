def RendimentoPorDiaUtil(valor_inicial, dias):
    rendimento = 0.02 # 2% de rendimento
    rendimento_por_dia = valor_inicial * rendimento
    rendimento_final = rendimento_por_dia * dias

    return rendimento_final


investimento_inicial = 1000
semanas_investidas = int(input("Digite quantas semanas você investiu: "))
dias_investidos = semanas_investidas * 5 # 5 dias úteis por semana

rendimento_final = RendimentoPorDiaUtil(investimento_inicial, dias_investidos)

print(f"{investimento_inicial} investidos por {dias_investidos} dias úteis, com rendimento de 2% ao dia, resulta em {rendimento_final:.2f} de rendimento final.")