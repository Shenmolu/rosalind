//
//  medianString.cpp
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

vector<string> medianString(vector<string> dna, int k) {
	int distance = INT_MAX;
	string pattern;
	vector<string> median;
	for (int i = 0; i < pow(4, k); i++) {
		pattern = numberToPattern(i, k);
		int dist = distanceBetweenPatternAndStrings(pattern, dna);
		if (distance >= dist) {
			distance = dist;
			cout << dist << " " << pattern << endl;
		}
	}
	return median;
}