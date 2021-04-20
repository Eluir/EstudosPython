m = 3
n = 2
p = 5

if m < 8:
    if n >= 3:
        if p <= 4:
            m = m + 3
        else:
            n = n + 5
            p = p + 5
        m = n + p

print(p + m + n)
