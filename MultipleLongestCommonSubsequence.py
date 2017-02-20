def LCSBACKTRACK(v, w, u):
    m = len(v) + 1
    n = len(w) + 1
    l = len(u) + 1

    s = [[[0] * l for x in range(n)] for y in range(m)]
    backtrack = [[[0] * l for x in range(n)] for y in range(m)]

    for i in range(n):
        s[i][0][0]= -i
        backtrack[i][0][0] = 1

    for i in range(m):
        s[0][i][0] = -i
        backtrack[0][i][0] = 2

    for i in range(l):
        s[0][0][i]= -i
        backtrack[0][0][i] = 3

    for k in range(1, l):
        for i in range(1, n):
            for j in range(1, m):
                p = 1 if (u[k-1]==v[j-1] and (v[j-1]==w[i-1])) else 0

                s1 = s[i-1][j][k]
                s2 = s[i][j-1][k]
                s3 = s[i][j][k-1]
                s4 = s[i-1][j-1][k]
                s5 = s[i-1][j][k-1]
                s6 = s[i][j-1][k-1]
                s7 = s[i-1][j-1][k-1] + p
                score = s[i][j][k] = max(s1, s2, s3, s4, s5, s6, s7)

                if score == s1:
                    backtrack[i][j][k] = 1
                if score == s2:
                    backtrack[i][j][k] = 2
                if score == s3:
                    backtrack[i][j][k] = 3
                if score == s4:
                    backtrack[i][j][k] = 4
                if score == s5:
                    backtrack[i][j][k] = 5
                if score] == s6:
                    backtrack[i][j][k] = 6
                if score == s7:
                    backtrack[i][j][k] = 7
    print(s[len(w)][len(v)][len(u)])
    return(backtrack)

def OutputLCS(backtrack, j, i, k):
    a = ""
    b = ""
    c = ""
    while((i!=0)and(j!=0)and(k!=0)):
        if backtrack[i][j][k] == 1:
            a = a + '-'
            b = b + str(w[i-1])
            c = c + '-'
            i -= 1
        elif backtrack[i][j][k] == 2:
            a = a + str(v[j-1])
            b = b + '-'
            c = c + '-'
            j -= 1
        elif backtrack[i][j][k] == 3:
            a = a + '-'
            b = b + '-'
            c = c + str(u[k-1])
            k -= 1
        elif backtrack[i][j][k] == 4:
            a = a + '-'
            b = b + str(w[i-1])
            c = c + str(u[k-1])
            k -= 1
            i -= 1
        elif backtrack[i][j][k] == 5:
            a = a + str(v[j-1])
            b = b + str(w[i-1])
            c = c + '-'
            j -= 1
            i -= 1
        elif backtrack[i][j][k] == 6:
            a = a + str(v[j-1])
            b = b + '-'
            c = c + str(u[k-1])
            j -= 1
            k -= 1
        elif backtrack[i][j][k] == 7:
            a = a + str(v[j-1])
            b = b + str(w[i-1])
            c = c + str(u[k-1])
            j -= 1
            k -= 1
            i -= 1

    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        v = f.readline().strip()
        w = f.readline().strip()

        backtrack = LCSBacktrack(v, w, u)
        output = ''
        OutputLCS(backtrack, v, len(v), len(w), len(u))