#ifndef _COUNTER_H_
#define _COUNTER_H_

#include <queue>
#include <vector>

#include "tbb/concurrent_vector.h"
#include "tbb/concurrent_hash_map.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"

#include "defines.h"

using namespace std;
using namespace tbb;

RetVal Counter();

#endif
