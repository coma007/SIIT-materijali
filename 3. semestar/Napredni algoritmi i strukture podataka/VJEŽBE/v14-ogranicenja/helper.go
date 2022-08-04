package main

import (
	"time"
)

func Now() int64 {
	return time.Now().Unix()
}

func IsPast(stored int64) bool {
	return stored < Now()
}
