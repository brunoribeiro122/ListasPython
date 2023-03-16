#Criando uma lista
minha_lista = [1,2,3,4,5]

#Usando um loop for para percorrer a lista e imprimir cade elemento

for i in range(len(minha_lista)):#O len define a quantidade de itens que tem na minha lista, entao o for vai estar no range até 5
    print('O elemento', i+1, 'da lista é', minha_lista[i])

#Criando uma lista de números 
numeros = [1,2,3,4,5]
#Usando um loop for para percorrer a lista e imprimir cada elemento
for numero in numeros:
    print(numero, ' -Com for')
#Usando um loop while para percorrer a lista e imprimir cade elemento 
i = 0 
while i < len(numeros):
    print(numeros[i],'= Com While')
    i += 1

#PARA APAGAR ELEMNENTOS DA LISTA PODE SER USADO O COMANDO del:
print(numeros)
del numeros[0]
print(len(numeros))
print(numeros)

#Usando um indice negativo eu consigo fazer com que a lista seja 'varrida' ao contrario por exemplo
# numeros[-1] sera o ultimo numero da lista
listanova = [1,2,3,4,5,6,7,8,9,0,12,42,45,55]
print(listanova[-1])