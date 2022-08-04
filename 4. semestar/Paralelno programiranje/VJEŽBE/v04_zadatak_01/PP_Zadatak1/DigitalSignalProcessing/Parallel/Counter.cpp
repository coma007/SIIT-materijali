#include "Counter.h"
#include <iostream>

extern concurrent_vector<unsigned char> clip2CounterVector;
extern concurrent_hash_map<unsigned char, unsigned int> couterValues;

struct CounterClass {
    void operator() (const blocked_range<unsigned int>& range) const {
        for (unsigned int i = range.begin(); i != range.end(); i++) {
            concurrent_hash_map<unsigned char, unsigned int>::accessor a;
            unsigned char c = clip2CounterVector[i];
            couterValues.insert(a, clip2CounterVector[i]);
            a->second+=1;
        }
    }

};

RetVal Counter()
{

    int size = clip2CounterVector.size();
    CounterClass cc;
    parallel_for(blocked_range<unsigned int>(0, size), cc);

    return RET_OK;
}
