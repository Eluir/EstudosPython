nome = input('Qual seu nome?\n')
idade = int(input('Qual sua idade?\n'))

if idade >= 0 and idade <= 12:
    print('Criança')
else:
    if idade > 12 and idade <= 60:
        print('Adulto')
    else:
        if idade > 60 and idade <= 100:
            print('Idoso')
        else:
            print('Centenário')
