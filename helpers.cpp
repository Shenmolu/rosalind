//
//  helpers.cpp
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

char* stringToCharArray(string str) {
    char* cstr = new char[str.length() + 1];
    strcpy(cstr, str.c_str());
    return cstr;
}

char complementBase(char base) {
	switch(base) {
		case 'A': return 'T';
		case 'C': return 'G';
		case 'G': return 'C';
		case 'T': return 'A';
	}
	return -1;
}





