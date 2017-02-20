import sys
import random
from ReadFile import ReadReadPairs

def ReadFile(file):
    with open(file) as f:
        numbers = f.readline().split()
        k = int(numbers[0])
        d = int(numbers[1])

        patterns = f.readlines()
        patterns = [p.strip().split('|') for p in patterns]
    return (k, d, patterns)

def GappedGenomePathString(k, d, patterns):
    string = patterns[0][0]
    for p in patterns[1:d+1]:
        string += p[0][-1]
    string += patterns[0][1]
    for p in patterns[1:]:
        string += p[1][-1]
    return string

if __name__ == "__main__":
    file = sys.argv[1]
    (k, d, patterns) = ReadFile(file)
    string = GappedGenomePathString(k, d, patterns)
    print string
