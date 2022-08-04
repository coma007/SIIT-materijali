#include "Clip.h"

extern queue<short> highPass2ClipVector;
extern vector<unsigned char> clip2CounterVector;

RetVal Clip(char lowerValue, char upperValue)
{
    short data;

    // clipping loop
    while(!highPass2ClipVector.empty())
    {
        data = highPass2ClipVector.front();
        highPass2ClipVector.pop();

        if(data<lowerValue)
        {
            data = lowerValue;
        }
        else if(data>upperValue)
        {
            data = upperValue;
        }

        clip2CounterVector.push_back(data);
    }
    return RET_OK;
}
