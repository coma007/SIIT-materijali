package main

import (
	"fmt"
	"math"
)

func checkArmstrong(number int) bool {

	left := number
	sum := 0.0
	for left > 0 {
		sum += math.Pow(float64(left % 10), 3)
		left /= 10
	}
	fmt.Println(number)
	fmt.Println(sum)
	return float64(number) == sum

}


func main() {

	fmt.Println(checkArmstrong(548834))



}
