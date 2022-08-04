package main

import "fmt"

func findMaxElif(number int) string {
	if number > 0 {
		return "positive"
	} else if number < 0 {
		return "negative"
	} else {
		return "equal to 0"
	}
}

func findMaxSwitch(number int) string {
	switch number > 0 {
	case true :
		return "positive"
	default:
		switch number < 0 {
		case true:
			return "negative"
		default:
			return "equal to 0"
		}
	}
}

func main() {
	var number = -15
	fmt.Println("Number", number, "is", findMaxElif(number))
	fmt.Println("Number", number, "is", findMaxSwitch(number))
}
