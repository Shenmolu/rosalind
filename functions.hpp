//
//  helpers.hpp
//  
//
//  Created by Shenmo Lu on 1/9/17.
//
//

#ifndef patternCount_hpp
#define patternCount_hpp
#include <iostream>
#include <list>
#include <vector>

std::vector<int> ApproximatePattern(std::string pattern, std::string text, int d);

std::vector<std::string> clumpFinding(std::string genome, int k, int l, int t);

char complementBase(char base);

std::vector<int> computingFrequencies(std::string text, int k);

std::vector<std::vector<int> > Count(std::vector<std::string> motifs, int k, int t);

int distanceBetweenPatternAndStrings(std::string pattern, std::vector<std::string> dna);

int frequentWords(std::list<std::string>& l, std::string text, int k);

std::vector<std::string> frequentWordsWithMismatches(std::string text, int k, int d);

std::vector<std::string> freqWordsWithMismatchesAndRevComp(std::string text, int k, int d);

std::vector<std::string> GibbsSampler(std::vector<std::string> dna, int k, int t, int N);

std::vector<std::string> GreedyMotifSearch(std::vector<std::string> dna, int k, int t);

std::vector<std::string> GreedyMotifSearchWithPseudocounts(std::vector<std::string> dna, int k, int t);

int hammingDistance(std::string p, std::string q);

std::vector<std::string> medianString(std::vector<std::string> dna, int k);

std::vector<int> minimumSkew(std::string text);

std::vector<std::string> motifEnumeration(std::vector<std::string> dna, int k, int d);

std::vector<std::string> neighbors(std::string pattern, int d);

std::string numberToPattern(int num, int k);

char numberToSymbol(int number);

int patternCount(std::string text, std::string pattern);

std::vector<int> patternMatching(std::string text, std::string pattern);

long patternToNumber(std::string pattern);

std::vector<std::vector<double> > Profile(std::vector<std::vector<int> > count, int k, int t, bool pseudo);

std::string profileMostProbableKmer(std::string text, int k, double profile[][4]);

std::vector<std::string> RandomizedMotifSearch(std::vector<std::string> dna, int k, int t);

std::string reverseComplement(std::string pattern);

int Score(int count[][4], int k);

char* stringToCharArray(std::string str);

int symbolToNumber(char symbol);

#endif /* functions_hpp */
