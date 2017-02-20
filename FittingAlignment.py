import sys

def LCSbacktrack(v, w):
    m = len(v) + 1
    n = len(w) + 1

    s = [x[:] for x in [[0] * m] * n]
    backtrack = [x[:] for x in [[1] * m] * n]

    for i in range(n):
        s[i][0]= -i
        backtrack[i][0] = 1

    for j in range(m):
        s[0][j] = 0
        backtrack[0][j] = 2

    for i in range(1, n):
        for j in range(1, m):
            f = 1 if v[j-1] == w[i-1] else -1
            opt1 = s[i-1][j] - 1
            opt2 = s[i][j-1] - 1
            opt3 = s[i-1][j-1] + f
            s[i][j] = max(opt1, opt2, opt3)

            if s[i][j] == opt1:
                backtrack[i][j] = 1
            if s[i][j] == opt2:
                backtrack[i][j] = 2
            if s[i][j] == opt3:
                backtrack[i][j] = 3

    maximum = 0
    maxJ = 0
    for j in range(m):
        if(s[i][j] > maximum):
            maxJ = j
            maximum=s[i][j]

    return maximum, maxJ, backtrack

def constructAligm(backtrack, v, w, maxJ):
    i = len(w)
    j = maxJ
    a = ""
    b = ""
    time = len(w)
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

    maximum, maxJ, backtrack = LCSbacktrack(v,w)
    print(maximum)
    a, b = constructAligm(backtrack, v, w, maxJ)
    print(a[::-1])
    print(b[::-1])