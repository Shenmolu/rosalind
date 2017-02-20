//
//  frequentWordsWithMismatches.cpp
//
//
//  Created by Shenmo Lu on 1/15/17.
//
//

#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include "functions.hpp"

using namespace std;

vector<string> frequentWordsWithMismatches(string text, int k, int d) {
	vector<string> frequentPatterns;
	vector<string> neighborhood;

	int size = (int)pow(4, k);
	int frequencyArray[size];
	int index;
	int count;
	int maxCount = 0;
	string pattern;

	for (int i = 0; i < size; i++) {
		frequencyArray[i] = 0;
	}

	for (int i = 0; i <= text.length() - k; i++) {
		neighborhood = neighbors(text.substr(i, k), d);

		for (int j = 0; j < neighborhood.size(); j++) {
			index = patternToNumber(neighborhood[j]);
			frequencyArray[index]++;
		}
	}

	for (int i = 0; i < size; i++) {
		count = frequencyArray[i];
		if (count > maxCount) {
			cout << count << " ";
			frequentPatterns.clear();
			frequentPatterns.push_back(numberToPattern(i, k));
			maxCount = count;
		}
		else if (count == maxCount) {
			frequentPatterns.push_back(numberToPattern(i, k));
		}
	}

	return frequentPatterns;
}