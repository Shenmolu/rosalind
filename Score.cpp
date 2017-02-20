//
//  Score.cpp
//
//
//  Created by Shenmo Lu on 1/22/17.
//
//

#include <vector>
#include "functions.hpp"

using namespace std;

int Score(int count[][4], int k) {
	int max;
	int score = 0;
	int total = count[0][0] + count[0][1] + count[0][2] + count[0][3];
	for (int i = 0; i < k; i++) {
		max = 0;
		for (int j = 0; j < 4; j++) {
			if (max < count[i][j]) {
				max = count[i][j];
			}
		}
		score += (total - max);
	}
	return score;
}