import sys

def LCSBacktrack(v, w):
    global sigma
    global score

    m = len(v)+1
    n = len(w)+1

    s = [x[:] for x in [[0] * m] * n]
    backtrack = [x[:] for x in [[1] * m] * n]

    for i in range(m):
        s[0][i]= -sigma * i
        backtrack[0][i] = 2

    for j in range(n):
        s[j][0] = -sigma * j
        backtrack[j][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            mu = score[ord[v[j-1]]][ord[w[i-1]]]
            deletion = s[i-1][j] - sigma
            insertion = s[i][j-1] - sigma
            match = s[i-1][j-1] + mu
            
            s[i][j] = max(deletion, insertion, match)
            
            # 1 for up, 2 for left, 3 for diagonal
            if s[i][j] == deletion:
                backtrack[i][j] = 1
            if s[i][j] == insertion:
                backtrack[i][j] = 2
            if s[i][j] == match:
                backtrack[i][j] = 3

    return(s[-1][-1], backtrack)

def OutputLCS(backtrack, v, i, j):
    a = ""
    b = ""
    while i != 0 or j != 0:
        if backtrack[i][j] == 1:
            a = a + '-'
            b = b + str(w[j-1])
            j -= 1
        elif backtrack[i][j] == 2:
            a = a + str(v[i-1])
            b = b + str('-')
            i -= 1
        else:
            a = a + str(v[i-1])
            b = b + str(w[j-1])
            i -= 1
            j -= 1
    return a, b

if __name__ == "__main__":

    file = open(sys.argv[1], 'r')
    matrix = open(sys.argv[2], 'r')
    sigma = int(sys.argv[3])

    v = file.readline().strip()
    w = file.readline().strip()

    ord = {}
    row = matrix.readline().strip().split()
    for i in range(len(row)):
        ord[row[i]] = i

    score = []
    matrix = matrix.readlines()
    matrix = [row.strip().split() for row in matrix]
    for row in matrix:
        score.append([int(a) for a in row[1:]])

    score, backtrack = LCSBacktrack(v, w)
    print('score: ', score)
    a, b = OutputLCS(backtrack, v, len(v), len(w))
    print(a[::-1])
    print(b[::-1])
