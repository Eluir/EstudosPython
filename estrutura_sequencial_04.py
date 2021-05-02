nota1 = float(input('Informe a nota do primeiro bimestre: \n'))
nota2 = float(input('Informe a nota do segundo bimestre: \n'))
nota3 = float(input('Informe a nota do terceiro bimestre: \n'))
nota4 = float(input('Informe a nota do quarto bimestre: \n'))


# perguntar pro creiso como fazer a contágem pra deixar a média dinamica
def media(a, b, c, d):
    resultado = (a + b + c + d) / 4
    return resultado


print(f'Sua média final é: {media(nota1, nota2, nota3, nota4)}')
