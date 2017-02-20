import sys

def LCSbacktrack(v, w):
    m = len(v) + 1
    n = len(w) + 1

    s = [x[:] for x in [[0] * m] * n]
    backtrack = [x[:] for x in [[1] * m] * n]

    for i in range(n):
        s[i][0]= 0
        backtrack[i][0] = 1

    for j in range(m):
        s[0][j] = 0
        backtrack[0][j] = 2

    for i in range(1, n):
        for j in range(1, m):
            f = 1 if v[j-1] == w[i-1] else -2
            opt1 = s[i-1][j] - 2
            opt2 = s[i][j-1] - 2
            opt3 = s[i-1][j-1] + f
            s[i][j] = max(opt1, opt2, opt3)

            if s[i][j] == opt1:
                backtrack[i][j] = 1
            if s[i][j] == opt2:
                backtrack[i][j] = 2
            if s[i][j] == opt3:
                backtrack[i][j] = 3

    maximum = 0
    maxI = 0
    for i in range(n):
        if(s[i][j] > maximum):
            maxI = i
            maximum = s[i][j]

    return maximum, maxI, backtrack

def constructAligm(backtrack, v, w, maxI):
    i = maxI
    j = len(v)
    a = ""
    b = ""
    time = maxI
    while i != 0 or j != 0:
        if time == 0:
            break
        if backtrack[i][j] == 1:
            a = a + '-'
            b = b + str(w[i-1])
            time -= 1
            i -= 1
        elif backtrack[i][j] == 2:
            a = a + str(v[j-1])
            b = b + str('-')
            j -= 1
        else:
            a = a + str(v[j-1])
            b = b + str(w[i-1])
            time -= 1
            i -= 1
            j -= 1
    return a, b

if __name__ == "__main__":

    file = open(sys.argv[1], 'r')

    v = file.readline().strip()
    w = file.readline().strip()

    maximum, maxI, backtrack = LCSbacktrack(v,w)
    print(maximum)
    a, b = constructAligm(backtrack, v, w, maxI)
    print(a[::-1])
    print(b[::-1])