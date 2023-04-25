def FahrenheitParaCelsius(temperatura):
    temperaturaConvertida = ((temperatura - 32) * 5) / 9
    return temperaturaConvertida


temperaturaEmFahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temperaturaEmCelsius = FahrenheitParaCelsius(temperaturaEmFahrenheit)

print(f"{temperaturaEmFahrenheit}°F, em Celsius é: {temperaturaEmCelsius}°C")
