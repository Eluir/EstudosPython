raio = int(input('Qual o raio da circunferência que deseja calcular a área? \n'))

pergunta = input('O número informado é em CM ou M?\n Digite: \n 1 - CM\n 2 - M\n')

pi = 3.14

a = pi * raio ** 2

if pergunta == 1:
    print(f'A área deste círculo é {a}cm. ')
else:
    print(f'A área deste círculo é: {a}m ')
