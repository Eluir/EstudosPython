a = 5
b = 2
c = 5

if (a + c) > (b + 6):
    a = a + 5
    if b > 4:
        a = a + 2
    if c < 5:
        if a > 11:
            c = b + 2
        c = a + b

print(a + b + c)
