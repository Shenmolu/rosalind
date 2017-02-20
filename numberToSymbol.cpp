//
//  numberToSymbol.cpp
//  
//
//  Created by Shenmo Lu on 1/11/17.
//
//

#include <stdio.h>
#include "functions.hpp"

using namespace std;

char numberToSymbol(int number) {
	switch(number) {
		case 0: return 'A';
		case 1: return 'C';
		case 2: return 'G';
		case 3: return 'T';
	}
	return '\0';
}