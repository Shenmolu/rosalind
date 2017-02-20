//
//  frequentWords.cpp
//  
//
//  Created by Shenmo Lu on 1/10/17.
//
//

#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <string>
#include <iterator>
#include <algorithm>
#include "functions.hpp"

using namespace std;

int frequentWords(list<string>& l, string text, int k) {
    int tsize = text.size();
    int max = 0;
    string kmer;
    map<string, int> counts;
    map<string, int>::iterator it;
    
    for (int i = 0; i <= tsize - k; i++) {
        kmer = text.substr(i, k);
        it = counts.find(kmer);
        if (it != counts.end()) {
            if (++counts[kmer] > max) {
                max = counts[kmer];
            }
        }
        else {
            counts.insert(make_pair(kmer, 1));
            if (max == 0) {
                max++;
            }
        }
    }
    
    it = counts.begin();
    while (it != counts.end()) {
        if (it->second == max) {
            l.push_back(it->first);
        }
        it++;
    }
    
    return l.size();
}
