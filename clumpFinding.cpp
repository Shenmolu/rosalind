//
//  ClumpFinding.cpp
//
//
//  Created by Shenmo Lu on 1/11/17.
//
//

#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include "functions.hpp"

using namespace std;

// Frequency Array approach
vector<string> clumpFinding(string genome, int k, int L, int t) {
	vector<int> freqArray;
	freqArray = computingFrequencies(genome.substr(0, L), k);

	for (int i = 0; i <= genome.size() - L; i++) {
		


	}

}
/*
vector<string> clumpFinding(string genome, int k, int l, int t) {
	string kmer;
	int index;
	vector<int> pos;
	vector<string> frequentPatterns;

	for (int i = 0; i <= genome.size() - k; i++) {
        kmer = genome.substr(i, k);
        index = patternToNumber(kmer);
   		pos = patternMatching(genome, kmer);
   		if (pos.size() >= t) {
       		for (int j = 0; j <= pos.size() - t; j++) {
       			if (pos[j+t-1] + k - pos[j] <= l) {
					if(find(frequentPatterns.begin(), frequentPatterns.end(), kmer) == frequentPatterns.end()) {
					    frequentPatterns.push_back(kmer);
       				}
       				break;
       			}
       		}
       	}
    }

    return frequentPatterns;
}*/

/*
//A time-saving but memory-consuming version of the function
vector<string> clumpFinding(string genome, int k, int l, int t) {
	string kmer;
	int index;
	vector<int> pos;
	vector<string> frequentPatterns;
	int size = (int)pow(4, k);
	int clump[size];
	fill(clump, clump+size, 0);
	for (int i = 0; i <= genome.size() - k; i++) {
        kmer = genome.substr(i, k);
        index = patternToNumber(kmer);
        if (clump[index] == 0) {
       		pos = patternMatching(genome, kmer);
       		if (pos.size() >= t) {
	       		for (int j = 0; j <= pos.size() - t; j++) {
	       			if (pos[j+t-1] - pos[j] <= l - k) {
	       				clump[index] = 1;
	       				frequentPatterns.push_back(kmer);
	       				break;
	       			}
	       		}
	       	}
    	}
    }

    return frequentPatterns;
}
*/