//
//  patternToNumber.cpp
//
//
//  Created by Shenmo Lu on 1/10/17.
//
//

#include <stdio.h>
#include <string>
#include <math.h>
#include "functions.hpp"

using namespace std;

long patternToNumber(string pattern) {
	long num = 0;
	for (int i = 0; i < pattern.length(); i++) {
		char symbol = pattern.at(pattern.length() - i - 1);
		num += pow(4, i) * symbolToNumber(symbol);
	}
	return num;
}