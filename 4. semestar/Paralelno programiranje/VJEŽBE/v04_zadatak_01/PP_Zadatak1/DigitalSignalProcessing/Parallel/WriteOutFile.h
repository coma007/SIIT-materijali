#ifndef _WRITE_OUT_FILE_H_
#define _WRITE_OUT_FILE_H_

#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include "defines.h"
#include "tbb\concurrent_hash_map.h"

using namespace std;
using namespace tbb;

RetVal WriteOutFile(string fileName);

#endif
