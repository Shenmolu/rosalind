//
//  minimumSkew.cpp
//
//
//  Created by Shenmo Lu on 1/11/17.
//
//

#include <stdio.h>
#include <string>
#include <vector>
#include "functions.hpp"

using namespace std;


vector<int> minimumSkew(string text) {
	int skew = 0;
	int min = 0;
	vector<int> pos;
	pos.push_back(0);

	for (int i = 0; i < text.length(); i++) {
		char c = text[i];
		if(c == 'G') {
			++skew;
		}
		else {
			if (c == 'C') {
				--skew;
				if(skew < min) {
					pos.clear();
					pos.push_back(i+1);
					min = skew;
					continue;
				}
			}

			if (skew == min) {
				pos.push_back(i+1);
			}
		}
	}

	return pos;
}