//
//  ApproximatePattern.cpp
//
//
//  Created by Shenmo Lu on 1/11/17.
//
//

#include <stdio.h>
#include <string>
#include "functions.hpp"

using namespace std;

vector<int> ApproximatePattern(string pattern, string text, int d) {
	string kmer;
	vector<int> pos;
	int k = pattern.length();
	for (int i = 0; i <= text.length() - k; i++) {
		kmer = text.substr(i, k);
		if (hammingDistance(kmer, pattern) <= d) {
			pos.push_back(i);
		}
	}
	return pos;
}