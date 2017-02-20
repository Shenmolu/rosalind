//
//  numberToPattern.cpp
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

string numberToPattern(int num, int k) {
	int rem;
	string str = "";
	while (num > 0) {
		rem = num % 4;
		str = numberToSymbol(rem) + str;
		num /= 4;
	}

	while (str.size() < k) {
		str = 'A' + str;
	}

	return str;
}