minha_lista = []
trocado = True
num = int(input('Quantos elementos deseja ?')) #Nesta parte o usuario digita quantos elementos ele deseja na lista

for i in range(num):
    val = float(input('Entre com o número: '))#Nesta parte o usuario digita os elementos que ele deseja na lista conforme o numero de elementos que ele digitou antes
    minha_lista.append(val)

while trocado:
    trocado = False
    for i in range(len(minha_lista) - 1):
        if minha_lista[i] > minha_lista[i+1]:
            trocado = True
            minha_lista[i], minha_lista[i + 1] = minha_lista[i+1], minha_lista[1]
print('\nOrdenado:')
print(minha_lista)