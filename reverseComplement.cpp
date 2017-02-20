//
//  reverseComplement.cpp
//
//
//  Created by Shenmo Lu on 1/10/17.
//
//

#include <stdio.h>
#include <string>
#include "functions.hpp"

using namespace std;

string reverseComplement(string pattern) {
	string recom = "";
	for (int i = 0; i < pattern.size(); i++) {
		recom = complementBase(pattern.at(i)) + recom;
	}
	return recom;
}
