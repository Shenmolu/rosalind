import sys
from ReadFile import ReadPatterns
from DeBruijnFromKmers import DeBruijnFromKmers
from MaximalNonBranchingPaths import Degree
from MaximalNonBranchingPaths import MaximalNonBranchingPaths
from GenomePathSpelledString import GenomePathSpelledString

def ContigsFromReads(patterns):
    contigs = []
    graph = DeBruijnFromKmers(patterns)
    paths = MaximalNonBranchingPaths(graph)
    for path in paths:
        contigs.append(GenomePathSpelledString(path))
    return contigs

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        patterns = ReadPatterns(f)
        contigs = ContigsFromReads(patterns)
        for contig in contigs:
            print contig
        