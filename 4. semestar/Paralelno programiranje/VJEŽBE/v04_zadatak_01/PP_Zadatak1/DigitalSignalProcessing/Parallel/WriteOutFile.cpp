#include "WriteOutFile.h"


extern concurrent_hash_map<unsigned char, unsigned int> couterValues;

RetVal WriteOutFile(string fileName)
{
    ofstream outputFile(fileName.c_str());

	if (outputFile.is_open() == false)
	{
        cout << "WriteOutFile: Output file " << fileName << " could not be opened." << endl;
		return RET_ERROR;
	}

	concurrent_hash_map<unsigned char, unsigned int>::const_accessor ac;
	for (int i = 0; i < couterValues.size(); i++)
	{
		if (couterValues.find(ac, i))
		{
			outputFile << i << ":\t" << ac->second << endl;
		}
	}

    outputFile.close();

    return RET_OK;
}
