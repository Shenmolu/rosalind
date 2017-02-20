import sys

def LCSBacktrack(v, w):
    global sigma

    m = len(v)+1
    n = len(w)+1

    s = [x[:] for x in [[0] * m] * n]

    for i in range(n):
        s[i][0]= -i

    for j in range(m):
        s[0][j] = -j

    for i in range(1, n):
        for j in range(1, m):
            f = 0 if v[j-1] == w[i-1] else -1
            opt1 = s[i-1][j] - 1
            opt2 = s[i][j-1] - 1
            opt3 = s[i-1][j-1] + f
            s[i][j] = max(opt1, opt2, opt3)

    dist = abs(s[n-1][m-1])
    return dist

if __name__ == "__main__":
    file = open(sys.argv[1], 'r')

    v = file.readline().strip()
    w = file.readline().strip()

    dist = LCSBacktrack(v,w)
    print(dist)



