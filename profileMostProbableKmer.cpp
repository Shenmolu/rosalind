//
//  profileMostProbableKmer.cpp
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

string profileMostProbableKmer(string text, int k, double profile[][4]) {
	int pos = 0;
	double pr = 1;
	double maxPr = 0;
	int strLen = text.length();
	int bases[strLen];

	for (int i = 0; i < strLen; i++) {
		bases[i] = symbolToNumber(text.at(i));
	}

	for (int i = 0; i <= strLen - k; i++) {
		pr = 1;
		for (int j = 0; j < k; j++) {
			pr = pr * profile[j][bases[i+j]];
		} 
		if (pr > maxPr) {
			maxPr = pr;
			pos = i;
		}
	}
	return text.substr(pos, k);
}