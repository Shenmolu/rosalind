import sys
import copy

def constructGraph(rows):
    graph = {}
    weight = {}
    for row in rows:
        row = row.strip().replace('->', ':').split(':')
        a = int(row[0])
        b = int(row[1])
        w = int(row[2])

        graph.setdefault(a, [[], []])
        graph.setdefault(b, [[], []])
        graph[a][1].append(b)
        graph[b][0].append(a)

        weight[(a,b)] = w

    return graph, weight

def TopologicalOrdering(graph):
    temp = copy.deepcopy(graph)
    order = []
    candidates = [key for key in temp.keys() if temp[key][0] == []]
    while len(candidates) > 0:
        a = candidates[0]
        order.append(a)
        candidates.remove(a)
        while len(temp[a][1]) > 0:
            b = temp[a][1][0]
            temp[a][1].remove(b)
            temp[b][0].remove(a)
            if len(temp[b][0]) <= 0:
                candidates.append(b)
    return order


def LongestPath(graph, weight, source, sink):
    s = {}
    path = []
    backtrack = [0 for x in range(len(graph)+1)]

    for b in graph:
        s[b] = -float('inf')
    s[source] = 0
    order = TopologicalOrdering(graph)

    for b in order:
        if len(graph[b][0]) > 0:
            s[b] = max([s[a]+weight[(a,b)] for a in graph[b][0]])
            for a in graph[b][0]:
                if s[b] == s[a]+weight[(a,b)]:
                    backtrack[b] = a
    path.append(sink)
    return s[sink], backtrack

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        source = int(f.readline().strip())
        sink = int(f.readline().strip())
        rows = f.readlines()

        graph, weight = constructGraph(rows)
        maxLen, path = LongestPath(graph, weight, source, sink)
        print(maxLen)
        print('->'.join(path))