//
//  computingFrequencies.cpp
//
//
//  Created by Shenmo Lu on 1/10/17.
//
//

#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
#include "functions.hpp"

using namespace std;

vector<int> computingFrequencies(string text, int k) {
	string kmer;
	int index;
	int size = (int)pow(4, k);
	vector<int> frequencyArray;
	frequencyArray.resize(size, 0);

	for (int i = 0; i <= text.size() - k; i++) {
		kmer = text.substr(i, k);
		index = patternToNumber(kmer);
		frequencyArray[index]++;
	}

	return frequencyArray;
}
/*
int* computingFrequencies(string text, int k) {
	string kmer;
	int index;
	int size = (int)pow(4, k);
	int* frequencyArray = new int[size];
	fill(frequencyArray, frequencyArray + size, 0);

	for (int i = 0; i < text.size() - k; ++i) {
		kmer = text.substr(i, k);
		index = patternToNumber(kmer);
		frequencyArray[index]++;
	}

	return frequencyArray;
}

*/