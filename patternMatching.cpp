//
//  patternMatching.cpp
//
//
//  Created by Shenmo Lu on 1/10/17.
//
//

#include <stdio.h>
#include <string>
#include <vector>
#include "functions.hpp"

using namespace std;

vector<int> patternMatching(string text, string pattern) {
	vector<int> v;
	string kmer;
	int k = pattern.size();
	for (int i = 0; i <= text.length() - k; i++) {
		kmer = text.substr(i, k);
		if (pattern.compare(kmer) == 0) {
			v.push_back(i);
		}
	}
	return v;
}