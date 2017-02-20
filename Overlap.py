import sys
from ReadFile import ReadPatterns

def Overlap(patterns):
    graph = {}
    for i in range(0, len(patterns)):
        graph[patterns[i]] = []
        for j in [x for x in xrange(len(patterns)) if x != i]:
            if patterns[i][1:] == patterns[j][:-1]:
                graph[patterns[i]].append(patterns[j])
    return graph

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        patterns = ReadPatterns(f)
        graph = Overlap(patterns)
        for v in sorted(graph):
            for w in sorted(graph[v]):
                print v + ' -> ' + w