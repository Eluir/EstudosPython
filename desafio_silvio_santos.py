num = int(input('Diginte um número: \n'))
countPIM = 0

for x in range(1, num, 1):
    if x % 4 == 0:
        print('PIM')
        countPIM += 1
    if x % 4 != 0:
        print(f'{x}')
print(f'Quantidade de vezes que o PIM apareceu: {countPIM}')

print('Acabou-se')
