package main

import (
	"errors"
	"fmt"
)

func prime(number int) (int, error){

	if number < 1 {
		return 0, errors.New("index less than 1")
	}

	var n = 1000000
	nonprimes := make([]bool, n+1, n+1)
	var p = 2
	for p*p <= n {
		if nonprimes[p] == false {
			var i = p*p
			for i < n {
				nonprimes[i] = true
				i += p
			}
		}
		p += 1
	}
	primes := make([]int, 0 , n+1)
	for i, v := range nonprimes {
		if  v == false {
			primes = append(primes, i)
		}
	}

	return primes[number+1], nil
}

func main() {

	number := 1000
	result, err := prime(number)
	if err != nil {
		fmt.Println("Error: ", err.Error())
	} else {
		fmt.Println(number, ". prime number is: ", result)
	}

}
