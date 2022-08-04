#include "WriteOutFile.h"

extern unsigned int couterValues[256];

RetVal WriteOutFile(string fileName)
{
    ofstream outputFile(fileName.c_str());

	if (outputFile.is_open() == false)
	{
        cout << "WriteOutFile: Output file " << fileName << " could not be opened." << endl;
		return RET_ERROR;
	}


    for(int i=0; i<256; i++)
    {
        if(couterValues[i])
        {
            outputFile << i << ":\t" << couterValues[i] << endl;
        }
    }

    outputFile.close();

    return RET_OK;
}
