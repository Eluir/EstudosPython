a = 6
b = 2
c = 4
d = 1

if a > 5 and b <= 2:
    if c < d:
        c = c + 1
    else:
        d = d + 3
else:
    if c > 2 or d < 4:
        c = c * 2

print(((a + b + c) - d))
