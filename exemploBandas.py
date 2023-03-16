#etapa 1: criando lista chamada banda
banda = []
#etapa 2: adicionando os membros da banda
banda.append('John Lennon')
banda.append('Paul McCartney')#Ele adiciona os membros da banda na lista
banda.append('George Harrison')
print('Etapa 2:', banda)
#etapa 3
for member in range(2):
    banda.append(input('Novo membro:'))#Aqui o programa faz um input de 2 novos membros para banda usando o banda.append(input)
print('etapa 3:', banda)
#etapa 4:
del banda[-1]#Aqui o programa exclui os 2 ultimos membros da banda(lista)
del banda[-1]
print('etapa 4', banda)
#etapa 5:
banda.insert(0, 'ringostarr')
print('etapa 5:,', banda)# Nesta etapa o programa adiciona outro membro sem usar o input, apenas usando o insert
print('The Fab:', len(banda))

