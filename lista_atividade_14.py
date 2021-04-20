a = 1
b = 8
c = 5

if a + c > b + 6:
    a = a + 5
    if b > 4:
        a = a + 2
    if c < 6:
        if a > 11:
            c = c + 2
        c = a + b
print(a+b+c)
