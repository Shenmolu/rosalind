import sys

def read_file(file):
    k = int(file.readline())
    text = file.readline().strip()
    return (k, text)

def Composition(text, k):
    comp = []
    comp = [text[i:i+k] for i in range(0, len(text)-k+1)]
    comp = sorted(comp)
    return comp

if __name__ == "__main__":
    file = sys.argv[1]
    with open(file) as f:
		(k, text) = read_file(f)
		comp = Composition(text, k)
		for c in comp:
		    print c