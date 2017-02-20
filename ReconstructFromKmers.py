import sys
from ReadFile import ReadPatterns
from Overlap import Overlap
from EulerianPath import EulerianPath
from GenomePathSpelledString import GenomePathSpelledString

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
        param = ReadPatterns(f, True)
        patterns = param[1]

        graph = Overlap(patterns)
        path = EulerianPath(graph)
        text = GenomePathSpelledString(path)
        print text