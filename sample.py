def LCSBACKTRACK(v, w,u):
    global  score
    m=len(v)+1
    n=len(w)+1
    l=len(u)+1
    Backtrack=[[[0 for x in range(l)]for y in range(m)]for z in range(n)]
    s=[[[0 for x in range(l)]for y in range(m)]for z in range(n)]
    for i in range(n):
        s[i][0][0]= -i
        Backtrack[i][0][0] = 0
    for i in range(m):
        s[0][i][0] = -i
        Backtrack[0][i][0] = 1
    for i in range(l):
        s[0][0][i]= -i
        Backtrack[0][0][i] = 2
    for k in range(1, len(u)+1):
        for i in range(1,len(w) + 1):
            for j in range(1,len(v) + 1):
                if(u[k-1]==v[j-1])and(v[j-1]==w[i-1]):
                    f=1
                else:
                    f=0
                s[i][j][k] = max(s[i-1][j][k], s[i][j-1][k], s[i][j][k-1],s[i-1][j-1][k],s[i-1][j][k-1],
                                 s[i][j-1][k-1],s[i-1][j-1][k-1] + f)
                if s[i][j][k] == s[i-1][j][k]:
                    Backtrack[i][j][k] = 0
                if s[i][j][k] == s[i][j-1][k]:
                    Backtrack[i][j][k] = 1
                if s[i][j][k] == s[i][j][k-1]:
                    Backtrack[i][j][k] = 2
                if s[i][j][k] == s[i-1][j-1][k]:
                    Backtrack[i][j][k] = 3
                if s[i][j][k] == s[i-1][j][k-1]:
                    Backtrack[i][j][k] = 4
                if s[i][j][k] == s[i][j-1][k-1]:
                    Backtrack[i][j][k] = 5
                if s[i][j][k] == s[i-1][j-1][k-1] + f:
                    Backtrack[i][j][k] = 6
    fout.write(str(s[len(w)][len(v)][len(u)])+'\n')
    print(s)
    print(Backtrack)
    return(Backtrack)

def OUTPUTAligm(Backtrack, j, i, k):
    ans1 = ""
    ans2 = ""
    ans3 = ''
    while((i!=0)and(j!=0)and(k!=0)):
        if Backtrack[i][j][k] == 0:
            ans1 = ans1 + '-'
            ans2 = ans2 + str(w[i-1])
            ans3 = ans3 + '-'
            i -= 1
        else:
            if Backtrack[i][j][k] == 1:
                ans1 = ans1 + str(v[j-1])
                ans2 = ans2 + '-'
                ans3 = ans3 + '-'
                j -= 1
            else:
                if Backtrack[i][j][k] == 2:
                    ans1 = ans1 + '-'
                    ans2 = ans2 + '-'
                    ans3 = ans3 + str(u[k-1])
                    k -= 1
                else:
                    if Backtrack[i][j][k] == 4:
                        ans1 = ans1 + '-'
                        ans2 = ans2 + str(w[i-1])
                        ans3 = ans3 + str(u[k-1])
                        k -= 1
                        i -= 1
                    else:
                        if Backtrack[i][j][k] == 3:
                            ans1 = ans1 + str(v[j-1])
                            ans2 = ans2 + str(w[i-1])
                            ans3 = ans3 + '-'
                            j -= 1
                            i -= 1
                        else:
                            if Backtrack[i][j][k] == 5:
                                ans1 = ans1 + str(v[j-1])
                                ans2 = ans2 + '-'
                                ans3 = ans3 + str(u[k-1])
                                j -= 1
                                k -= 1
                            else:
                                if Backtrack[i][j][k] == 6:
                                    ans1 = ans1 + str(v[j-1])
                                    ans2 = ans2 + str(w[i-1])
                                    ans3 = ans3 + str(u[k-1])
                                    j -= 1
                                    k -= 1
                                    i -= 1

    fout.write(ans1[::-1]+'\n')
    fout.write(ans2[::-1]+'\n')
    fout.write(ans3[::-1])

fin = open('data.txt', 'r')
fout=open('a.txt', 'w')
v=fin.readline().replace('\n','')
w=fin.readline().replace('\n','')
u=fin.readline().replace('\n','')
b=LCSBACKTRACK(v,w,u)
OUTPUTAligm(b,len(v),len(w),len(u))