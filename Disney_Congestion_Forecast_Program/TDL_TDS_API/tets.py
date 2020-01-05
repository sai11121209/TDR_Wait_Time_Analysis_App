
H = 4
M = 45
for i in range(1000):
    if (7<=H<=22):
        if (7==H):
            if (45<=M):
                pass
        if (22==H):
            if (0>=M):
                pass
    print(str(H)+':'+str(M))
    M = M + 1
    if (M%60==0):
        H = H + 1
        M = 0 