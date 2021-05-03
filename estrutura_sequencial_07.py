num = int(input('Insira a medida do quadrado para saber sua área: \n'))
pergunta = int(input('O valor informado está em CM ou M? Digite: \n 1 - CM \n 2 - M \n'))

a = (num ** 2) * 2

if pergunta == 1:
    print(f'O dobro da área do quadrado é: {a} cm²')
if pergunta == 2:
    print(f'O dobro da área do quadrado é: {a} m²')
