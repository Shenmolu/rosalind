//
//  GibbsSampler.cpp
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
#include <random>
#include "functions.hpp"

using namespace std;

vector<string> GibbsSampler(vector<string> dna, int k, int t, int N) {

	vector<string> bestMotifs;
	vector<string> motifs;
	vector<string> realBest;
	vector<double> sumVec;
	int count[k][4];
	double profile[k][4];
	string motifi;
	int strLen = dna[0].length();
	int numMotifs = 0;
	int score;
	int bestScore;
	bool pseudo;
	int randNum;
	srand (time(NULL));
	double pr;
	double sum;
	double randPr;
	int index;
	string kmer;
	string motif;
	string replaced;
	int lowestScore = INT_MAX;

	for (int r = 0; r < 20; r++) {
		motifs.clear();
		// motif matrix formed by random k-mers in each string from Dna
		for (int i = 0; i < t; i++) {
			randNum = rand() % (strLen-k+1);
			motifi = dna[i].substr(randNum, k);
			motifs.push_back(motifi);
		}

		// zero-fill count
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < 4; j++) {
				count[i][j] = 0;
			}
		}
		for (int i = 0; i < t; i++) {
			motif = motifs[i];
			for (int j = 0; j < k; j++) {
				count[j][symbolToNumber(motif.at(j))]++;
			}
		}

		bestMotifs = motifs;
		bestScore = Score(count, k);

		for (int n = 0; n < N; n++) {

			// zero-fill count
			for (int i = 0; i < k; i++) {
				for (int j = 0; j < 4; j++) {
					count[i][j] = 0;
				}
			}

			randNum = rand() % t;

			for (int i = 0; i < t; i++) {
				if (i != randNum) {
					motif = motifs[i];
					for (int j = 0; j < k; j++) {
						count[j][symbolToNumber(motif.at(j))]++;
					}
				}
			}

			// form profile
			pseudo = false;
			for (int i = 0; i < k; i++) {
				for (int j = 0; j < 4; j++) {
					if (count[i][j] == 0) {
						pseudo = true;
						goto next;
					}
				}
			}
			next:
			numMotifs = count[0][0] + count[0][1] + count[0][2] + count[0][3];
			for (int i = 0; i < k; i++) {
				for (int j = 0; j < 4; j++) {
					if (pseudo) {
						profile[i][j] = ((double)count[i][j]+1)/((double)numMotifs+4);
					}
					else {
						profile[i][j] = (double)count[i][j]/(double)numMotifs;
					}
				}
			}

			sumVec.clear();
			sum = 0.0;
			replaced = dna[randNum];
			for (int i = 0; i <= strLen - k; i++) {
				pr = 1.0;
				for (int j = 0; j < k; j++) {
					pr *= (double)profile[j][symbolToNumber(replaced.at(i+j))];
				}
				sum += pr;
				sumVec.push_back(sum);
			}

			randPr = (double)rand()/(double)RAND_MAX * (sum);
			//cout << "randPr = " << randPr << "  sum = " << sum << endl;
			if (randPr <= sumVec[0]) {
				index = 0;
			}
			else {
				for (int i = 1; i < sumVec.size(); i++) {
					if (randPr > sumVec[i-1] && randPr <= sumVec[i]) {
						index = i;
						break;
					}
				}
			}

			for (int i = 0; i < k; i++) {
				count[i][symbolToNumber(replaced.at(index+i))]++;
			}

			motifs[randNum] = replaced.substr(index, k);

			score = Score(count, k);
			//cout << "Score: " << score << endl;
			if (score < bestScore) {
				bestScore = score;
				bestMotifs = motifs;
			}
		}

		if (bestScore < lowestScore) {
			lowestScore = bestScore;
			realBest = bestMotifs;
		}
	}
	return realBest;
}