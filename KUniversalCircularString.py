import sys
import random
import itertools
from DeBruijnFromKmers import DeBruijnFromKmers
from EulerianCycle import EulerianCycle


def binaryStrings(k):
    patterns = ["".join(seq) for seq in itertools.product("01", repeat=k)]
    return patterns

#def KUniversalCircularString():

def EulerianCycle(graph):
    stack = []
    cycle = []
    outNode = random.choice(graph.keys())
    while 1:
        if (len(graph[outNode]) > 0):
            stack.append(outNode)
            inNode = graph[outNode][0]
            graph[outNode].remove(inNode)
            outNode = inNode     
        else:
            cycle.insert(0, outNode)
            if (len(stack) > 0):
                outNode = stack.pop(-1)
            else:
                break
    return cycle

if __name__ == "__main__":
    k = int(sys.argv[1])
    patterns = binaryStrings(k)
    graph = DeBruijnFromKmers(patterns)
    cycle = EulerianCycle(graph)
    string = cycle[0]
    for p in cycle[1:-(k-1)]:
        string += p[-1]
    print string
