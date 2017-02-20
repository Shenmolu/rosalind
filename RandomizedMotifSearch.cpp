//
//  RandomizedMotifSearch.cpp
//
//
//  Created by Shenmo Lu on 1/22/17.
//
//

#include <stdio.h>
#include <string>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <climits>
#include <algorithm>
#include "functions.hpp"

using namespace std;

vector<string> RandomizedMotifSearch(vector<string> dna, int k, int t) {

	vector<string> bestMotifs;
	vector<string> motifs;
	vector<string> realBest;
	int count[k][4];
	double profile[k][4];
	string motifi;
	int strLen = dna[0].length();
	int numMotifs = 0;
	int score,bestScore;
	int lowestScore = INT_MAX;
	bool pseudo = false;
	int randNum;
	srand (time(NULL));

	for (int r = 0; r < 1000; r++) {

		// zero-fill count
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < 4; j++) {
				count[i][j] = 0;
			}
		}

		bestMotifs.clear();
		motifs.clear();

		// motif matrix formed by random k-mers in each string from Dna
		for (int i = 0; i < t; i++) {
			randNum = rand() % (strLen-k+1);
			motifi = dna[i].substr(randNum, k);
			bestMotifs.push_back(motifi);
			for (int j = 0; j < k; j++) {
				count[j][symbolToNumber(motifi.at(j))]++;
			}
		}
		bestScore = Score(count, k);

		while(1) {
			motifs.clear();

			// form profile
			for (int m = 0; m < k; m++) {
				for (int n = 0; n < 4; n++) {
					if (count[m][n] == 0) {
						pseudo = true;
						goto next;
					}
				}
			}

			next:
			numMotifs = count[0][0] + count[0][1] + count[0][2] + count[0][3];
			for (int m = 0; m < k; m++) {
				for (int n = 0; n < 4; n++) {
					if (pseudo) {
						profile[m][n] = ((double)count[m][n]+1)/((double)numMotifs+4);
					}
					else {
						profile[m][n] = (double)count[m][n]/(double)numMotifs;
					}
				}
			}

			// zero-fill count
			for (int i = 0; i < k; i++) {
				for (int j = 0; j < 4; j++) {
					count[i][j] = 0;
				}
			}

			// for each string text
			for (int j = 0; j < t; j++) {

				motifi = profileMostProbableKmer(dna[j], k, profile);
				motifs.push_back(motifi);

				for (int m = 0; m < k; m++) {
					count[m][symbolToNumber(motifi.at(m))]++;
				}
			}

			score = Score(count, k);
			if (score < bestScore) {
				bestScore = score;
				bestMotifs = motifs;
			}
			else {
				break;
			}
		}

		if (bestScore < lowestScore) {
			lowestScore = bestScore;
			realBest = bestMotifs;
		}
	}
	return realBest;
}