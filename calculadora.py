def soma(x, y):
    resultado = x + y
    return resultado


def subtracao(x, y):
    resultado = x - y
    return resultado


def divisao(x, y):
    if x == 0 or y == 0:
        quociente = 'Pô, meu chapa. Não existe divisão por zero!'
    else:
        quociente = x / y
    return quociente


def multiplicacao(x, y):
    produto = x * y
    return produto


def receber_parametros():
    x = float(input('Digite o primeiro número: \n'))
    y = float(input('Digite o segundo número: \n'))
    return [x, y]


selecao = int(input('Digite uma opção: \n 1 - Somar \n 2 - Subtrair \n 3 - Dividir \n 4 - Multiplicar \n'))

if selecao == 1:
    parametros = receber_parametros()
    print(f'O resultado dessa bagaceira é: {soma(parametros[0], parametros[1])}')

if selecao == 2:
    parametros = receber_parametros()
    print(f'O resultado dessa bagaceira é: {subtracao(parametros[0], parametros[1])}')

if selecao == 3:
    parametros = receber_parametros()
    print(f'O resultado dessa bagaceira é: {divisao(parametros[0], parametros[1])}')

if selecao == 4:
    parametros = receber_parametros()
    print(f'O resultado dessa bagaceira é: {multiplicacao(parametros[0], parametros[1])}')
