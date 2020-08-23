'''
Autor: Rogerio Coelho
E-mail: rogerio.coelho@faesa.br
Repositorio: https://github.com/rogeriomcoelho/python.git
Descricao: Listas e Estruturas de Repetições. O for é utilizado quando voce sabe 
quantas repeticoes vc precisa executar.
Ja o while voce repete quantas vezes forem necessarios
'''

lista = [2, 5 , 6, 1, 8, 3,9]
#Percorre os elementos de uma lista
print("Elementos da lista:")
for elemento in lista:
    print(elemento)


print("Lista de Supermercados:")
listaSupermercado = ["arroz", "feijao", "banana", "tomate"]
for itens in listaSupermercado:
    print(itens)

#Imprime os elementos entre uma range de valores
print("Range de valores de 10 até 30:")
for i in range (10, 30):
    print(i)

saida = "n"

while saida != "s":
    n1 = float(input("Digite o primeiro numero = "))
    n2 = float(input("Digite o segundo numero = "))
    divisao = n1/n2
    print("Divisao de n1/n2 = " + str(divisao))
    saida = input("Digite s para sair do sistema ou qq outra coisa para continuar = ")


#Atencao para break. Interrompe a exercucao de repeticao
print("Exemplo for com break")
for i in range (1,6):
    if i == 3:
        break
    print(i)


#Atencao para Continue. Apenas a iteracao nao eh executada
print("Exemplo for com continue")
for i in range (1,6):
    if i == 3:
        continue
    print(i)
