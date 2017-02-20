import sys
from ReadFile import ReadAdjacentList
from Degree import Degree

def MaximalNonBranchingPaths(graph):
    paths = []
    degree = Degree(graph)
    visited = []    # stores all the visited 1-in-1-out nodes
    for v in graph:
        if degree[v][0] != 1 or degree[v][1] != 1:  # if v is not a 1-in-1-out node
            visited.append(v)
            if degree[v][1] > 0:
                for w in graph[v]:
                    path = [v, w]
                    while degree[w][0] == 1 and degree[w][1] == 1:
                        visited.append(w)
                        w = graph[w][0]
                        path.append(w)
                    paths.append(path)
    
    for v in graph:
        if degree[v][0] == 1 and degree[v][1] == 1:
            if v not in visited:
                visited.append(v)
                w = graph[v][0]
                cycle = [v]
                while degree[w][0] == 1 and degree[w][1] == 1:
                    visited.append(w)
                    cycle.append(w)
                    if v == w:
                        break
                    w = graph[w][0]
                paths.append(cycle)
    return paths

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        graph = ReadAdjacentList(f)
        paths = MaximalNonBranchingPaths(graph)
        for path in paths:
            print ' -> '.join(path)
