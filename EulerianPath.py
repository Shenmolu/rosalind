import sys
import random
from Degree import Degree
from ReadFile import ReadAdjacentList

# return a node whose indegree is less than outdegree
def StartNode(degree):
    return [key for key in degree if degree[key][0] < degree[key][1]][0]

def EulerianPath(graph):
    stack = []
    path = []
    degree = Degree(graph)
    v = StartNode(degree)
    while 1:
        if v in graph and len(graph[v]) > 0:
            stack.append(v)
            w = graph[v][0]
            graph[v].remove(w)
            v = w
        else:
            path.insert(0, v)
            if len(stack) > 0:
                v = stack.pop(-1)
            else:
                break
    return path

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        graph = ReadAdjacentList(f)
        path = EulerianPath(graph)
        print '->'.join(path)
