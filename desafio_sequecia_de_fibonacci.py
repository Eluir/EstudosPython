num = int(input('Digite quantos números da sequência de Fibonacci você quer: \n'))

f1 = 0
f2 = 1
count = 0

while count < num:
    f3 = f1 + f2
    print(f3)
    f1 = f2
    f2 = f3
    count += 1
print('Acabou-se')
