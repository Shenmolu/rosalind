//
//  hammingDistance.cpp
//
//
//  Created by Shenmo Lu on 1/10/17.
//
//

#include <stdio.h>
#include <string>
#include "functions.hpp"

using namespace std;

int hammingDistance(string p, string q) {
	int distance = 0;
	for (int i = 0; i < p.length(); i++) {
		if (p[i] != q[i]) {
			distance++;
		}
	}
	return distance;
}