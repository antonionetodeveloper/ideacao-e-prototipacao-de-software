def HorasParaMinutos(horas):
    return horas * 60


def MinutosParaSegundos(minutos):
    return minutos * 60


tempo_de_prova = float(input("Digite o tempo que você levou para terminar a prova em horas: "))

tempo_de_prova_em_minutos = HorasParaMinutos(tempo_de_prova)
tempo_de_prova_em_segundos = MinutosParaSegundos(tempo_de_prova_em_minutos)

print("O tempo que você levou para terminar a prova em segundos foi: ", tempo_de_prova_em_segundos, "s")
