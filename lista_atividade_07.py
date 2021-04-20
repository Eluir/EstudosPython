a = 5
b = 5
c = 1
d = 3
if a > 1 and b <= 3:
    if c < d:
        c = c + 1
    else:
        d = d + 3
else:
    if c > 7 or d < 5:
        c = c * 2

print((a + b + c) - d)
