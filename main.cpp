//
//  main.cpp
//  
//
//  Created by Shenmo Lu on 1/9/17.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <list>
#include <ctime>
#include <string>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <random>
#include <time.h>
#include "functions.hpp"

using namespace std;

int main(int argc, char *argv[]) {
    clock_t start;
    string text;
    string pattern;
    string str;
    int d = 0;
    double x;
    //int k;
    //int pc, fw;
    list<string> l;
    fstream myfile;
    myfile.open("/Users/penny/Desktop/data.txt");

/*
    int k, t, N;
    myfile >> k;
    myfile >> t;
    myfile >> N;
    vector<string> dna;
    while (myfile >> text) {
        dna.push_back(text);
    }

    vector<string> vrms = GibbsSampler(dna, k, t, N);
    cout << "\noutput: "<< endl;
    for (int i = 0; i < vrms.size(); i++) {
        cout << vrms[i] << endl;
    }*/

/*
    srand (time(NULL));
    vector<double> sumVec;
    int index;
    sumVec.push_back(2);
    sumVec.push_back(3);
    sumVec.push_back(6);
    int zero = 0;
    int one = 0;
    int two = 0;
    int randPr;
    cout << "just rand" <<rand();
    //cout << "randPr = " << randPr << "  sum = " << sum << endl;
    for (int r = 0; r < 100; r++) {
        randPr = ((double)rand())/((double)RAND_MAX)*6;
        cout << "randPr" << randPr <<" ";
        if (randPr <= sumVec[0]) {
            index = 0;
        }
        else {
            for (int i = 0; i < sumVec.size(); i++) {
                if (randPr > sumVec[i-1] && randPr <= sumVec[i]) {
                    index = i;
                    break;
                }
            }
        }

        if (index == 0) {
            zero++;
        }
        if (index == 1) one++;
        if (index == 2) two++;
    }

    cout << zero << " " <<one << " " << two;
*/
/*********************************************************************************************

*********************************************************************************************/

/*********************************************************************************************
    int k, t;
    myfile >> k;
    myfile >> t;
    vector<string> dna;
    while (myfile >> text) {
        dna.push_back(text);
    }

    vector<string> vrms = RandomizedMotifSearch(dna, k, t);
    cout << "\noutput: "<< endl;
    for (int i = 0; i < vrms.size(); i++) {
        cout << vrms[i] << endl;
    }
*********************************************************************************************/

/*********************************************************************************************
    myfile >> k;
    myfile >> t;
    vector<string> dna;
    while (myfile >> text) {
        dna.push_back(text);
    }

    vector<string> vgmsp = GreedyMotifSearchWithPseudocounts(dna, k, t);
    cout << "\noutput: "<< endl;
    for (int i = 0; i < vgmsp.size(); i++) {
        cout << vgmsp[i] << endl;
    }
*********************************************************************************************/

/*********************************************************************************************
    int k, t;
    myfile >> k;
    myfile >> t;
    vector<string> dna;
    while (myfile >> text) {
        dna.push_back(text);
    }

    vector<string> vgms = GreedyMotifSearch(dna, k, t);
    cout << "\noutput: "<< endl;
    for (int i = 0; i < vgms.size(); i++) {
        cout << vgms[i] << endl;
    }
*********************************************************************************************/
 /*   myfile >> text;
    myfile >> d;
    double profile[d][4];
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < d; j++) {
            myfile >> x;
            profile[j][i] = x;
        }
    }

    string kmer = profileMostProbableKmer(text, d, profile);
    cout << kmer;*/
/*********************************************************************************************
    myfile >> text;
    myfile >> d;
    double profile[d][4];
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < d; j++) {
            myfile >> x;
            profile[j][i] = x;
        }
    }

    string kmer = profileMostProbableKmer(text, d, profile);
    cout << kmer;
*********************************************************************************************/
   vector<string> dna;
    getline(myfile, str);
    d = stoi(str);
    
    while (!myfile.eof()) {
        getline(myfile, text);
        dna.push_back(text);
    }

    vector<string> median = medianString(dna, d);
    for (int i = 0; i < median.size(); i++) {
        cout << median[i] << endl;
    }
/*********************************************************************************************
    vector<string> dna;
    getline(myfile, str);
    d = stoi(str);
    
    while (!myfile.eof()) {
        getline(myfile, text);
        dna.push_back(text);
    }

    string median = medianString(dna, d);
    cout << median << endl;
*********************************************************************************************/

/*********************************************************************************************
    vector<string> dna;
    getline(myfile, pattern);
    while (myfile >> text) {
        dna.push_back(text);
    }
    int distance = distanceBetweenPatternAndStrings(pattern, dna);
    cout << distance << endl;
*********************************************************************************************/

/*********************************************************************************************
    vector<string> dna;
    getline(myfile, str);
    while (!myfile.eof()) {
        getline(myfile, text);
        dna.push_back(text);
    }

    vector<string> vme = motifEnumeration(dna, 5, 2);
    cout << vme[0];
    for (int i = 1; i < vme.size(); i++) {
        cout  << " " << vme[i];
    }
*********************************************************************************************/

/*********************************************************************************************
    text = "ACGTTGCATGTCGCATGATGCATGAGAGCT";
    vector<string> vfwmr = freqWordsWithMismatchesAndRevComp(text, 4, 1);
    for (int i = 0; i < vfwmr.size(); i++) {
        cout << vfwmr[i] << " ";
    }
*********************************************************************************************/

/*********************************************************************************************
    getline(myfile, text);;
    vector<string> vfwwm = frequentWordsWithMismatches(text, 6, 3);
    for (int i = 0; i < vfwwm.size(); i++) {
        cout << vfwwm[i] << " ";
    }
*********************************************************************************************/

/*********************************************************************************************
    getline(myfile, pattern);
    getline(myfile, str);
    d = stoi(str);

    vector<string> vn = neighbors(pattern, d);
    for (int i = 0; i < vn.size(); i++) {
        cout << vn[i] << endl;
    }
    cout << endl;
    cout << "size: " << vn.size() << endl;
*********************************************************************************************/

/*********************************************************************************************
    //getline(myfile, pattern);
    //getline(myfile, text);
    //getline(myfile, str);
    //d = stoi(str);

    pattern = "";
    text = "";
    d = ;

    vector<int> vap = ApproximatePattern(pattern, text, d);

    for (int i = 0; i < vap.size(); i++) {
        cout << vap[i] << " ";
    }
    cout << endl;
    cout << "size: " << vap.size() << endl;
*********************************************************************************************/

/*********************************************************************************************
    text = "";
    vector<int> vms = minimumSkew(text);
    for (int i = 0; i < vms.size(); i++) {
        cout << vms[i] << " ";
    }
    cout << endl;
*********************************************************************************************/

/*********************************************************************************************
    string p, q;
    p = "";
    q = "";
    //getline(myfile, p);
    //getline(myfile, q);
    cout << hammingDistance(p, q) << endl;
*********************************************************************************************/

/*********************************************************************************************
    vector<int> array = computingFrequencies(text, 8);
    for (int i = 0; i < array.size(); i++) {
        cout << array[i] << " ";
    }
    cout << endl;
*********************************************************************************************/

/*********************************************************************************************
    start = clock();
    vector<string> vcf = clumpFinding(text, 10 ,548, 20);
    std::cout << "Time: " << (clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms" << std::endl;
    for (int i = 0; i < vcf.size(); i++) {
        cout << vcf[i] << " ";
    }
    cout << "\nsize: " << vcf.size() << endl;
*********************************************************************************************/

    //char* tstr = stringToCharArray("A");

    //cout << "pattern to number: " << patternToNumber("ATGCAA") << endl;
    //cout << "number to pattern: " << numberToPattern(5437, 8) << endl;
    //cout << "reverse complement: " << reverseComplement("AAAACCCGGT") << endl;

/*********************************************************************************************
    cout << "pattern matching: " << endl;
    vector<int> vpm = patternMatching(text, pattern);
    for (int i = 0; i < vpm.size(); i++) {
        cout << vpm[i] << " ";
    }
    cout << endl;
*********************************************************************************************/

/*********************************************************************************************
    getline(myfile, pattern);
    pc = patternCount(text, pattern);
    cout << pc << endl;
*********************************************************************************************/
    
/*********************************************************************************************
    k = atoi(argv[2]);
    fw = frequentWords(l, text, k);
    for (list<string>::iterator it = l.begin(); it != l.end(); it++) {
        std::cout << *it << ' ';
    }
    cout << endl;
*********************************************************************************************/
    myfile.close();
}
