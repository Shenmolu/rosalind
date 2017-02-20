//
//  GreedyMotifSearch.cpp
//
//
//  Created by Shenmo Lu on 1/21/17.
//
//

#include <math.h>
#include <stdio.h>
#include <string>
#include <vector>
#include "functions.hpp"

using namespace std;

vector<string> GreedyMotifSearch(vector<string> dna, int k, int t) {

	vector<string> bestMotifs;
	vector<string> motifs;
	int count[k][4];
	double profile[k][4];
	int strLen = dna[0].length();
	int bases[t][strLen];
	string motif0;
	string motifi;
	int numMotifs = 0;
	int score,bestScore;

	// convert symbols to numbers
	for (int i = 0; i < t; i++) {
		for (int j = 0; j < strLen; j++) {
			bases[i][j] = symbolToNumber(dna[i].at(j));
		}
	}

	// zero-fill count
	for (int i = 0; i < k; i++) {
		for (int j = 0; j < 4; j++) {
			count[i][j] = 0;
		}
	}	

	// motif matrix formed by first k-mers in each string from Dna
	for (int i = 0; i < t; i++) {
		motifi = dna[i].substr(0, k);
		bestMotifs.push_back(motifi);
		for (int j = 0; j < k; j++) {
			count[j][bases[i][j]]++;
		}
	}
	bestScore = Score(count, k);

	// for each k-mer Motif in the first string from Dna
	for (int i = 0; i <= strLen - k; i++) {
		// zero-fill count
		for (int j = 0; j < k; j++) {
			for (int m = 0; m < 4; m++) {
				count[j][m] = 0;
			}
		}

		motifs.clear();
		motif0 = dna[0].substr(i, k);
		motifs.push_back(motif0);
		numMotifs = 1;
		for (int j = 0; j < k; j++) {
			count[j][bases[0][i+j]]++;
		}

		// for each string text
		for (int j = 1; j < t; j++) {
			// form profile
			for (int m = 0; m < k; m++) {
				for (int n = 0; n < 4; n++) {
					profile[m][n] = (double)count[m][n]/(double)numMotifs;
				}
			}

			motifi = profileMostProbableKmer(dna[j], k, profile);
			motifs.push_back(motifi);
			numMotifs++;

			// update count
			for (int m = 0; m < k; m++) {
				count[m][symbolToNumber(motifi.at(m))]++;
			}
		}

		score = Score(count, k);
		if (score < bestScore) {
			bestScore = score;
			bestMotifs = motifs;
		}
	}
	return bestMotifs;
}
