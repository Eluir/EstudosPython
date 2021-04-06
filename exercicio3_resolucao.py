nome = str(input('Qual seu nome?\n'))
nota1 = int((input('Qual sua nota do 1º bimestre?\n')))
nota2 = int(input('Qual sua nota do 2º bimestre?\n'))
nota3 = int(input('Qual sua nota do 3º bimestre?\n'))
nota4 = int(input('Qual sua nota do 4º bimestre?\n'))
soma_notas = ((nota1 + nota2 + nota3 + nota4) / 4)

if soma_notas <= 40:
    print('Reprovado')
elif soma_notas > 40 and soma_notas <= 60:
    print('Recuperação')
elif soma_notas > 60 and soma_notas <= 100:
    print('Aprovado')


#Perguntar como faz pra usar o resultado do if em um print adicionando um texto