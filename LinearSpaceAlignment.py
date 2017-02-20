import sys

def LinearSpaceAlignment(top, bottom, left, right):
    global protein1, protein2
    global prevScores, currScores
    global align1, align2
    
    if left == right:
        align1 += protein1[top:bottom]
        align2 += ['-']*(bottom - top)
        #align1.extend(list(protein1[top:bottom]))
        #align2.extend(['-']*(bottom - top))
        return -sigma * (bottom - top)

    if top == bottom:
        align1.extend(['-']*(right-left))
        align2.extend(list(protein2[left,right]))
        return -sigma * (right - left)

    middle = int((left+right)/2)
    midEdge = MiddleEdge(top, bottom, left, right)
    midNode = midEdge[0]
    linearSpaceAlignment(top, midNode, left, middle)

    if midEdge[0] == midEdge[2] and midEdge[1] + 1 == midEdge[3]:
        align1 += '-'
        align2 += protein2[midEdge[1]]
    if midEdge[0] + 1 == midEdge[2] and midEdge[1] == midEdge[3]:
        align1 += protein1[midEdge[0]]
        align2 += '-'
    else:
        align1 += protein1[midEdge[0]]
        align2 += protein2[midEdge[1]]

    linearSpaceAlignment(middleEdge[2], bottom, middleEdge[3], right)
    return middleEdge

def Score(v, w):
    global sigma
    global score

    n = len(v) + 1
    m = len(w) + 1

    prevScores = [0] * (len1 + 1)
    currScores = [0] * (len1 + 1)
    currScores[0] = -sigma

    for j in range(m):
        prevScores[j] = -sigma * j

    for i in range(1, n):
        currScores[0] = -sigma * i
        for j in range(1, m):
            p = score[order[v[i-1]]][order[w[j-1]]]
            topScore = currScores[j-1] - sigma
            leftScore = prevScores[j] - sigma
            diagScore = prevScores[j-1] + p
            currScores[j] = max(topScore, leftScore, diagScore)
        prevScores = currScores[:]

    return prevScores

def MiddleEdge(v, w):
    middle = int(len2/2)
    i = 0
    j = middle
    k = 0
    l = middle + 1

    v1 = v[:j]
    w1 = w[:]
    v2 = v[j+1::-1]
    w2 = w[::-1]

    fromSource = Score(v1,w1)
    toSink = Score(v2,w2)
    toSink = toSink[::-1]

    score1 = [fromSource[i] + toSink[i] - sigma for i in range(len2)]
    diagnal = [score[order[v[j]]][order[w[i-1]]] for i in range(1, len2)]
    score2 = [fromSource[i-1] + toSink[i] + diagnal[i-1] for i in range(1, len2)]

    max1 = max(score1)
    max2 = max(score2)
    maxS = max(max1, max2)
    if maxS == max1:
        i = score1.index(maxS)
        k = score1.index(maxS)
    else:
        i = score2.index(maxS) - 1
        k = score2.index(maxS)

    return (i, j, k, l)

if __name__ == "__main__":

    file = open(sys.argv[1], 'r')
    matrix = open(sys.argv[2], 'r')

    protein1 = file.readline().strip()
    protein2 = file.readline().strip()

    sigma = 5

    order = {}
    row = matrix.readline().strip().split()
    for i in range(len(row)):
        order[row[i]] = i

    score = []
    matrix = matrix.readlines()
    matrix = [row.strip().split() for row in matrix]
    for row in matrix:
        score.append([int(a) for a in row[1:]])

    len1 = len(protein1)
    len2 = len(protein2)

    prevScores = [0] * (len1 + 1)
    cureScores = [0] * (len1 + 1)

    #align1 = []
    #align2 = []
    align1 = ''
    align2 = ''
    LinearSpaceAlignment(0, len1, 0, len2)