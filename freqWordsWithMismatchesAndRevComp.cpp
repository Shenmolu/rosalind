//
//  reverseComplement.cpp
//
//
//  Created by Shenmo Lu on 1/21/17.
//
//

#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include "functions.hpp"

using namespace std;

vector<string> freqWordsWithMismatchesAndRevComp(string text, int k, int d) {
	vector<string> frequentPatterns;
	vector<string> neighborhood;
	vector<string> revNeighborhood;

	int size = (int)pow(4, k);
	int frequencyArray[size];
	int index;
	int count;
	int maxCount = 0;
	int neighborhoodSize;
	string pattern;
	string revComp;


	for (int i = 0; i < size; i++) {
		frequencyArray[i] = 0;
	}

	revComp = reverseComplement(text);

	for (int i = 0; i <= text.length() - k; i++) {
		neighborhood = neighbors(text.substr(i, k), d);
		neighborhoodSize = neighborhood.size();
		revNeighborhood = neighbors(revComp.substr(i, k), d);

		for (int j = 0; j < neighborhoodSize; j++) {
			index = patternToNumber(neighborhood[j]);
			frequencyArray[index]++;
			index = patternToNumber(revNeighborhood[j]);
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
