#Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. 
# Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:
#- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
#- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
#- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.
#No sistema, todos os valores devem estar armazenados em variáveis.
print("Bem vindo! saiba se foi aprovado!")
nome = str (input ("qual e seu nome?"))
nota1 = int (input ("qual e a primeira nota?"))
nota2 = int (input ("qual e a segunda nota?"))
faltas = int (input ("quantas faltas vc teve no mes?"))
somanota = int (nota1+nota2)
medianota = int (somanota /2)
print ("media:",medianota,"faltas:",faltas)

if faltas >=3:
    print("ola",nome,"voce foi reprovado por falta")
else:
    if medianota<7:
        print('ola',nome, 'voce foi reprovado por nota')
    else: 
        print ('ola',nome,"voce foi aprovado")