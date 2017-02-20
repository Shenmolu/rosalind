import sys

def ReadAdjacentList(file):
    graph = []
    graph = file.readlines()
    graph = [line.strip().split(' -> ') for line in graph]
    graph = [(line[0], line[1].split(',')) for line in graph]
    graph = dict(graph)
    return graph

def ReadPatterns(file, num=False):
    numbers = []
    if num:
        numbers = file.readline().split()
        numbers = map(int, numbers)

    patterns = file.readlines()
    patterns = [p.strip() for p in patterns]
    if num:
        numbers.append(patterns)
        return numbers
    else:
        return patterns

def ReadReadPairs(file):
    with open(file) as f:
        numbers = f.readline().split()
        k = int(numbers[0])
        d = int(numbers[1])

        patterns = f.readlines()
        patterns = [p.strip().split('|') for p in patterns]
    return (k, d, patterns)