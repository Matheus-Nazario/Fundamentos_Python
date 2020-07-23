print("calculando descontos para hotel")
num_ap= int(input("Qual é a quantidade de apartamentos no hotel? \n"))
valor_ap= float(input("Qual é o valor da diária por apartamento? \n R$"))

v_por_diaria = valor_ap - ( valor_ap * ( 25/100))

print("O valor da diária com o desconto é R${}.".format(v_por_diaria))

v_final100 = num_ap *  v_por_diaria  

print("O Valor neste final de semana com 100%, ocupação é R${} ". format(v_final100))


v_final70 = num_ap * (70/100) * ( v_por_diaria )

print("O Valor neste final de semana com 70%, ocupação é R${} ". format(v_final70))

prejuizo =  valor_ap * ( 25/100) * num_ap

print("O valor que o Hotel deixará de arrecadar com o desconto é de R${}". format(prejuizo))
