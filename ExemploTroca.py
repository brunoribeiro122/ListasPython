minha_lista = [17,8,10,6,2,4] #lista para ordenar
trocado = True #precisamos do true para entrar no loop while
while trocado:
    trocado = False #Sem trocas até agora
    for i in range(len(minha_lista) - 1):
        if minha_lista[i] > minha_lista[i+1]:
            trocado = True #Ocorreu uma troca
            minha_lista[i],minha_lista[i+1] = minha_lista[i+1],minha_lista[i]
print(minha_lista)

#Este é um algoritmo de ordenação chamado Bubble Sort, que percorre a lista várias vezes, comparando cada par de elementos adjacentes e trocando-os de lugar se eles estiverem na ordem errada.
#O código começa com uma lista desordenada minha_lista e uma variável booleana trocado que é inicializada como True. Em seguida, entra em um loop while que só termina quando nenhuma troca é feita durante a passagem pela lista.
#Dentro do loop, a variável trocado é definida como False no início de cada passagem. Em seguida, o loop for percorre a lista minha_lista com a função range(len(minha_lista) - 1), verificando se cada par de elementos adjacentes está na ordem correta. Se um elemento estiver fora de ordem, é trocado com o elemento adjacente e a variável trocado é definida como True.
#Se a variável trocado permanecer como False após uma passagem completa pela lista, o loop while é interrompido e a lista finalmente ordenada é impressa na tela com o comando print(minha_lista).
#Este algoritmo é fácil de entender, mas pode ser ineficiente em listas grandes, pois pode levar muitas passagens para ordenar completamente a lista. Existem outros algoritmos de ordenação mais eficientes para listas maiores.
