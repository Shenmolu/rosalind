//
//  Count.cpp
//
//
//  Created by Shenmo Lu on 1/22/17.
//
//

#include <vector>
#include <string>
#include "functions.hpp"

using namespace std;

vector<vector<int>> Count(vector<string> motifs, int k, int t) {
	vector<vector<int>> count;
	for (int i = 0; i < k; i++) {
		for (int j = 0; j < 4; j++) {
			count[i][j] = 0;
		}
	}

	for (int i = 0; i < t; i++) {
		for (int j = 0; j < k; j++) {
			count[j][symbolToNumber(motifs[i].at(j))]++;
		}
	}
	return count;
}