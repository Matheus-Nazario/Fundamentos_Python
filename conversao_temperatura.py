print(" Conversão de temperatura em graus Fahrenheit para Celsius")

fah= float(input("Qual é a temperatura graus Fahrenheit? \n "))
# fah = Fahrenheit

celsius = 5*( fah - 32) / 9

print("Transformando {:.2f}°F para Celsius, fica na temperatura de {:.2f} °C".format(fah , celsius ))