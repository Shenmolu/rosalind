import sys
from ReadFile import ReadPatterns

def GenomePathSpelledString(patterns):
    text = patterns[0]
    for p in patterns[1:]:
    	text += p[-1]
    return text

if __name__ == "__main__":
	file = sys.argv[1]
	with open(file) as f:
		patterns = ReadPatterns(f)
		print GenomePathSpelledString(patterns)