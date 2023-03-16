#Criando uma lista com elementos duplicados 
lista_com_duplicatas = [1,2,3,1,4,2,5,6,3,7,8,5,9]
#Iniciando uma lista vazia para armazenar os elementos únicos
lista_sem_duplicatas = []

#Usando um loop while para percorrer a lista e remover os elemnetos duplicados
while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) #pop é um comando usado para remover o elemnto da lista
    if elemento not in lista_sem_duplicatas:#not in significa que NAO ESTA PRESENTE então ele verifica na lista inteira onde o elemento nao esta presente para adiciona-lo usando o .append
        lista_sem_duplicatas.append(elemento)
#Imprimindo o resultado
print('A lista de duplicatas é', lista_sem_duplicatas)