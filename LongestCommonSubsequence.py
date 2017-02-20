import sys

def LCSBacktrack(v, w):
    n = len(v)+1
    m = len(w)+1
    
    s = [x[:] for x in [[0] * m] * n]
    backtrack = [x[:] for x in [[0] * m] * n]

    for i in range(0, n):
        s[i][0] = 0

    for i in range(0, m):
        s[0][i] = 0

    for i in range(1, n):
        for j in range(1, m):
            if s[i-1][j] > s[i][j-1]:
                maxLen = s[i-1][j]
                backtrack[i][j] = 1
            else:
                maxLen = s[i][j-1]
                backtrack[i][j] = 2

            if v[i-1] == w[j-1] and maxLen < s[i-1][j-1]+1:
                maxLen = s[i-1][j-1]+1
                backtrack[i][j] = 3

            s[i][j] = maxLen

    return backtrack

def OutputLCS(backtrack, v, i, j):
    global output
    while i != 0 and j != 0:
        if backtrack[i][j] == 1:
            i -= 1
        elif backtrack[i][j] == 2:
            j -= 1
        elif backtrack[i][j] == 3:
            output = v[i-1] + output
            i -= 1
            j -= 1

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        v = f.readline().strip()
        w = f.readline().strip()

        backtrack = LCSBacktrack(v, w)
        output = ''
        OutputLCS(backtrack, v, len(v), len(w))
        print(output)
