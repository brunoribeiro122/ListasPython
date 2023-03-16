#Criando uma lista de números
numeros = [10,20,30,40,50,9,600,60]
#Usando a função sum() para somar os elementos na lista
soma = sum(numeros)

#Imprimindo o resultado
print('A soma dos números na lista é:', soma)

#Encontrar o maior numero da lista
maior_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
print('O maior numero é:',maior_numero)

#Ou exemplo de soma usando a variavel ao inves do sun()
minha_lista = [10,1,8,3,5,2,12,34,53,65,77,4,33,88,95]
total = 0
for i in range(len(minha_lista)):
    total += minha_lista[i] #Neste caso a variavel total é zero, e nesta condiçao enquanto I for estiver no range do indice que o comando len vai indicar, e o programa vai somar total = total + minha_lista ou seja, somar todos os elemento
    # e armazenar o resultado na variavel total
    #No primeiro loop for utilizando a função range(len(minha_lista)), a variável i percorre todos os índices da lista minha_lista. Em cada repetição, o valor correspondente àquele índice é somado à variável total.
    
print('A soma de todos os elementos da lista é',total)
#No segundo loop for, a variável u percorre todos os elementos da lista minha_lista. Em cada repetição, o elemento correspondente é somado à variável total1.
total1 = 0
for u in minha_lista:
    total1 += u
print('A soma de todos os elementos da lista é',total1)