import sys
from ReadFile import ReadPatterns

def DeBruijnFromKmers(patterns):
    graph = {}
    for text in patterns:
        prefix = text[:-1]
        suffix = text[1:]
        graph.setdefault(prefix, [])
        graph[prefix].append(suffix)
    return graph

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        patterns = ReadPatterns(f)
        graph = DeBruijnFromKmers(patterns)
        for key in sorted(graph):
            print "%s -> %s" % (key, ",".join(sorted(graph[key])))