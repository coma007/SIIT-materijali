#ifndef _HIGH_PASS_FILTER_H_
#define _HIGH_PASS_FILTER_H_

#include <queue>
#include "defines.h"

#include "tbb/concurrent_vector.h"

using namespace std;
using namespace tbb;

RetVal HighPassFilter(float alpha);

#endif
