'''
Autor: Rogerio Coelho
E-mail: rogerio.coelho@faesa.br
Repositorio: https://github.com/rogeriomcoelho/python.git
Descricao: Explicar o funcionamento de Listas e operações basicas de listas
'''

lista = [5, 6, 7, 8]
print(lista)

#imprime o elemento na posicao 3, lembrando que comeca 0
print(lista[2])

# Tamanho da lista use a funcao len()
print(len(lista))

lista.append(10)
print("Nova lista apos adicionar o 10 no final = " + str(lista))

posicao, valor = 0, 20
lista.insert(posicao,valor)
print("Nova lista apos adicionar o 20 na primeira posicao = " + str(lista))

#Eliminar o elemento 5 da lista
lista.remove(5)
print("Lista sem o elemento 5 = " + str(lista))

print("Posicao do elemento 8 na Lista = " + str(lista.index(8)))

#Para ordenar uma lista utilize o comando sort
lista.sort()
print("Lista ordernada do menor ao maior = " + str(lista))

lista.reverse()
print("Lista ordernada do maior ao menor = " + str(lista))

