//
//  patternCount.cpp
//
//
//  Created by Shenmo Lu on 1/9/17.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>
#include "functions.hpp"

using namespace std;

int patternCount(string text, string pattern) {
    int count = 0;
    int tsize = text.size();
    int psize = pattern.size();
    string kmer;
    
    for (int i = 0; i < tsize - psize; i++) {
        kmer = text.substr(i, psize);
        if (kmer.compare(pattern) == 0) {
            count++;
        }
    }
    
    return count;
}
