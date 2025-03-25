# LEIA DO TECLADO A TEMPERATURA EM CELSIUS E IMPRIMA O EQUIVALENTE EM FAHRENHEIT.

TempCelsius = float(input("Digite a temperatura em graus Celsius: "))

TempFahrenheit = (TempCelsius * (9/5)) + 32

print(f"A temperatura em fahrenheit é: , {TempFahrenheit: 2f}")