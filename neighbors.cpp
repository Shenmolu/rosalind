//
//  neighbors.cpp
//
//
//  Created by Shenmo Lu on 1/14/17.
//
//

#include <stdio.h>
#include <vector>
#include <string>
#include "functions.hpp"

using namespace std;

vector<string> neighbors(string pattern, int d) {
	vector<string> neighborhood;
	vector<string> suffixNeighbors;
	string suffix;
	string text;

	if (d == 0) {
		neighborhood.push_back(pattern);
		return neighborhood;
	}

	if (pattern.length() == 1) {
		neighborhood.push_back("A");
		neighborhood.push_back("C");
		neighborhood.push_back("G");
		neighborhood.push_back("T");
		return neighborhood;
	}

	suffix = pattern.substr(1);
	suffixNeighbors = neighbors(suffix, d);

	for (int i = 0; i < suffixNeighbors.size(); i++) {
		text = suffixNeighbors[i];
		if (hammingDistance(suffix, text) < d) {
			neighborhood.push_back("A" + text);
			neighborhood.push_back("C" + text);
			neighborhood.push_back("G" + text);
			neighborhood.push_back("T" + text);
		}
		else {
			neighborhood.push_back(pattern.substr(0,1) + text);
		}
	}

	return neighborhood;
}



/*
void removeDuplicate(vector<string> vec);
vector<string> immediateNeighbors(string pattern);

vector<string> neighbors(string pattern, int d) {
	vector<string> neighborhood;
	neighborhood.push_back(pattern);

	for (int i = 1; i <= d; i++) {
		for (int j = 0; j < neighborhood.size(); j++) {
			vector<string> immedNeigh = immediateNeighbors(neighborhood[j]);
			for (int k = 0; k < 3; k++) {
				neighborhood.push_back(immedNeigh[k]);
			}
			removeDuplicate(neighborhood);
		}
	}

	return neighborhood;
}

void removeDuplicate(vector<string> vec) {
  sort(vec.begin(), vec.end());
  vec.erase(unique(vec.begin(), vec.end()), vec.end());
}

vector<string> immediateNeighbors(string pattern) {
	vector<string> neighborhood;
	for (int i = 0; i < pattern.length(); i++) {
		switch (pattern[i]) {
			case 'A':
				neighborhood.push_back(pattern.replace(i, 1, 1, 'C'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'G'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'T'));
				break;
			case 'C':
				neighborhood.push_back(pattern.replace(i, 1, 1, 'A'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'G'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'T'));
				break;
			case 'G':
				neighborhood.push_back(pattern.replace(i, 1, 1, 'A'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'C'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'T'));
				break;
			case 'T':
				neighborhood.push_back(pattern.replace(i, 1, 1, 'A'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'C'));
				neighborhood.push_back(pattern.replace(i, 1, 1, 'G'));
				break;		
		}
	}
	return neighborhood;
}

*/