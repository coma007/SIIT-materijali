#include "ReadInFile.h"

extern queue<unsigned char> in2HighPassQueue;

RetVal ReadInFile(string fileName)
{
    unsigned char data;
    FILE* inputFile = fopen(fileName.c_str(), "rb");

	if (inputFile == NULL)
    {
        cout << "ReadInFile: Input file " << fileName << " could not be opened." << endl;
		return RET_ERROR;
	}

    while(fread(&data, sizeof(unsigned char), 1, inputFile))
    {
        in2HighPassQueue.push(data);
    }

    fclose(inputFile);

    return RET_OK;
}
