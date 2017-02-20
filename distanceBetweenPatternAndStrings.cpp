//
//  distanceBetweenPatternAndStrings.cpp
//
//
//  Created by Shenmo Lu on 1/21/17.
//
//

#include <math.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <climits>
#include "functions.hpp"

using namespace std;

int distanceBetweenPatternAndStrings(string pattern, vector<string> dna) {
	int k = pattern.length();
	int distance = 0;
	int hammingDist;
	int minDist;
	int strLen = dna[0].length();
	string text;
	string kmer;

	for (int i = 0; i < dna.size(); i++) {
		minDist = INT_MAX;
		text = dna[i];
		for (int j = 0; j <= strLen - k; j++) {
			kmer = text.substr(j, k);
			hammingDist = hammingDistance(pattern, kmer);
			if (minDist > hammingDist) {
				minDist = hammingDist;
			}
		}
		distance += minDist;
	}
	return distance;
}