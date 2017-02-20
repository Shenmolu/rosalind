import sys

def ManhattanTourist(n, m, down, right):
    s = [x[:] for x in [[0] * (m+1)] * (n+1)]

    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]

    for i in range(1, m+1):
        s[0][i] = s[0][i-1] + right[0][i-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j]+down[i-1][j], s[i][j-1]+right[i][j-1])

    return s[n][m]

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        size = f.readline().split()
        n = int(size[0])
        m = int(size[1])
        weights = f.readlines()
        down = [row.split() for row in weights[:n]]
        down = [list(map(int, row)) for row in down]
        right =[row.split() for row in weights[n+1:]]
        right = [list(map(int, row)) for row in right]

        minLen = ManhattanTourist(n, m, down, right)

        print(minLen)