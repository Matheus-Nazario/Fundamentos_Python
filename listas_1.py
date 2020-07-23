lista = [] 
   
n = int(input("informa ")) 
  
for i in range(0, 3): 
    ele = int(input()) 
    lista.append(ele)
    
print(lista)

maior = max(lista)
print(maior)

menor = min(lista)
print(menor)

media = sum(lista) / len(lista)
print(media)

for i in lista:
    if i < media:
        print(i)