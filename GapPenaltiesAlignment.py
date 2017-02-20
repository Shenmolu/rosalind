import sys

def LCSBacktrack(v, w):
    global sigma
    global e
    global score

    m = len1 + 1
    n = len2 + 1

    low = [x[:] for x in [[1] * m] * n]
    mid = [x[:] for x in [[1] * m] * n]
    upr = [x[:] for x in [[1] * m] * n]
    backtrack_low = [x[:] for x in [[1] * m] * n]
    backtrack_mid = [x[:] for x in [[1] * m] * n]
    backtrack_upr = [x[:] for x in [[1] * m] * n]

    for i in range(n):
        low[i][0] = -e * i
        mid[i][0] = 0
        upr[i][0] = 0
        backtrack_upr[i][0] = 0

    for j in range(m):
        low[0][j] = 0
        mid[0][j] = 0
        upr[0][j] = -e * i
        backtrack_upr[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            i1 = low[i-1][j] - e
            i2 = mid[i-1][j] - sigma
            lo = low[i][j] = max(i1, i2)

            d1 = upr[i][j-1] - e
            d2 = mid[i][j-1] - sigma
            up = upr[i][j] = max(d1, d2)

            p = score[order[v[j-1]]][order[w[i-1]]]
            m1 = low[i][j]
            m2 = upr[i][j]
            m3 = mid[i-1][j-1] + p
            mi = mid[i][j] = max(m1, m2, m3)

            # 0 = lower-level, 1 = middle-level, 2 = upper-level
            if lo == i1:
                backtrack_low[i][j] = 0
            elif lo == i2:
                backtrack_low[i][j] = 1

            if up == d1:
                backtrack_upr[i][j] = 2
            elif up == d2:
                backtrack_upr[i][j] = 1

            if mi == m1:
                backtrack_mid[i][j] = 0
            elif mi == m2:
                backtrack_mid[i][j] = 2
            elif mi == m3:
                backtrack_mid[i][j] = 1

    backtrack = [backtrack_low, backtrack_mid, backtrack_upr]
    return(mid[-1][-1], backtrack)

def OutputLCS(backtrack, i, j):
    a = ""
    b = ""
    curLv = 1
    while i*j != 0:
        preLv = backtrack[curLv][i][j]
        if curLv == 0:
            a = '-' + a
            b = w[i-1] + b
            i -= 1
        elif curLv == 1 and preLv == 1:
            a = v[j-1] + a
            b = w[i-1] + b
            i -= 1
            j -= 1
        elif curLv == 2:
            a = v[j-1] + a
            b = '-' + b
            j -= 1
        curLv = preLv
    return a, b

if __name__ == "__main__":

    file = open(sys.argv[1], 'r')
    matrix = open(sys.argv[2], 'r')
    
    sigma = 11
    e = 1

    v = file.readline().strip()
    w = file.readline().strip()

    len1 = len(v)
    len2 = len(w)

    order = {}
    row = matrix.readline().strip().split()
    for i in range(len(row)):
        order[row[i]] = i

    score = []
    matrix = matrix.readlines()
    matrix = [row.strip().split() for row in matrix]
    for row in matrix:
        score.append([int(a) for a in row[1:]])

    s, backtrack = LCSBacktrack(v, w)
    print(s)
    a, b = OutputLCS(backtrack, len2, len1)
    print(a)
    print(b)
