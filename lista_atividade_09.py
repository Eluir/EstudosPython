g = 6
b = 4
f = 7 + 2

if g > b or f < 12:
    if b >= 3:
        f = f + 2
    f = f + 3
if g <= 5:
    if b + 2 > 6 and f > 3:
        b = b + 2
g = g + 1

print(g + b + (2 * f))
