import sys
import random



def read_file(file):
    params = file.readline().split()
    k = int(params[0])
    t = int(params[1])
    N = int(params[2])
    dna = []
    for i in range(t):
        dna.append(file.readline().strip())
    return (dna, k, t, N)

def indexToAcid(i):
    return "ACGT"[i]

def symbol_to_number(a):
    return "ACGT".index(a)

def motifs_count(motifs, k):
    count = []
    for i in range(0, k):
        curr_count = [0] * 4
        for motif in motifs:
            curr_count[symbol_to_number(motif[i])] += 1
        count.append(curr_count)
    return count

def motifs_score(motifs, k):
    score = 0
    for count in motifs_count(motifs, k):
        score += sum(count) - max(count)
    return score

def motifs_profile(motifs, k):
    counts = motifs_count(motifs, k)
    profile = []
    total = float(len(motifs))
    if any(0 in count for count in counts):
        for count in counts:
            probs = [(c+1)/(total+4) for c in count]
            profile.append(probs)

    else:
        for count in counts:
            probs = [c/total for c in count]
            profile.append(probs)

    return profile

def most_probable_kmer(profile, text, k):
    prob = []
    for i in range(0, len(text)-k+1):
        pr = 1.0
        for j in xrange(k):
            pr *= profile[j][symbol_to_number(text[i+j])]
        prob.append(pr)


    total = float(sum(prob))
    r = random.random()
    prob_sum = 0.0
    for i in range(len(prob)):
        prob_sum += prob[i]
        if prob_sum/total >= r:
            return text[i:i+k]
    return -1

    
def gibbs_sampler(dna, k, t, N):
    motifs = []
    for text in dna:
        pos = random.randint(0, len(text) - k)
        motifs.append(text[pos:pos+k])

    best_motifs = motifs
    best_score = motifs_score(motifs, k)

    for j in xrange(N):
        i = random.randint(0, t - 1)
        profile = motifs_profile(motifs[:i] + motifs[i+1:], k)
        motifs[i] = most_probable_kmer(profile, dna[i], k)

        curr_score = motifs_score(motifs, k)
        if curr_score < best_score:
            best_score = curr_score
            best_motifs = motifs

    return (best_score, best_motifs)

file = sys.argv[1]
(dna, k, t, N) = read_file(open(file, 'r'))

best_score = float("inf")
for start in xrange(20):
    (curr_score, curr_motifs) = gibbs_sampler(dna, k, t, N)
    if curr_score < best_score:
        best_score = curr_score
        best_motifs = curr_motifs

print best_score
for motif in best_motifs:
    print motif