package main

import "fmt"

func values(slajs []int) []int {

	retSlajs := make([]int, 0, cap(slajs))
	for i, v := range slajs {
		if v <= i {
			retSlajs = append(retSlajs, v)
		}
	}
	return retSlajs
}

func main() {

	slajs := make([]int, 0, 5)
	slajs = append(slajs, 1, 5, -1, 6, -12)
	fmt.Println("Elements with value less than index: ", values(slajs))
}
