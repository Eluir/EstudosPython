K = 4
M = 1
H = 8
K = K + 2
M = M + K

if K < 2:
    K = K + 6
    M = K + 6
else:
    H = H + 2
    M = 2
H = 7
K = K + 4 - 3
M = M + 1 - 1

print(K + M + H)
