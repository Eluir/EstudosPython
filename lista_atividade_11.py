m = 5
n = 8
p = 2

if m < 8:
    if n >= 1:
        if p <= 5:
            m = m + 8
        else:
            n = n + 1
            p = p + 3
        m = m + p
    p = n + m
print(p + m + n)
