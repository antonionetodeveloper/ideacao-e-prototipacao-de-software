def CelciusParaFahrenheit(temperatura):
    temperaturaConvertida = (9 * temperatura + 160) / 5
    return temperaturaConvertida


temperaturaEmCelcius = float(input("Digite a temperatura em Celcius: "))
temperaturaEmFahrenheit = CelciusParaFahrenheit(temperaturaEmCelcius)

print(f"{temperaturaEmCelcius}°C, em Fahrenheit é: {temperaturaEmFahrenheit}°F")
