import sys
from ReadFile import ReadPatterns
def DeBruijnFromString(text, k):
    graph = {}
    for i in xrange(len(text)-k+1):
        n = text[i:i+k-1]

        if n not in graph.keys():
            graph[n] = []
        graph[n].append(text[i+1:i+k])
    return graph

file = sys.argv[1]
with open(file) as f:
    param = ReadPatterns(f, True)
    k = param[0]
    text = param[1][0]

    graph = DeBruijnFromString(text, k)
    for key in sorted(graph):
        print "%s -> %s" % (key, ",".join(sorted(graph[key])))