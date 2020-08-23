'''
Autor: Rogerio Coelho
E-mail: rogerio.coelho@faesa.br
Repositorio: https://github.com/rogeriomcoelho/python.git
Descricao: Receber as tres notas de um aluno e calcular a media. Se nota > 7, 
aprovado. Caso contrário, Prova Final.
'''

nota1 = input("Digite a nota 1 = ")
nota2 = input("Digite a nota 2 = ")
nota3 = input("Digite a nota 3 = ")

#atencao para conversao de str para float.
soma = float(nota1) + float(nota2) + float(nota3)
media = soma / 3.0

#atencao para conversao de float para str
print("Media = " + str(media))

if (media >= 7.0):
    print("Aprovado")
else:
    print("Prova Final")

