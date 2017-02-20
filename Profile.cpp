//
//  Profile.cpp
//
//
//  Created by Shenmo Lu on 1/22/17.
//
//

#include <vector>
#include <string>
#include "functions.hpp"

vector<vector<double>> Profile(vector<vector<int> count, int k, int t, bool pseudo) {
	vector<vector<double>> profile;
	bool addCount = false;
	int total = count[0][0] + count[0][1] + count[0][2] + count[0][3];
	if (pseudo) {
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < 4; j++) {
				if (count[i][j] == 0) {
					pseudo = true;
					goto next;
				}
			}
		}
	}
	next:
	for (int i = 0; i < k; i++) {
		for (int j = 0; j < 4; j++) {
			if (pseudo) {
				profile[i][j] = ((double)count[i][j]+1)/((double)total+1);
			}
			else {
				profile[i][j] = (double)count[i][j]/(double)total;
			}
		}
	}
}