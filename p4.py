'''
Autor: Rogerio Coelho
E-mail: rogerio.coelho@faesa.br
Repositorio: https://github.com/rogeriomcoelho/python.git
Descricao: Apresentação do condicional if e Operadores Lógicos: and, or, not.
'''

nome = input("Digite o seu nome = ")
sexo = input("Digite seu sexo (M/F) = ")
idade = int(input("Digite sua idade = "))

print("Nome = " + nome)

#if simples
if (sexo == 'M'):
    print("Seu sexo eh Masculino!")
else:
    print("Seu sexo eh Feminino!")

#if com varias condicoes
if (idade < 16):
    print("Voce eh menor idade!")
    print("Não pode votar!")
elif ( (idade < 18) or (idade > 65)):
    print("Você não precisa votar!\n")
else:
    print("Você é Obrigado votar!")

print("Fim do programa!")

