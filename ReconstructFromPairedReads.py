import sys
import random
import itertools
from DeBruijnFromKmers import DeBruijnFromKmers
from EulerianPath import EulerianPath

def readFile(file):
    with open(file) as f:
        numbers = f.readline().split()
        k = int(numbers[0])
        d = int(numbers[1])

        patterns = f.readlines()
        patterns = [p.strip() for p in patterns]
    return (k, d, patterns)

def DeBruijnFromPairedReads(patterns, k):
    graph = {}
    for text in patterns:
        prefix = (text[:k-1], text[k+1:-1])
        suffix = (text[1:k], text[k+2:])

        if prefix not in graph.keys():
            graph[prefix] = []
        graph[prefix].append(suffix)
    return graph

if __name__ == "__main__":
    file = sys.argv[1]
    (k, d, patterns) = readFile(file)
    graph = DeBruijnFromPairedReads(patterns, k)
    path = EulerianPath(graph)
    
    string = path[0][0]
    for p in path[1:]:
        string += p[0][-1]
    for p in path[-k-d:]:
        string += p[1][-1]
    print string






