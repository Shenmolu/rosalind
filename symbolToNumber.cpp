//
//  symbolToNumber.cpp
//  
//
//  Created by Shenmo Lu on 1/11/17.
//
//

#include <stdio.h>
#include "functions.hpp"

using namespace std;

int symbolToNumber(char symbol) {
	switch(symbol) {
		case 'A': return 0;
		case 'C': return 1;
		case 'G': return 2;
		case 'T': return 3;
	}
	return -1;
}