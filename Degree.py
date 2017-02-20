import sys

def Degree(graph):
    degree = {}
    for v in graph:
        # degree[v] = [indegree, outdegree]
        degree.setdefault(v, [0,0])
        degree[v][1] += len(graph[v])
        for w in graph[v]:
            degree.setdefault(w, [0,0])
            degree[w][0] += 1
    return degree