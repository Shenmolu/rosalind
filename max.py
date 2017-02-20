import sys

def maximalNonBranchingPaths(patterns):
    g = {}
    for text in patterns:
        prefix = text[:-1]
        suffix = text[1:]

        if prefix not in g.keys():
            g[prefix] = []
        g[prefix].append(suffix)
    """
    
    # Assume the type of nodes is Integer with the value from 0 to len(g)-1.
    """
    # Count the in-degree of nodes.
    indegree = [0] * (len(g))
    for node in g:
        for v in g[node]:
            indegree[v] += 1

    def oneone(v):
        """
        Check if the node v is a 1-in-1-out node. True for yes, False for no.
        """
        nonlocal indegree, g
        if indegree[v] != 1 or len(g[v]) != 1:
            return False
        else:
            return True        


    # if node v is a 1-in-1-out node and is visited, it will be added in this set.
    visited = set()
    
    paths = []
    for v in g:
        if not oneone(v):           # if v is not a 1-in-1-out node
            visited.add(v)
            
            for w in g[v]:
                non_branching_path = [v,w]
                while oneone(w):
                    visited.add(w)
                    non_branching_path.append(g[w][0])
                    w = g[w][0]
                paths.append(non_branching_path)

    # check all isolated cycle
    for v in g:
        if oneone(v) and v not in visited:
            visited.add(v)
            cycle = [v]
            w = g[v][0]

            while oneone(w):
                cycle.append(w)
                visited.add(w)
                if w == v:
                    break
                w = g[w][0]

            paths.append(cycle)
            
    return paths

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        patterns = f.readlines()
        patterns = [p.strip() for p in patterns]
        path = maximalNonBranchingPaths(patterns)

        print (path)


