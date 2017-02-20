import sys
import random
from ReadFile import ReadAdjacentList

def EulerianCycle(graph):
    stack = []
    cycle = []
    v = random.choice(graph.keys())
    while 1:
        if (len(graph[v]) > 0):
            stack.append(v)
            w = graph[v][0]
            graph[v].remove(w)
            v = w
        else:
            cycle.insert(0, v)
            if (len(stack) > 0):
                v = stack.pop(-1)
            else:
                break
    return cycle

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        graph = ReadAdjacentList(f)
        cycle = EulerianCycle(graph)
        print '->'.join(cycle)
