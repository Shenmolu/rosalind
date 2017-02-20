import sys

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

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        source = int(f.readline().strip())
        sink = int(f.readline().strip())
        rows = f.readlines()

        graph, weight = constructGraph(rows)
        order = TopologicalOrdering(graph)

        print ', '.join(order)
