valor_conta = float (input("Qual é o valor da conta? \n R$ "))

carlos = valor_conta // 3
andre = valor_conta // 3
amigos=  valor_conta - (carlos + andre)
felipe = amigos

print("O Carlos vai pagar R$ {}, o André R${} e o Felipe R${}.".format(carlos , andre, felipe))