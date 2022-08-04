#ifndef _CLIP_H_
#define _CLIP_H_

#include <queue>
#include <vector>

#include "tbb/concurrent_vector.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"

#include "defines.h"

using namespace std;
using namespace tbb;

RetVal Clip(char lowerValue, char upperValue);

#endif
