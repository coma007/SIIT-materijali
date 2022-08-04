#include "Counter.h"

extern vector<unsigned char> clip2CounterVector;
extern unsigned int couterValues[256];

RetVal Counter()
{
    unsigned char data;

    // array initialization
    memset(couterValues, 0x00, 256*sizeof(unsigned int));

    // count each value
    while(!clip2CounterVector.empty())
    {
        data = clip2CounterVector.back();
        clip2CounterVector.pop_back();

        couterValues[data]++;
    }
    return RET_OK;
}
