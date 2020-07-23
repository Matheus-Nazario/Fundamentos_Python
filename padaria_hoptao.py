print("Padaria Hoptão")

pao = int(input("Qual é a quantidade que vendeu por dia de pães? "))

valor_pao= pao * 0.12

broa = int(input("Qual é a quantidade que vendeu por dia de broas? "))

valor_broa = broa * 1.50

lucro = valor_pao + valor_broa * (10/100)

print("O valor de 10%, do total arrecadado é {}.".format(lucro))


