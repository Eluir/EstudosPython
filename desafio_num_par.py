num = int(input('Informe um número aí meu chapa!\n'))
count = 0
sum = 0

while num >= count:
    if count % 2 == 0:
        sum += count
    count += 1

print(f'A quantidade de números pares é: {sum}')
