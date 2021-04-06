nome = input('Qual seu nome?\n')
idade = int(input('Qual sua idade?\n'))

print('Você é um (a):')

if idade <= 12:
    print('Criança')
elif idade > 12 and idade <= 25:
    print('Jovem')
elif idade > 25 and idade <= 50:
    print('Adulto')
elif idade > 50 and idade <= 100:
    print('Idoso')
else:
    print('Centenário')
