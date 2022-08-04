#include "Clip.h"
#include <iostream>

extern concurrent_vector<short> highPass2ClipVector;
extern concurrent_vector<unsigned char> clip2CounterVector;

struct ClipClass {
    char lowerValue;
    char upperValue;
    ClipClass(char lV, char uV) : lowerValue(lV), upperValue(uV) {};
    void operator() (const blocked_range<int>& range) const {
        for (int i = range.begin(); i != range.end(); i++) {
            short data = highPass2ClipVector[i];
            if (data < lowerValue)
            {
                clip2CounterVector.push_back(lowerValue);
            }
            else if (data > upperValue)
            {
                clip2CounterVector.push_back(upperValue);
            }
        }
    }

};

RetVal Clip(char lowerValue, char upperValue)
{

    // clipping loop
    ClipClass cc(lowerValue, upperValue);
    int size = highPass2ClipVector.size();
    parallel_for(blocked_range<int>(0, size), cc);

    return RET_OK;
}
