//
//  motifEnumeration.cpp
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

vector<string> motifEnumeration(vector<string> dna, int k, int d) {
	vector<string> motifs;
	vector<string> neighborhood;
	vector<int> pos;

	string pattern;
	int strLen = dna[0].length();
	bool flag;
	long number;

	int size = (int)pow(4, k);
	vector<bool> patterns;
	patterns.resize(size, true);

	for (int i = 0; i <= strLen - k; i++) {
		pattern = dna[0].substr(i, k);
		neighborhood = neighbors(pattern, d);

		for (int j = 0; j < neighborhood.size(); j++) {
			flag = true;
			// for each string
			for (int m = 1; m < dna.size(); m++) {
				pos = ApproximatePattern(neighborhood[j], dna[m], d);
				if (pos.size() == 0) {
					flag = false;
					break;
				}
			}

			number = patternToNumber(neighborhood[j]);
			if (flag && patterns[number]) {
				motifs.push_back(neighborhood[j]);
				patterns[number] = false;
			}
		}
	}
	return motifs;
}