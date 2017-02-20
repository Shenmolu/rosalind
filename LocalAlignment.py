import sys

def LCSBacktrack(v, w):
    global  score

    m = len(v) + 1
    n = len(w) + 1

    s = [x[:] for x in [[0] * m] * n]
    backtrack = [x[:] for x in [[1] * m] * n]

    for i in range(n):
        s[i][0] = 0
        backtrack[i][0] = 1

    for j in range(m):
        s[0][j] = 0
        backtrack[0][j] = 2

    for i in range(1, n):
        for j in range(1, m):
            f = score[index[v[j-1]]][index[w[i-1]]]
            opt1 = s[i-1][j] - sigma
            opt2 = s[i][j-1] - sigma
            opt3 = s[i-1][j-1] + f
            s[i][j] = max(opt1, opt2, opt3, 0)
            if s[i][j] == opt1:
                backtrack[i][j] = 1
            if s[i][j] == opt2:
                backtrack[i][j] = 2
            if s[i][j] == opt3:
                backtrack[i][j] = 3
            if s[i][j] == 0:
                backtrack[i][j] = 0
                
    maximum = 0
    for i in range(n):
        for j in range(m):
            if(s[i][j] > maximum):
                coord = (i, j)
                maximum = s[i][j]

    return maximum, coord, backtrack

def constructAligm(backtrack, v, coord):
    i = coord[0]
    j = coord[1]
    a = ""
    b = ""
    while i != 0 or j != 0:
        if backtrack[i][j] == 0:
            break
        elif backtrack[i][j] == 1:
            a = a + '-'
            b = b + str(w[i-1])
            i -= 1
        elif backtrack[i][j] == 2:
            a = a + str(v[j-1])
            b = b + str('-')
            j -= 1
        else:
            a = a + str(v[j-1])
            b = b + str(w[i-1])
            i -= 1
            j -= 1
    return a, b

if __name__ == "__main__":

    file = open(sys.argv[1], 'r')
    matrix = open(sys.argv[2], 'r')
    sigma = int(sys.argv[3])

    v = file.readline().strip()
    w = file.readline().strip()

    index = {}
    row = matrix.readline().strip().split()
    for i in range(len(row)):
        index[row[i]] = i

    score = []
    matrix = matrix.readlines()
    matrix = [row.strip().split() for row in matrix]
    for row in matrix:
        score.append([int(a) for a in row[1:]])

    m, coord, backtrack = LCSBacktrack(v,w)
    a, b = constructAligm(backtrack, v, coord)

    print(m) 
    print(a[::-1])
    print(b[::-1])